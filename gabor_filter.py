import numpy as np
from gaussian_filter import gaussian_filter

def gabor_filter(size, sigma, freq):
    """
    Generate Gabor filter with given parameters.

    Parameters:
    - size: Size of the filter.
    - sigma: Standard deviation of the Gaussian envelope.
    - freq: Frequency of the sinusoidal carrier.

    Returns:
    Tuple containing the Gabor filter components (cosine and sine).
    """
    
    # Generate the Gaussian envelope
    gauss_filt = gaussian_filter(size, sigma)
    
    # Generate the Gabor filter components
    cos_h = gauss_filt * np.cos(2 * np.pi * freq * np.arange(1, size + 1))
    sin_h = gauss_filt * np.sin(2 * np.pi * freq * np.arange(1, size + 1))
    
    return cos_h, sin_h
