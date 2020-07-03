import numpy as np


class data_scientist:
    """
    Endows data with meaning.

    Attributes
    ----------
    data : float
        input data
    """

    def __init__(self):
        self.data = None

    def shift_enter(self, data: np.ndarray) -> str:
        self.data = data
        return "cutting-edge data science"
