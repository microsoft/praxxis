from numpy import array
from keras.preprocessing.sequence import pad_sequences


def pad_sequence(sequence, length, value=None):
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence


def one_hot_encode(sequence, ohe):
    encoded = ohe.transform(array(sequence).reshape(len(sequence), 1))
    return encoded


def generate_features(sequence, length, ohe):
    padded = pad_sequence(sequence, length)
    encoded = one_hot_encode(padded, ohe)  # TODO: possible to avoid ohe with tensorflow?

    features = ohe.categories_[0]
    n_features = len(features)

    # reshape sequence to be 3D
    x = encoded[-length:].reshape((1, length, n_features))

    return x
