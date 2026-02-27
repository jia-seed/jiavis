# jiavis

![python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![platform](https://img.shields.io/badge/platform-windows-lightgrey?style=flat-square&logo=windows&logoColor=white)
![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![ai](https://img.shields.io/badge/ai-100%25%20local-purple?style=flat-square)

a local voice assistant that runs entirely on your machine. no cloud, no api keys, no subscriptions. just talk to your computer.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c08ac125-4ecc-4a54-8e60-d1c405178de0" width="400" />
</p>

## how it works
```
you speak → mic captures → whisper transcribes → phi-2 thinks → speaker responds
```

## requirements

- windows 10/11
- python 3.8+
- microphone (tested with samson q2u)
- speaker (tested with jbl clip 5, yeah just what i had laying around)
- [lm studio](https://lmstudio.ai/)
- in my case my intel asus nuc 14 rvk

<p align="center">
  <img src="https://github.com/user-attachments/assets/1b357f9b-7463-47ac-8a65-abb73ff8f21b" width="400" />
</p>

## setup

1. install dependencies
```bash
pip install sounddevice numpy openai-whisper requests
```

2. download a model in lm studio

<p align="center">
  <img src="https://github.com/user-attachments/assets/9cba486c-d47c-4e89-a534-8546865545e2" width="500" />
</p>

- open lm studio
- search for `TheBloke/phi-2-GGUF`
- download the `Q4_K_M` version

3. start the local server

- go to the developer tab in lm studio
- load the phi-2 model
- toggle the server on (runs on localhost:1234)

4. run jiavis
```bash
python jiavis.py
```

5. speak after you see "listening..."

## architecture
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  mic         │ ──▶ │     your pc  │ ──▶ │  speaker     │
│  (input)     │     │  (local ai)  │     │  (output)    │
└──────────────┘     └──────────────┘     └──────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
   ┌────────────┐    ┌────────────┐    ┌────────────┐
   │  whisper   │    │  lm studio │    │  windows   │
   │  (stt)     │    │  + phi-2   │    │  tts       │
   └────────────┘    └────────────┘    └────────────┘
```

## customization

edit the system prompt in `jiavis.py` to change the personality:
```python
{"role": "system", "content": "you are jiavis, a helpful voice assistant..."}
```

## why local?

- **privacy**: your voice never leaves your machine
- **free**: no api costs or subscriptions
- **fast**: no network latency
- **offline**: works without internet

## credits

built with [whisper](https://github.com/openai/whisper), [lm studio](https://lmstudio.ai/), and vibes
