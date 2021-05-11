from math import log2

def entropy(container):
    total = sum(container)
    return -sum((x/total)*log2(x/total) for x in container if x != 0)

def without(l, to_be_removed):
    result = list(l)
    result.remove(to_be_removed)
    return result

def print_predictions(predictions):
    print('[PREDICTIONS]:', end=' ')
    for x in predictions:
        print(x, end=' ')
    print()