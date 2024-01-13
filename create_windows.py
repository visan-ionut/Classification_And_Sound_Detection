# File: window_creator.py

import numpy as np

def create_windows(audio, fs, filter_size, overlap_percent):
    """
    Create overlapping windows for the given audio.

    Parameters:
    - audio: 1D array containing audio samples.
    - fs: Sampling frequency.
    - filter_size: Size of the filter used for feature extraction.
    - overlap_percent: Percentage of overlap between consecutive windows.

    Returns:
    - windows: 2D array containing audio windows.
    """
    
    # Convert 12ms to samples
    window_size_samples = int((12 / 1000) * fs)

    # Calculate overlap in samples
    overlap_samples = int(window_size_samples * overlap_percent / 100)

    # Calculate the number of windows
    num_windows = int(np.floor((len(audio) - filter_size) / (filter_size - overlap_samples))) + 1

    # Initialize array to store windows
    windows = np.zeros((num_windows, filter_size))

    # Create overlapping windows
    for i in range(num_windows):
        start_idx = i * (filter_size - overlap_samples)
        end_idx = start_idx + filter_size
        windows[i, :] = audio[start_idx:end_idx]

    return windows
