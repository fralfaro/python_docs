import numpy as np

def mean_absolute_error(
        targets: np.ndarray, predictions: np.ndarray) -> float:
    """
    Calculate the mean absolute error (MAE) metric.

    Parameters:
        targets (np.ndarray): Real values.
        predictions (np.ndarray): Estimated values.

    Returns:
        float
            The calculated MAE value rounded to four decimal places.
    """
    error = predictions - targets
    return round(np.abs(error).mean(), 4)

