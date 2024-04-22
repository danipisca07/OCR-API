def divide_until_below(value, belowThreshold = 100, divideBy = 10):
    if(value < belowThreshold):
        return value

    return divide_until_below(value/divideBy, belowThreshold, divideBy)