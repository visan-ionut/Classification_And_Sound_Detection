import numpy as np

def gaussian_filter(size, sigma):
    """
    Generate a 1D Gaussian filter.

    Parameters:
    - size: Size of the filter.
    - sigma: Standard deviation of the Gaussian.

    Returns:
    1D array representing the Gaussian filter.
    """
    
    # Calculate the mean
    miu = size / 2
    
    # Calculate the power of e in the exponent
    exponent = np.exp(-((np.arange(1, size + 1) - miu) ** 2) / (2 * sigma ** 2))
    
    # Calculate the final Gaussian filter formula
    gauss_filt = (1 / (sigma * np.sqrt(2 * np.pi))) * exponent
    
    return gauss_filt
