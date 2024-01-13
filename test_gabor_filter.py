import numpy as np
import matplotlib.pyplot as plt
from gabor_filter import gabor_filter

def main():
    # Set parameters
    size = 1102
    sigma = 187.21221
    freq = 0.00267

    # Get Gabor filters
    cos_filter, sin_filter = gabor_filter(size, sigma, freq)

    # Plot and save the filters
    plt.plot(cos_filter, label='Cosine Filter')
    plt.title('Gabor Cosine Filter')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.savefig('Visan_Ionut_341C4_gabor_cos.png')
    plt.show()

    plt.plot(sin_filter, label='Sine Filter')
    plt.title('Gabor Sine Filter')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.savefig('Visan_Ionut_341C4_gabor_sin.png')
    plt.show()

if __name__ == "__main__":
    main()
