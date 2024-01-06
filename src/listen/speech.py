import os
import tempfile
from pydub import AudioSegment
from openai import OpenAI
from datetime import datetime

import logging

logger = logging.getLogger("listen")

client = OpenAI(api_key=os.environ.get("OPENAI_TOKEN"))


def to_speech(text: str):
    max_length = 4096
    text_chunks = [text[i : i + max_length] for i in range(0, len(text), max_length)]

    with tempfile.TemporaryDirectory() as temp_dir:
        logger.info(f"Storing tmp files at: {temp_dir}")
        audio_files = []

        for i, chunk in enumerate(text_chunks):
            logger.info(f"Processing chunk (TTS) {i+1} of {len(text_chunks)}, chunk size is {len(chunk)}")
            response = client.audio.speech.create(model="tts-1", voice="onyx", input=chunk)
            audio_file_path = os.path.join(temp_dir, f"chunk_{i}.mp3")
            response.stream_to_file(audio_file_path)
            audio_files.append(audio_file_path)

        combined = AudioSegment.empty()
        for file in audio_files:
            segment = AudioSegment.from_mp3(file)
            combined += segment

        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        final_audio_path = f"listen-{current_time}.mp3"
        combined.export(final_audio_path, format="mp3")
        logger.info(f"Find your final audio file at: {final_audio_path}")
        return final_audio_path
