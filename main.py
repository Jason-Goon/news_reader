# main.py

import queue
import threading
import time
import os
import logging
from collections import deque
from scripts.content_aggregator import fetch_news
from scripts.tts_processor import generate_tts
from scripts.audio_output import play_audio
from scripts.utils import chunk_text, clean_text
import pygame 

# audio dir 
if not os.path.exists('audio'):
    os.makedirs('audio')

# queues init 
text_queue = queue.Queue()
audio_queue = queue.Queue(maxsize=1)

def content_aggregator():
    processed_items = deque(maxlen=10)
    while True:
        news_items = fetch_news()
        new_items_found = False

        for guid, summary in news_items:
            if guid not in processed_items:
                processed_items.append(guid)
                new_items_found = True
                chunks = chunk_text(summary)
                for chunk in chunks:
                    text_queue.put(chunk)
            else:
                print(f"Already processed item: {guid}")

        if not new_items_found:
            print("No new content fetched.")
            time.sleep(10)
        else:
            time.sleep(1)

def tts_worker():
    while True:
        chunk = text_queue.get()
        try:
            cleaned_chunk = clean_text(chunk)
            logging.info(f"TTS Worker: Processing chunk: {cleaned_chunk[:30]}...")
            output_file = f"audio/{int(time.time())}.wav"
            generate_tts(cleaned_chunk, output_file)
            audio_queue.put(output_file)  # This should block if the queue is full
        except Exception as e:
            logging.error(f"Error in tts_worker: {e}")
        finally:
            text_queue.task_done()

if __name__ == "__main__":
    pygame.mixer.init()
    threading.Thread(target=content_aggregator, daemon=True).start()
    threading.Thread(target=tts_worker, daemon=True).start()
    try:
        while True:
            audio_file = audio_queue.get()
            try:
                print(f"Audio Player: Playing file {audio_file}")
                play_audio(audio_file)
                os.remove(audio_file)
            except Exception as e:
                print(f"Error in main audio player: {e}")
            finally:
                audio_queue.task_done()
    except KeyboardInterrupt:
        print("Shutting down...")
