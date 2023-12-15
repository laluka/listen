import os
from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_TOKEN"))


def to_speech(text: str):
    speech_file_path = "/dev/stdout"
    response = client.audio.speech.create(
        model="tts-1", voice="onyx", input=text  # alloy
    )
    response.stream_to_file(speech_file_path)
    # return response.read()
