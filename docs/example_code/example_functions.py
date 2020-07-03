import random


def fibonnaci(n: int) -> int:
    """Returns mean of a 2d array along 0 axis

    Parameters
    ----------
    x : np.ndarray
        2 dimensional array

    Returns
    -------
    float
        mean along 0 axis
    """
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def monte_carlo_estimate_pi(nr_samples: int) -> float:
    """
    Monte Carlo estimate of pi.

    Parameters
    ----------
    nr_samples : int
        Number of samples

    Returns
    -------
    float
        Estimate of pi
    """
    pi_est = 0
    area_circle = 0
    area_square = 1
    for z in range(0, nr_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        in_circle = x ** 2 + y ** 2 <= 1
        if in_circle:
            area_circle += 1
        area_square += 1
        pi_est = 4 * (area_circle / area_square)
    return pi_est
