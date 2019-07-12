import os 
import warnings
import pandas as pd
#from sklearn.externals 
import joblib
from keras.models import load_model
from tensorflow import logging 

# code from mtool_model_score.py
from numpy import array
from keras.preprocessing.sequence import pad_sequences

def encode(sequence, converter):
    newSeq = []
    for filename in sequence:
        if filename not in converter:
           newSeq.append(1) #<Unknown>
        else:
            newSeq.append(converter.index(filename))
    return newSeq

def pad_sequence(sequence, length, value=0):
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence[(len(sequence) - length):]

def prep_input(sequence, converter, length):
    encoded = encode(sequence, converter)
    padded = pad_sequence(encoded, length)
    shaped = array(padded).reshape(1, length, 1)
    return shaped

def predict(sequence):
    logging.set_verbosity(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

    # load in model and converter
    converter_file = 'convert.pkl'
    converter_path = os.path.join(os.path.dirname(__file__), converter_file)
    converter = joblib.load(converter_path)

    model_file = 'lstm_model.h5'
    model_path = os.path.join(os.path.dirname(__file__),  model_file) 
    model = load_model(model_path)

    # encode sequence, pad, reshape
    # TODO: get length from model shape
    prepped_in = prep_input(sequence, converter, length=5)
    
    # predict
    data = model.predict(prepped_in)
   
    # convert results into meaningful thing
    print(pd.Series(data[0], converter).sort_values(ascending=False))

    
 