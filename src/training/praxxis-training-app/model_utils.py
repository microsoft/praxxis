"""
This file contains utilities for the model creation and retraining.
"""

import collections

import numpy as np
from numpy import array
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical


def basic_counter(sequences):
    """converts sequences of names to numbers"""
    converter = ["<None>", "<Unknown>"]
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
    """pad sequence to given length"""
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence[(len(sequence) - length):]


def one_hot_encode(sequence, ohe):
    """encode using OHE"""
    encoded = ohe.transform(array(sequence).reshape(len(sequence), 1))
    return encoded


def generate(sequences, batch_size, num_steps, total_names):
    """generator that yields sets of <batch_size> number of sequences"""
    x = np.zeros((batch_size, num_steps))
    # y = np.zeros((batch_size, num_steps, total_names))
    y = np.zeros((batch_size, total_names))
    i = 0
    while True:
        for sequence in sequences:
            for j in range(1, len(sequence)):
                x[i, :] = pad_sequence(sequence[:j], num_steps)
                # OHE based on sequence
                temp = [0] * total_names
                temp[sequence[j]] = 1
                y[i, :] = temp  # to_categorical(sequence[j],num_classes=total_names)
                # to_categorical(pad_sequence(sequence[:j+1], num_steps), num_classes=total_names)
                i += 1
                if i == batch_size:
                    yield x.reshape(batch_size, num_steps, 1), y
                    i = 0


def generate_features(sequence, length, ohe):
    """old generator for non-batch training"""
    padded = pad_sequence(sequence, length)
    encoded = one_hot_encode(padded, ohe)  # TODO: possible to avoid ohe with tensorflow?

    features = ohe.categories_[0]
    n_features = len(features)

    # reshape sequence to be 3D
    x = encoded[-length:].reshape((1, length, n_features))

    return x


def decode(encoded, converter):
    """decode using the converter"""
    decoded = converter[int(encoded[0])]
    return decoded


def one_hot_decode(encoded, converter):
    """decode using OHE"""
    index = encoded.tolist()[0].index(1)
    return converter[int(index)]

    decoded = ohe.inverse_transform(encoded)
    return decoded.squeeze().tolist()

"""
def highest_prob_five(results, converter):
    # print the most probable 5 values
    sorted = pd.Series(yhat_proba, converter).sort_values(ascending=False)
    print(sorted)
"""
