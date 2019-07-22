"""
build a LSTM model with mtool notebook execution sequences for predicting next

questions:
SHAPE: what's going on? what should shapes be? how do I shape from generator? do I need to flatten?
    --> shape is now fixed! reshape to 3D array, batch as first dimension, timestep, then feature
    --> flattening is unnecessary though output is 1 by <# of filenames> array

FEATURES: am I right that features should be notebook sequence, etc? how do I add more?
    --> yes
    --> https://monkeylearn.com/blog/beginners-guide-text-vectorization/

OHE: is this the move? what about non-sequential data like cell output? what about new notebooks being run? during retraining, do I remake the OHE?
    --> link above, change series shaping at bottom 
    --> will probably need to update converter every training cycle

LAYERS: at what point (if any) should I look at adding more layers? what value do they add?
    --> still not sure

BATCH: is adding batches important? should batches be shuffled each time? how to choose batch size?
    --> appears to be a hyperparameter?
"""
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

from mtool_model_data import sequences
from mtool_model_utils import *

##
# hyperparameters to tune
##
# n_steps: the number of input steps to be used to predict the next notebook, avg of input seq length
lens = pd.Series([len(s) for s in sequences])
desc = lens.describe()
n_steps = int(desc['mean'])   # affects the training time not the complexity of the model

# n_units: LSTM units/cells,which determines the complexity of the model 
# (sometimes called  size_of_output, n_neurons)
n_units = n_steps  

# split: fraction of data used to train (vs. used for validation)
split = 2/3

# batch: size of each batch (right now, 2 batches per epoch)
batch = int((1/3) * len(sequences))

# optimizer: using adam, as is standard
# adam's base learning rate: 0.001
from keras import optimizers
adam = optimizers.adam(lr=0.001)

# loss: also consider binary cross_entropy
loss_func = 'categorical_crossentropy'

##
# data summary: view frequencies of notebooks in dataset
##
notebooks = sum(sequences, [])
frequency = pd.Series(notebooks).value_counts()
print(frequency)

# features considered (right now, just filenames)
n_features = 1

# first approximation, assigns each sequence a numerical equiv 
# TODO: use Tokenizer? OHE? cleaner solution?
seqs, converter = basic_counter(sequences)
#ohe = OneHotEncoder(converter, handle_unknown='ignore', sparse=False)

# unique_file_count: size of OHE (could make larger to allow for expansion (?))
unique_file_count = len(converter) 

seed = 42
np.random.seed(seed)  # make the run deterministic

np.random.shuffle(seqs)
train_seq = seqs[:int(len(seqs)*split)]
valid_seq = seqs[int(len(seqs)*split):]


##
# define and compile model
##
def define_compile_model():
    model = Sequential()
    
    # input_shape = (time_step, seq_len)
    #    time_step = # timesteps considered
    #    seq_len= # of features considerd 
    model.add(LSTM(n_units, input_shape=(n_steps, n_features)))

    # size = length of OHE array
    model.add(Dense(unique_file_count, activation='softmax'))
    
    model.compile(loss=loss_func, optimizer=adam, metrics=['acc'])
    print(model.summary())
    return model

define_compile_model()


##
# fit the model
##
training_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)
validation_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)

start = time.time()
model = define_compile_model()
history = model.fit_generator(training_gen, len(train_seq)//(batch), epochs=100, validation_data=validation_gen, validation_steps = len(valid_seq)//(batch*n_steps) +1, verbose=2)
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
training_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)
validation_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)

start = time.time()
model = define_compile_model()
history = model.fit_generator(training_gen, len(train_seq)//(batch), epochs=epoch_min_val, verbose=2)
end = time.time()
elapsed = end - start

##
# export the lstm model to a single file
##
# TODO: currently dumps model in same directory, let's... not
model_file = 'lstm_model.h5'
model_path = os.path.join(os.path.dirname(__file__), "models", model_file) 
model.save(model_path)

##
# make predictions with the model
##
np.random.shuffle(seqs)
num_tests = 3

sample = generate(seqs[:num_tests], batch_size=1, num_steps=n_steps, total_names=unique_file_count)

for i in range(num_tests):
    x, y = next(sample)
    yhat_proba = model.predict(x)
    print('\nSequence: %d' % (i+1))
    print('Sequence: %s' % [decode(val, converter) for val in x[0]])
    print('Expected: %s' % one_hot_decode(y, converter))
    print('Predicted:')

    print(pd.Series(yhat_proba[0], converter).sort_values(ascending=False))

#model.evaluate(validation_gen)


##
# export the converter as a pickle
##
converter_file = 'convert.pkl'
converter_path = os.path.join(os.path.dirname(__file__), converter_file)
joblib.dump(converter, converter_path, compress=9)