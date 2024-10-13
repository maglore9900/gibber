# gibber

A simple Speech-to-Text (STT) / Text-to-Speech (TTS) wrapper for LLMs.
Currently it supports OpenAI and Ollama for local LLM models.

With minor modification it could support other closed source models. The LLM functions are defined in [modules/adapter.py](modules/adapter.py) 

# INSTALLATION

so basically the steps are pretty simple

1. download the code (clone it or download it and unzip it)
2. install **python 3.10** on the system (seriously this version)
3. create a virtual environment using `python -m venv .` in the folder/dir of the code
4. activate the environment with `Scripts\activate.bat` on windows or `source bin/activate` on linux
5. run pip install to install all the required modules `pip install -r requirements.txt`
   | Note: Gibber leverages your local hardware and on linux that can mean you need to download packages / drivers to get this to work.
   | Example: on ubuntu you will need to run `sudo apt install portaudio19-dev` the additional packages are going to vary based on the distribution. Easiest way to resolve will be to google the error codes you see. Once you have taken the necessary action, run `pip install -r requirements.txt` again.
6. then `cp example_env.txt to .env`
7. open the new `.env` file, and put in your info, like openai key or ollama model, or whatever
8. If you are using an Nvidia GPU and dont already have the CUDA toolkit and such, see note below
9. then run `python main.py` to start the whole thing up

> Note: If you are using faster-whisper and have an nvidia GPU you will need to download the cuda tool kit and cudann to leverage your GPU.
>
> Instructions are [Here](docs/cuda.md)
>
> If this seems too complicated you can just leave it at its default, which will use google for speech-to-text
>
> Note: On linux systems you may see Alsa warnings/errors. Right now they do not affect performance and can generally be ignored.

# Configuration

All of the easy configuration is done in the .env file. This section will explain what the values do, although you will also find it in the [example_env.txt](example_env.txt)

#LLM_TYPE will take openai, local. Local will use Ollama
`LLM_TYPE = 'openai'`

#-----OpenAI variables
`OPENAI_API_KEY = ''`
`OPENAI_MODEL = 'gpt-4o-mini'`

#-----Ollama variables
#OLLAMA_MODEL will take any model you can load in ollama
`OLLAMA_MODEL = 'gemma2'`
`OLLAMA_URL = 'http://localhost:11434'`

#-----Customization Variables
#CHARACTER will take any character prompt you have in the [prompts/prompts.py](prompts/prompts.py) file.

`CHARACTER = 'bob'`

#WAKE_WORD_ENABLED: If you want this to listen and attempt to translate all text you can disable wake word. However, speech to text transcription can sometimes return incorrect results when there is background noise. Set to false to disable wake word. When enabled the wake phrase will be wake word + character name, for example "hey bob"
`WAKE_WORD_ENABLED = 'True'`

`WAKE_WORD = 'hey'`

#LISTEN_MODEL will take whisper or google, whisper is the best option but requires additional setup with Nvidia drivers

`LISTEN_MODEL='google'`

#If you are using whisper and you have an nvidia GPU, AND you have followed the additional installation steps to get the CUDA drivers, then set the following to True to use the Nvidia card
`WHISPER_NVIDIA = 'False'`

#TIME_SILENCE is how long the silence needs to be (in seconds) after voice, for it to stop listening and transcribe. This speeds up the process, sending messages, and adjusting for noise.
`TIME_SILENCE = '2'`

#SPEECH_ENABLED is used to stream the audio to a service that will convert the text to speech. If you dont want to use this feature set to false, the response will be printed to the console.
`SPEECH_ENABLED = 'True'`

#STREAM SPEAK URL is using the default url for Alltalk. If you dont have all talk you can ignore this, if you want to use a different service, simply replace the url. Even without Alltalk this can respond in a robotic voice.

`STREAM_SPEAK_URL = 'http://127.0.0.1:7851/api/tts-generate'`
