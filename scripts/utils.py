# scripts/utils.py
import unicodedata
import re

def chunk_text(text, max_length=200):
    """
    Splits the text into chunks of maximum `max_length` characters.
    """
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 <= max_length:
            current_chunk += " " + word if current_chunk else word
        else:
            chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def clean_text(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    text = text.replace('%', ' percent')
    text = re.sub(r'[^a-zA-Z0-9\s\.,;:\'\"?!-]', '', text)

    return text
