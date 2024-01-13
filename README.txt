==================================
Classification and sound detection
==================================

The PDF file "pdf-statement_topic2023" contains the exact project
requirements (in romanian).

In this topic, we will explore some operations
for the analysis of signals, especially for analyzing
audio signals. We will see how we can use sound filtering
to distinguish different sounds.
Implementing a Gabor filter and a set of Gabor filters to
characterize the spectrum of sounds. The project also includes
the steps of creating analysis windows, filtering them using
Gabor filters, and extracting features for classification.
The ultimate goal is to implement a simple classifier for
different types of sounds and evaluate its performance.

Implementation of Gabor Filter
The "gaussian_filter" function:
This function generates a one-dimensional Gaussian filter of a
specified size and standard deviation. It calculates filter values
using the Gaussian probability density formula, where the mean is
set to half the filter size. The resulting filter represents a bell-shaped
curve used in various signal processing applications.
I implemented in the file "gabor_filter.py":
The "gabor_filter" function:
The gabor_filter function generates a Gabor filter by combining a Gaussian
filter and a sinusoidal wave. The resulting filter is returned as a tuple
containing components for the cosine and sine parts. This type of filter is
used in signal processing for texture and contour detection.

Create a set of filters
I implemented in the file "mel_filter.py":
The "to_mel" function:
The to_mel function converts a given frequency to the Mel scale using the
formula Mel = 1127 * log(1 + f / 700).
The "from_mel" function:
The from_mel function performs the inverse conversion, transforming a value from
the Mel scale back to the corresponding frequency.
The "create_gabor_filters" function:
Generates Gabor filters based on parameters on the Mel scale, using the previously
defined functions (to_mel, from_mel, gabor_filter). It divides the Mel interval into
M segments, calculates frequencies and lengths corresponding to the normal scale, and
then creates Gabor filters for each segment. The result is a list of Gabor filters, where
each filter is a pair of cosine and sine components.

Display the spectrum of filters
I implemented in the file "spectrum_calculator.py":
The "calculate_filter_spectrum" function:
Calculates the filter spectrum by performing the Fourier transform of the cosine and sine parts,
and the result consists of the magnitude of these spectra.

Create Windows
I implemented in the file "create_windows.py":
The "create_windows" function:
The create_windows function takes an audio signal, a sampling frequency, a filter size, and an overlap
percentage. It converts 12ms to samples, calculates the number of samples with which windows overlap,
and then createsand returns a matrix of overlapping windows from the given audio signal.

For testing the following requirements:
Save the cos and sin type filters using the parameters corresponding to the first segment
(fi = 0.00267, σ1 = 187.21221) using the names id_gabor_cos.png and id_gabor_sin.png.
Save a figure (id_filter_spectrum.png) with the magnitude of the spectrum corresponding to positive
frequencies, located in the first half of the response given by the fft function.

I used the files:
test_gabor_filter.py, from which the following were saved:
gabor_cos.png
gabor_sin.png
test_spectrum_calculator.py, from which the following was saved:
filter_spectrum.png
