# build a LSTM model with mtool notebook execution sequences for predicting next
import os
import time
import numpy as np
import pandas as pd

from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.externals import joblib

from keras.models import Sequential
from keras.models import load_model
from keras.layers import LSTM
from keras.layers import Dense

from numpy import array
from mtool_model_utils import *

sequences = []
##
# set the number of input steps to be used to predict the next
# NOTE: currently: sets the number of input steps as the average of input sequence length
# TODO: might want to choose value as hyperparameter? or better function
# NOTE: why does the number of steps not affect complexity? 
# NOTE: check out next code section. still not sure why training time impacted but not complexity
##
lens = pd.Series([len(s) for s in sequences])
# lens.hist()                # NOTE: creates histogram of sequence lengths (?)
desc = lens.describe()
n_steps = int(desc['mean'])  # affects the training time not the complexity of the model

##
# set the number of LSTM units/cells
##
n_units = n_steps  # i.e., size_of_output, which determines the complexity of the model

##
# get the name of all notebooks to be used as features
##
notebooks = sum(sequences, [])
frequency = pd.Series(notebooks).value_counts()
print(frequency)
features = sorted(set(notebooks))
n_features = len(features)  # i.e. size_of_input

##
# train an OHE with all features
##
ohe = OneHotEncoder(handle_unknown='ignore', sparse=False)
ohe.fit(array(features).reshape(n_features, 1))


##
# define and compile model
##
def define_compile_model():
    model = Sequential()
    model.add(LSTM(n_units, input_shape=(n_steps, n_features)))
    model.add(Dense(n_features, activation='softmax'))

    # https://stackoverflow.com/questions/38080035/how-to-calculate-the-number-of-parameters-of-an-lstm-network
    # LSTM params = 4 * ((size_of_input + 1) * size_of_output + size_of_output^2)
    #             = 4 * size_of_output * (size_of_input + 1 + size_of_output)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
    print(model.summary())

    return model


##
# fit the model
##
xs, ys = generate_all_samples(sequences, n_steps, ohe)
print('xs.shape: ' + str(xs.shape), '; ys.shape: ' + str(ys.shape))
split = 1/3

seed = 42
np.random.seed(seed)  # make the run deterministic

start = time.time()
model = define_compile_model()
history = model.fit(xs, ys, batch_size=1, epochs=100, verbose=2, validation_split=split, shuffle=False)
end = time.time()
elapsed = end - start

##
# diagnose the model for overfitting or underfitting
##
pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model train vs validation loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'validation'], loc='upper right')
pyplot.show()

epoch_min_val = np.argmin(history.history['val_loss'])

##
# evaluate the model with train/test split
##
x_train, x_test, y_train, y_test = train_test_split(xs, ys, test_size=split, random_state=seed)

seed = 42
np.random.seed(seed)

start = time.time()
model = define_compile_model()
history = model.fit(x_train, y_train, batch_size=1, epochs=epoch_min_val, verbose=2, shuffle=False)
end = time.time()
elapsed = end - start

model.evaluate(x_test, y_test)

##
# make predictions with the model
##
seq_new = sequences[-1]
samples = generate_samples(seq_new, n_steps, ohe)

for i, (x, y) in enumerate(samples):
    yhat_proba = model.predict_proba(x)  # model.predict(x)
    print('\nSequence: %d' % i)
    print('Sequence: %s' % [one_hot_decode(x, ohe) for x in x])
    print('Expected: %s' % one_hot_decode(y, ohe))
    print('Predicted: %s' % one_hot_decode(yhat_proba, ohe))
    print('\n%s' % str(pd.Series(yhat_proba[0], ohe.categories_).sort_values(ascending=False)))

    # yhat_class = model.predict_classes(x)
    # print('Predicted: %s' % ohe.categories_[yhat_class[0]])

##
# export the lstm model to a single file and then import
##
app_dir = "mtool-model-app"
model_file = 'lstm_model.h5'
model_path = os.path.join(app_dir, model_file)
model.save(model_path)

model_loaded = load_model(model_path)
model_loaded.evaluate(x_test, y_test)

seq_new = sequences[-1]
x = generate_features(seq_new, n_steps, ohe)
yhat_proba = model.predict(x)
series = pd.Series(yhat_proba[0], index=pd.Index(ohe.categories_[0], name='notebook'), name='probability')
series_sorted = series.sort_values(ascending=False)
print('\n%s' % str(series_sorted.reset_index()))

##
# export the ohe and then import
##

ohe_file = 'onehot_encoder.pkl'
ohe_path = os.path.join(app_dir, ohe_file)
joblib.dump(ohe, ohe_path, compress=9)
ohe_loaded = joblib.load(ohe_path)
encoded = ohe_loaded.transform(array(features).reshape(n_features, 1))
print(encoded)
