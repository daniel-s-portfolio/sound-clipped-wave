import scipy.io.wavfile as wav
import numpy as np
import sounddevice as sd

# Constants for sine wave specs
DURATION = 1
SAMPLE_RATE = 48000
FREQ = 440

def main():
    sine_wave(FREQ, DURATION, SAMPLE_RATE, amplitude=8192) # 1/4 max amplitude
    clipped_wave(FREQ, DURATION, SAMPLE_RATE, amplitude=16384) # 1/2 max amplitude


def sine_wave(freq, duration, sample_rate, amplitude):
    """
    Generates a sine wave of a given frequency and duration, then saves it
    as sine.wav in the current directory.
    """
    # create a numpy array where each index is a moment in time (indivual sample times)
    t = np.linspace(0, duration, num=int(duration * sample_rate), endpoint=False)

    # sample sine wave at each sample time 
    samples = amplitude * np.sin(2 * np.pi * freq * t)

    # convert to 16-bit integer format, write to .wav file
    samples_16bit = samples.astype(np.int16) 
    wav.write('sine.wav', sample_rate, samples_16bit)


def clipped_wave(freq, duration, sample_rate, amplitude):
    """
    Generates a clipped sine wave of a given frequency and duration, then saves it
    as clipped.wav in the current directory and plays the clipped wave audio.
    """
    # create a numpy array where each index is a moment in time (indivual sample times)
    t = np.linspace(0, duration, num=int(duration * sample_rate), endpoint=False)

    # sample sine wave at each sample time 
    samples = amplitude * np.sin(2 * np.pi * freq * t)

    # clip wave to 1/4 max amplitude, convert to 16-bit integer format, write to .wav file
    samples_clipped = np.clip(samples, -8192, 8192)
    samples_16bit = samples_clipped.astype(np.int16)
    wav.write('clipped.wav', sample_rate, samples_16bit)

    # play the clipped wave
    sd.play(samples_16bit, sample_rate)
    sd.wait()


if __name__ == "__main__":
    main()