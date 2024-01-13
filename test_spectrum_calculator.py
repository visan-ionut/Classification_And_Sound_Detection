import numpy as np
import matplotlib.pyplot as plt
from mel_filter import create_gabor_filters
from spectrum_calculator import calculate_filter_spectrum
from scipy.io import loadmat

# Parameters
M = 12
size = 1102
data = loadmat('data.mat')
fs = data['fs'][0, 0]

# Create Gabor filters
filters = create_gabor_filters(M, size, fs)

# Separate cosinus and sinus filters
cos_filters = [{'cos': filter_params[0], 'sin': filter_params[1]} for filter_params in filters]
sin_filters = [{'cos': filter_params[1], 'sin': filter_params[0]} for filter_params in filters]

def plot_and_save_spectra(cos_filters, sin_filters, fs):
    freqs = np.fft.fftfreq(size, 1 / fs)
    positive_freqs_mask = freqs >= 0

    # Plot cosinus spectra
    plt.figure(figsize=(10, 6))
    for i, cos_filter in enumerate(cos_filters):
        cos_spectrum, _ = calculate_filter_spectrum(size, 1, 1, cos_filter['cos'], cos_filter['sin'])
        plt.plot(freqs[positive_freqs_mask], cos_spectrum[positive_freqs_mask], label=f'Filter {i + 1} (cos)')

    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.legend()
    plt.title('Filter Spectrum')
    plt.grid(True)
    plt.savefig('Visan_Ionut_341C4_spectru_filtre.png')
    plt.show()

# Plot and save the spectra
plot_and_save_spectra(cos_filters, sin_filters, fs)
