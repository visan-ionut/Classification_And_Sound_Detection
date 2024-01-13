import numpy as np
import scipy.fft

def calculate_filter_spectrum(size, sigma, freq, cos_h, sin_h):
    """
    Calculate the spectrum of a Gabor filter.

    Parameters:
    - size: Size of the filter.
    - sigma: Standard deviation of the Gaussian part of the filter.
    - freq: Frequency of the sinusoidal part of the filter.
    - cos_h: Cosine part of the Gabor filter.
    - sin_h: Sine part of the Gabor filter.

    Returns:
    - cos_spectrum: Magnitude spectrum of the cosine part.
    - sin_spectrum: Magnitude spectrum of the sine part.
    """
    
    # Calculate the Fourier transform of the cosine and sine parts
    cos_spectrum = np.abs(scipy.fft.fft(cos_h))
    sin_spectrum = np.abs(scipy.fft.fft(sin_h))

    return cos_spectrum, sin_spectrum
