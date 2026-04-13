import scipy.io.wavfile as wav
import numpy as np

NSECS = 3
SAMPLE_RATE = 48_000
NSAMPLES = NSECS * SAMPLE_RATE

# frequency in Hz
F = 440

# create a numpy array where each index is a moment in time (indivual sample)
t = np.linspace(0, NSECS, num=NSAMPLES, endpoint=False)

# create for each sample time (sin * position)
f = np.sin(2 * np.pi * F * t) * t / NSECS

wav.write('./sine.wav', SAMPLE_RATE, f)






