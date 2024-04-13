def median(a):
    """
    Calculates the median value from a list of numbers
    """
    if type(a) == list:
        a.sort()
        if len(a)%2 == 0:
            l=len(a)//2
            median = a[l-1]

        else:
            l=len(a)//2
            median = (a[l-1]+a[l])/2
    else:
        raise ValueError("Input must be a list!")
    return median
