# Python Voice Assistant

An offline-capable Python desktop voice assistant that performs local text-to-speech synthesis, time retrieval, and automated Wikipedia searches via voice commands.

## Features
* **Speech-to-Text Integration:** Powered by Google Speech Recognition API for accuracy.
* **Offline Text-to-Speech:** Uses native OS speech synthesis via `pyttsx3` with configurable speech rates.
* **Intelligent Query Parsing:** Supports inline search commands (e.g., *"search Wikipedia quantum computing"*) or guided prompt-response loops.
* **Ambient Noise Calibration:** Automatic microphone gain adjustment at startup to reduce false triggers in noisy environments.

## Prerequisites & Installation

### System Dependencies
Speech recognition requires system-level audio driver bindings (`PortAudio`).

* **Windows:** No additional system packages required.
* **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt-get install python3-pyaudio portaudio19-dev
