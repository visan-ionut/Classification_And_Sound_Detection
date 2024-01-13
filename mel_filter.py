import numpy as np
from gabor_filter import gabor_filter

def to_mel(f):
    """Convert frequency to Mel scale."""
    return 1127 * np.log(1 + f / 700)

def from_mel(f_mel):
    """Convert Mel scale to frequency."""
    return 700 * ((np.exp(f_mel / 1127)) - 1)

def create_gabor_filters(M, size, fs):
    """Create Gabor filters based on Mel scale parameters."""
    
    # Frequencies A and B on the Mel scale
    f_A_mel = to_mel(0)
    f_B_mel = to_mel(fs / 2)

    # Generate Mel scale frequencies and lengths
    mel_frequencies = np.linspace(f_A_mel, f_B_mel, M + 1)
    normal_frequencies = from_mel(mel_frequencies)

    # Calculate centers c_i and lengths l_i on the normal scale
    centers_normal = (normal_frequencies[:-1] + normal_frequencies[1:]) / 2
    lengths_normal = np.diff(normal_frequencies)

    filters = []
    # Calculate fi = ci/fS and sigma_i = fS/li for all segments
    for i in range(M):
        fi_segment = centers_normal[i] / fs
        sigma_segment = fs / lengths_normal[i]

        # Create Gabor filter with the specified parameters
        filter_i = gabor_filter(size, sigma_segment, fi_segment)
        filters.append(filter_i)

    return np.array(filters)
