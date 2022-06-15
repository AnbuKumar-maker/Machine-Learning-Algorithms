#CodingScientist Anbu Kumar
#Data Transformation

from statistics import mean, stdev


def normalization(data: list, ndigits: int = 3) -> list:
    """
    Returns a normalized list of values
    @params: data, a list of values to normalize
    @returns: a list of normalized values (rounded to ndigits decimal places)
    @examples:
    >>> normalization([2, 7, 10, 20, 30, 50])
    [0.0, 0.104, 0.167, 0.375, 0.583, 1.0]
    >>> normalization([5, 10, 15, 20, 25])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # variables for calculation
    x_min = min(data)
    x_max = max(data)
    # normalize data
    return [round((x - x_min) / (x_max - x_min), ndigits) for x in data]


def standardization(data: list, ndigits: int = 3) -> list:
    """
    Returns a standardized list of values
    @params: data, a list of values to standardize
    @returns: a list of standardized values (rounded to ndigits decimal places)
    @examples:
    >>> standardization([2, 7, 10, 20, 30, 50])
    [-0.999, -0.719, -0.551, 0.009, 0.57, 1.69]
    >>> standardization([5, 10, 15, 20, 25])
    [-1.265, -0.632, 0.0, 0.632, 1.265]
    """
    # variables for calculation
    mu = mean(data)
    sigma = stdev(data)
    # standardize data
    return [round((x - mu) / (sigma), ndigits) for x in data]