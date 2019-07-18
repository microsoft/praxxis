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
from keras.models import clone_model
from keras.layers import LSTM
from keras.layers import Dense

def model_train(model, sequences, converter=[]):
    ##
    # hyperparameters to tune
    ##
    # n_steps: the number of input steps to be used to predict the next notebook, avg of input seq length
    n_steps = 5    # affects the training time not the complexity of the model

    # n_units: LSTM units/cells,which determines the complexity of the model 
    # (sometimes called  size_of_output, n_neurons)
    n_units = n_steps  

    # split: fraction of data used to train (vs. used for validation)
    split = 2/3

    # batch: size of each batch (right now, 2 batches per epoch)
    batch = int((1/3) * len(sequences))

    # add to the list, if necessary
    seqs, converter = encode(sequences, converter)

    # unique_file_count: size of OHE (could make larger to allow for expansion (?))
    unique_file_count = len(converter) 
    
    if model == None:
        model = model_create(n_units, n_steps, unique_file_count)

    # https://github.com/keras-team/keras/issues/1765
    new_model = clone_model(model)
    new_model.build()
    new_model.set_weights(model.get_weights())

    np.random.shuffle(seqs)
    train_seq = seqs[:int(len(seqs)*split)]
    valid_seq = seqs[int(len(seqs)*split):]

    ##
    # fit the model
    ##
    training_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)
    validation_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)

    history = model.fit_generator(training_gen, len(train_seq)//(batch), epochs=100, validation_data=validation_gen, validation_steps = len(valid_seq)//(batch*n_steps) +1, verbose=2)

    epoch_min_val = np.argmin(history.history['val_loss'])

    ##
    # retrain to point of minimum val loss, from initial model
    ##
    training_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)
    validation_gen = generate(seqs, batch_size=batch, num_steps=n_steps, total_names=unique_file_count)

    history = new_model.fit_generator(training_gen, len(train_seq)//(batch), epochs=epoch_min_val, verbose=2)

    return new_model


def model_create(n_units, n_steps, unique_file_count):
    # optimizer: using adam, as is standard
    # adam's base learning rate: 0.001
    from keras import optimizers
    adam = optimizers.adam(lr=0.001)

    # loss: also consider binary cross_entropy
    loss_func = 'categorical_crossentropy'

    # features considered (right now, just filenames)
    n_features = 1

    ##
    # define and compile model
    ##
    model = Sequential()
    
    # input_shape = (time_step, seq_len)
    #    time_step = # timesteps considered
    #    seq_len= # of features considerd 
    model.add(LSTM(n_units, input_shape=(n_steps, n_features)))

    # size = length of OHE array
    model.add(Dense(unique_file_count, activation='softmax'))
    
    model.compile(loss=loss_func, optimizer=adam, metrics=['acc'])

    return model



import collections 

import numpy as np
from numpy import array
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical


def encode(sequences, converter=["<None>","<Unknown>"]):
    newSeqs = []
    for seq in sequences:
        newSeq = []
        for filename in seq:
            if filename not in converter:
                converter.append(filename)
            newSeq.append(converter.index(filename))
        newSeqs.append(newSeq)
    return newSeqs, converter

def pad_sequence(sequence, length, value=0):
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence[(len(sequence) - length):]


def one_hot_encode(sequence, ohe):
    encoded = ohe.transform(array(sequence).reshape(len(sequence), 1))
    return encoded

def generate(sequences, batch_size, num_steps, total_names):
    x = np.zeros((batch_size, num_steps))
    #y = np.zeros((batch_size, num_steps, total_names))
    y= np.zeros((batch_size, total_names))
    i = 0
    while True:
        for sequence in sequences:
            for j in range(1, len(sequence)):
                x[i, :] = pad_sequence(sequence[:j], num_steps)
                # OHE based on sequence
                temp = [0] * total_names
                temp[sequence[j]] = 1
                y[i, :] = temp #to_categorical(sequence[j],num_classes=total_names) #to_categorical(pad_sequence(sequence[:j+1], num_steps), num_classes=total_names)
                i += 1
                if i == batch_size:
                    yield x.reshape(batch_size,num_steps,1), y
                    i = 0

def generate_features(sequence, length, ohe):
    padded = pad_sequence(sequence, length)
    encoded = one_hot_encode(padded, ohe)  # TODO: possible to avoid ohe with tensorflow?

    features = ohe.categories_[0]
    n_features = len(features)

    # reshape sequence to be 3D
    x = encoded[-length:].reshape((1, length, n_features))

    return x

def decode(encoded, converter):
    decoded = converter[int(encoded[0])]
    return decoded

def one_hot_decode(encoded, converter):
    index = encoded.tolist()[0].index(1)
    return converter[int(index)]

