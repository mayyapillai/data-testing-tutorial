import string


def increment(x):
    return x + 1


def strip_punctuation(text):
    return ''.join(s for s in text if s not in string.punctuation)


def bag_of_words(text):
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words


def min_max_scaler(x):
    """
    Returns a numpy array with all of the original values scaled between 0 and
    1.

    Assumes the data are a numpy array.
    """
    return (x - x.min()) / (x.max() - x.min())
