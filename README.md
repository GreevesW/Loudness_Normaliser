# Loudness_Normaliser

A proof of concept used to show how audio mastering pipelines can be used to make audio post production more efficient and scalable.

## Overview

This project automatically masters input audio by first normalising to a preset LUFS level before compressing it.

A version of the model using TTS is also included, but commented out.

## File Structure

```
.
├── mastering_pipeline.py
├── recordings
├── README.md
└── .gitignore
```

## Instalation

   ```bash
   pip install pyttsx3
   pip install pydub
   pip install pyloudnorm
   pip install soundfile
   pip install numpy
   pip install matplotlib
   ```

## Dependencies

ffmpeg

## Usage

Place audio recording in recordings folder. Rename the input to my_recording.wav

   ```bash
   python mastering_pipeline.py
   ```

## Outputs

input.wav
normalized.wav
mastered_output.wav

matplotlib plot showing waveform of the input, normalised and mastered audio
