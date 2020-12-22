#basic stats module
__author__ = "Kotachi Liu"
__copyright__ = "Copyright 2020, CSC 593"

__version__ = "1.0.1"
__maintainer__ = "Kotachi Liu"
__email__ = "kotachi@uri.edu"

    """
    Calculates mean and standard deviation of a list of floats
    %- INPUT:
    %-  1) list of floats (xlist)
    %- OUTPUT:
    %-  1) Mean (mu) and Standard Deviation (sigma)
    %- 
    """

import matplotlib.pyplot as plt

def list_stats(xlist):
    N = 0;
    sum = 0;
    delta = 0;
    sum_delta = 0;
    for x in xlist:
        N = N + 1;
        sum = sum + x;
    mu = sum / N;
    for x in xlist:
        delta = (x - mu) ** 2
        sum_delta = sum_delta + delta
    sigma = (sum_delta / (N - 1)) ** 0.5
    print('Mean:', mu);
    print('Standard Deviation:', sigma);
    plt.hist(xlist);
    return