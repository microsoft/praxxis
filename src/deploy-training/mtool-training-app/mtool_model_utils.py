from mtool_model_score import *


def one_hot_decode(encoded, ohe):
    decoded = ohe.inverse_transform(encoded)
    return decoded.squeeze().tolist()


def generate_samples(sequence, length, ohe):
    padded = pad_sequence(sequence, length + 1)  # added 1 for output
    encoded = one_hot_encode(padded, ohe)  # TODO: possible to avoid ohe with tensorflow?

    features = ohe.categories_[0]
    n_features = len(features)
    for i in range(length, len(encoded)):
        # reshape sequence to be 3D
        x = encoded[i-length:i].reshape((1, length, n_features))
        # select output
        y = encoded[i].reshape(1, n_features)

        yield x, y


def generate_all_samples(sequences, length, ohe):
    xs, ys = [], []
    for seq in sequences:
        samples = generate_samples(seq, length, ohe)
        for x, y in samples:
            xs += x[0],
            ys += y[0],
    return array(xs), array(ys)
