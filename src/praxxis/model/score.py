"""
This file scores an input against an LSTM model
"""
import os 
import warnings
import pandas as pd 
import joblib
from keras.models import load_model
from tensorflow import logging 

from numpy import array
from keras.preprocessing.sequence import pad_sequences


def encode(sequence, converter):
    """convert a sequence to numbers using a given converter list"""
    newSeq = []
    for filename in sequence:
        if filename not in converter:
           newSeq.append(1) #<Unknown>
        else:
            newSeq.append(converter.index(filename))
    return newSeq

def pad_sequence(sequence, length, value=0):
    """pad all sequences to length given"""
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence[(len(sequence) - length):]

def prep_input(sequence, converter, length):
    """prepare input by encoding, padding, and shaping"""
    encoded = encode(sequence, converter)
    padded = pad_sequence(encoded, length)
    shaped = array(padded).reshape(1, length, 1)
    return shaped

def predict(sequence, model_path, converter_path):
    """given a sequence, return predicted next step"""
    logging.set_verbosity(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

    # load in model and converter
    converter = joblib.load(converter_path)
    model = load_model(model_path)

    # encode sequence, pad, reshape
    # TODO: get length from model shape
    prepped_in = prep_input(sequence, converter, length=5)
    
    # predict
    data = model.predict(prepped_in)
   
    # convert results into meaningful thing
    print(pd.Series(data[0], converter).sort_values(ascending=False))

def get_files(model_db):
    """get model and converter files"""
    pass
    
 