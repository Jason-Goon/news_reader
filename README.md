# Live AI News Streamer

## Project Overview

This project aims to create a live AI streamer that continuously broadcasts summarized news content using text-to-speech (TTS) technology and streams it through OBS Studio with an animated character as a visual representation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Workflow](#workflow)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- **Content Aggregation**: Fetches news articles from RSS feeds and summarizes them.
- **Text-to-Speech Conversion**: Converts summarized text into speech using TTS.
- **Audio Playback**: Plays the generated audio through a virtual audio sink compatible with OBS.
- **Modular Design**: Easily extendable for future features like chat interaction and donation reading.

markdown


## Installation

### Prerequisites

- **Operating System**: Gentoo Linux
- **Python**: Version 3.10
- **OBS Studio**: For streaming and audio capture
- **Virtual Audio Cable**: Configured using PulseAudio's `module-null-sink`

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/live-ai-news-streamer.git
   cd live-ai-news-streamer

    Set Up Virtual Environment

    bash

python3.10 -m venv venv
source venv/bin/activate

Install Dependencies

bash

pip install --upgrade pip
pip install -r requirements.txt

Configure OBS Studio

    Set up a new scene with an audio input capturing the virtual audio sink (e.g., Virtual_Sink).
    Add visual elements like a static image or video for the background.
    Configure audio monitoring if needed.

Set Up Virtual Audio Sink

Load the virtual audio sink using PulseAudio:

bash

pactl load-module module-null-sink sink_name=Virtual_Sink sink_properties=device.description=Virtual_Sink

To make it persistent, add the following line to your ~/.config/pulse/default.pa:

bash

    load-module module-null-sink sink_name=Virtual_Sink sink_properties=device.description=Virtual_Sink

Usage

    Activate Virtual Environment

    bash

source venv/bin/activate

Run the Application

bash

    python main.py

    Start Streaming in OBS
        Open OBS Studio.
        Ensure the audio levels are active, indicating that the audio is being captured.
        Start streaming or recording as needed.

Workflow

    Content Aggregation
        The application fetches news articles from predefined RSS feeds.
        Articles are summarized to extract key information.

    Text Processing
        Summarized text is split into manageable chunks for processing.

    Text-to-Speech Conversion
        Each text chunk is converted into speech using the TTS engine.

    Audio Playback
        The generated audio files are played through the virtual audio sink.
        OBS Studio captures this audio for streaming.

    Parallel Processing
        While one chunk is being played, the next chunk is being processed.
        This ensures a continuous flow of content.

Testing

    Run Test Suite

    bash

    python -m unittest discover -s tests

    Test Coverage
        Tests cover content aggregation, text summarization, TTS processing, and audio playback.
        Mocking is used to simulate external dependencies and avoid side effects.

Dependencies

    Python Packages
        requests: For HTTP requests to fetch news content.
        beautifulsoup4: For parsing XML from RSS feeds.
        pygame: For audio playback.
        TTS: For text-to-speech conversion.
        unittest: For testing.
        unittest.mock: For mocking in tests.

    System Requirements
        PulseAudio: For managing audio sinks.
        OBS Studio: For capturing and streaming audio/video.

Future Enhancements

    Animated Character Integration: Implement a visual representation using tools like Live2D or Unity.
    Chat Interaction: Incorporate chat message reading and interactions.
    Advanced Summarization: Use more sophisticated NLP models for better summaries.
    Error Handling: Improve robustness with enhanced error handling and logging.

License

This project is licensed under the MIT License - see the LICENSE file for details.