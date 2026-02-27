# Jiavis - Local AI Voice Assistant | 100% Offline & Privacy-First

![python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![platform](https://img.shields.io/badge/platform-windows-lightgrey?style=flat-square&logo=windows&logoColor=white)
![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![ai](https://img.shields.io/badge/ai-100%25%20local-purple?style=flat-square)

**Jiavis** is a simple, powerful local voice assistant that runs entirely on your machine 24/7 with no cloud dependencies, API keys, or subscriptions. Built for privacy-focused users who want full control over their AI assistant without compromising their data security.

(for me i ran phi-2 on lmstudio with a speaker microphone using whisper and python on an intel asus nuc 14 rvk)

<p align="center">
  <img src="https://github.com/user-attachments/assets/c08ac125-4ecc-4a54-8e60-d1c405178de0" width="400" />
</p>

## How Jiavis Voice Assistant Works

Jiavis uses a simple but powerful workflow for natural voice interaction:

```
you speak → mic captures → whisper transcribes → phi-2 thinks → speaker responds
```

The entire process happens locally on your machine, ensuring your conversations remain private and secure. No data is ever sent to external servers or cloud services.

## System Requirements for Local AI Assistant

### Hardware Requirements
- **Operating System**: Windows 10/11
- **Python Version**: Python 3.8 or higher
- **Microphone**: Any USB or built-in microphone (tested with Samson Q2U)
- **Speaker**: Any speaker or headphones (tested with JBL Clip 5)
- **Computer**: Mid-range PC or mini PC (tested on Intel ASUS NUC 14 RVK)

### Software Dependencies
- **LM Studio**: Download from [lmstudio.ai](https://lmstudio.ai/) for local AI model management
- **Python Libraries**: sounddevice, numpy, openai-whisper, requests (automatically installed)

<p align="center">
  <img src="https://github.com/user-attachments/assets/1b357f9b-7463-47ac-8a65-abb73ff8f21b" width="400" />
</p>

## Complete Setup Guide

### Step 1: Install Python Dependencies

First, install the required Python packages for the voice assistant:

```bash
pip install sounddevice numpy openai-whisper requests
```

### Step 2: Download Local AI Model

<p align="center">
  <img src="https://github.com/user-attachments/assets/9cba486c-d47c-4e89-a534-8546865545e2" width="500" />
</p>

- open lm studio
- search for `TheBloke/phi-2-GGUF`
- download the `Q4_K_M` version

### Step 3: Start Local AI Server

Configure LM Studio to run your local AI model:

1. **Open LM Studio** application
2. **Navigate to Developer tab** in the interface
3. **Load the Phi-2 model** you downloaded
4. **Toggle server ON** (will run on localhost:1234)

### Step 4: Launch Jiavis Assistant

Start your local voice assistant:

```bash
python jiavis.py
```

### Step 5: Start Voice Interaction

Begin speaking after you see the "listening..." prompt in your terminal. Your voice assistant is now ready for 24/7 offline operation!

## Technical Architecture

The Jiavis voice assistant uses a modular architecture with three main components working together locally:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  microphone  │ ──▶ │   your pc    │ ──▶ │   speaker    │
│   (input)    │     │  (local ai)  │     │  (output)    │
└──────────────┘     └──────────────┘     └──────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
   ┌────────────┐    ┌────────────┐    ┌────────────┐
   │  Whisper   │    │ LM Studio  │    │  Windows   │
   │   (STT)    │    │  + Phi-2   │    │    TTS     │
   └────────────┘    └────────────┘    └────────────┘
```

### Component Details
- **Whisper**: OpenAI's speech-to-text model for voice recognition
- **LM Studio + Phi-2**: Local language model for natural language processing
- **Windows TTS**: Built-in text-to-speech for audio responses

## Customizing Your Voice Assistant

### Personality Customization

You can easily customize Jiavis's personality by editing the system prompt in `jiavis.py`. Locate this section and modify the content:

```python
{"role": "system", "content": "you are jiavis, a helpful voice assistant..."}
```

### Advanced Configuration Options

- **Response Length**: Modify `max_tokens` parameter to control response length
- **Voice Style**: Adjust `temperature` setting for more creative or conservative responses
- **Recording Duration**: Change `RECORD_SECONDS` to capture longer voice inputs
- **Microphone Device**: Update `MIC_DEVICE` to use different audio input devices

## Why Choose a Local Voice Assistant?

### Privacy-First Design
- **Complete Privacy**: Your voice data never leaves your machine
- **No Data Mining**: No corporate surveillance or data collection
- **Secure Communication**: All processing happens locally on your device

### Cost-Effective Solution
- **Zero Subscription Fees**: No monthly or annual costs
- **No API Limits**: Unlimited usage without rate limiting
- **One-Time Setup**: Install once, use forever

### Performance Benefits
- **Lightning Fast**: No network latency or internet delays
- **Always Available**: Works completely offline
- **Reliable Connection**: No dependence on external servers or internet connectivity

### Full Control
- **Open Source**: Modify and customize as needed
- **Local Storage**: All conversation history stays on your machine
- **Independence**: No vendor lock-in or service discontinuation risks

## Troubleshooting Common Issues

### Audio Device Problems
If you encounter microphone issues, check your device index by running:
```python
import sounddevice as sd
print(sd.query_devices())
```

### Model Loading Issues
Ensure LM Studio is running and the Phi-2 model is properly loaded before starting Jiavis.

### Performance Optimization
For better performance on slower machines, consider using the smaller Whisper model or adjusting the recording duration.

## Credits and Acknowledgments

This local voice assistant is built with these excellent open-source technologies:
- **[OpenAI Whisper](https://github.com/openai/whisper)**: Advanced speech-to-text capabilities
- **[LM Studio](https://lmstudio.ai/)**: User-friendly local AI model management
- **[Phi-2 Model](https://huggingface.co/microsoft/phi-2)**: Microsoft's efficient language model

## Contributing to Jiavis

We welcome contributions to improve this local voice assistant! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Share your customizations

---

**Ready to take control of your AI assistant?** Start building your privacy-focused, offline voice assistant today!
