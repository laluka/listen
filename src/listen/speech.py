import os
from openai import OpenAI


client = OpenAI(api_key=os.environ.get('OPENAI_TOKEN'))


def to_speech(text: str):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    return response.read()
