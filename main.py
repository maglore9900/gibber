from modules import adapter, speak_modified as speak
from prompts import prompts
import environ
import os

env = environ.Env()
environ.Env.read_env()


spk = speak.Speak(env)
ad = adapter.Adapter(env)
char = env("CHARACTER").lower()
char_prompt = getattr(prompts, char, "You are a helpful assistant.") + "\nAnswer the following request: {query}"

while True:
    text = spk.transcribe()
    if env("WAKE_WORD_ENABLED").lower() == "true":
        if text and env("WAKE_WORD").lower() in text.lower() and env("CHARACTER").lower() in text.lower():
            if "exit" in text.lower():
                break
            response = ad.llm_chat.invoke(char_prompt.format(query=text))
            if response:
                print(response.content)
                if env("SPEECH_ENABLED").lower() == "true":
                    spk.stream(response.content)
    else:
        if "exit" in text.lower():
            break
        response = ad.llm_chat.invoke(char_prompt.format(query=text))
        if response:
            print(response.content)
            if env("SPEECH_ENABLED").lower() == "true":
                spk.stream(response.content)
        
