# scripts/audio_output.py

import pygame
import os
import time
import psutil

def get_pygame_sink_input_id():
    pid = os.getpid()
    output_info = os.popen("pactl list sink-inputs").read()
    sink_input_id = None
    for line in output_info.split('\n'):
        if 'Sink Input #' in line:
            sink_input_id = line.split('#')[1].strip()
        elif f'application.process.id = "{pid}"' in line:
            return sink_input_id
    return None


def play_audio(file_path):
    """
    Plays the audio file located at `file_path` and routes it to the Virtual_Sink.
    """
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Pygame error: {e}")
        return

    time.sleep(0.1)

    sink_input_id = get_pygame_sink_input_id()
    if sink_input_id:
        os.system(f"pactl move-sink-input {sink_input_id} Virtual_Sink")
        print(f"Moved sink-input {sink_input_id} to Virtual_Sink.")
    else:
        print("No pygame audio stream found.")

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

