# scripts/tts_processor.py

from TTS.api import TTS

tts_model = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False, gpu=False)

def generate_tts(text, output_file):
    """
    Generates speech from text and saves it to the specified output file.
    """
    tts_model.tts_to_file(text=text, file_path=output_file)
