# * run tests from command line:
#   pytest -x mtool_model_tests.py
# * run tests from python code:
#   import pytest
#   pytest.main(['-x', 'mtool_model_tests.py'])

import string
import pytest

from mtool_model_utils import *


def test_pad_sequence():
    length = 7
    sequence = list(string.ascii_uppercase)

    seq_short = sequence[:4]
    padded_short = pad_sequence(seq_short, length)
    assert len(padded_short) == length

    seq_long = sequence[:10]
    padded_long = pad_sequence(seq_long, length)
    assert len(padded_long) == len(padded_long)


def test_one_hot_encode():
    length = 7
    sequence = list(string.ascii_uppercase)

    seq = sequence[:length]
    encoded = one_hot_encode(seq, seq)

    assert encoded.shape == (length, length)
    assert encoded.sum() == length


def test_one_hot_decode():
    length = 7
    sequence = list(string.ascii_uppercase)

    seq = sequence[:length]
    encoded = one_hot_encode(seq, seq)
    decoded = one_hot_decode(encoded, seq)

    assert decoded == seq


def test_generate_samples():
    length = 7
    sequence = list(string.ascii_uppercase)

    seq_short = sequence[:4]
    samples_short = generate_samples(seq_short, length, sequence)
    X, y = next(samples_short)
    assert X.shape == (1, length, len(sequence))
    assert y.shape == (1, len(sequence))
    with pytest.raises(Exception):
        next(samples_short)

    seq_long = sequence[:10]
    samples_long = generate_samples(seq_long, length, sequence)
    for X, y in samples_long:
        assert X.shape == (1, length, len(sequence))
        assert y.shape == (1, len(sequence))


def test_generate_all_samples():
    length = 1  #7
    sequence = list(string.ascii_uppercase)

    seqs = [sequence[:i] for i in range(length-1, length+3)]
    Xs, ys = generate_all_samples(seqs, length, sequence)

    n_samples = sum(1 if len(seq) <= (length + 1) else len(seq) - length for seq in seqs)
    assert Xs.shape == (n_samples, length, len(sequence))
    assert ys.shape == (n_samples, len(sequence))
