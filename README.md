Minor-Stego
===========

This python code implements the paper "A Robust Audio Steganographic Technique based on Phase Shifting and Psycho–acoustic Persistence of Human Hearing Ability" published in International Journal of Computing and Corporate Research (IJCCR), India.

The program hides the target audio file into the cover audio file employing the property of psycho-acoustic persistence of human hearing, which states that the sound heard at any point of time by the human ear persists in the human ear(drums) for upto one-tenth of a second, much like in case motion pictures. The target audio file is hidden sample by sample in the one-tenth synapse created through phase shifting of the cover audio file.

Technologies used:

	Python 2.7.5
	libsndfile 1.0.25
	libsndfile-devel 1.0.25
	numpy 1.8.2
	python-scikit-learn 0.14.1
	ffmpeg 2.1.5
	ffmpeg-devel 2.1.5

Recommendation:

	To run this code, please install the necessary programs (as listed above) in a Linux based system.


The program can take as input almost any valid audiofile. The output is always an uncompressed, monophonic WAV file, with the sampling frequency as specified in the program.
