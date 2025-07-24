
import os
import configparser
import azure.cognitiveservices.speech as speechsdk
try:
    from auth import get_api_key
except ImportError:
    def get_api_key(name):
        return None

#bitrate = Riff48Khz16BitMonoPcm


# Delay key check until speech is actually needed
SPEECH_REGION = "eastus"
speech_config = None

def get_speech_config():
    global speech_config
    if speech_config is not None:
        return speech_config
    key = get_api_key("neospeechkey") or os.environ.get("neospeechkey")
    if not key:
        raise RuntimeError("No Azure Speech key found. Please set it in ~/.neocasa_auth.json or as the 'neospeechkey' environment variable.")
    speech_config = speechsdk.SpeechConfig(subscription=key, region=SPEECH_REGION)
    return speech_config

def speak(text, volume="+10%", pitch="0%", rate="+5%", voice="en-US-NancyNeural", audio_format="Riff48Khz16BitMonoPcm"):
    # Generate SSML with dynamic parameters
    ssml = f"""
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
        <voice name="{voice}">
            <prosody rate="{rate}" pitch="{pitch}" volume="{volume}">
                {text}
            </prosody>
        </voice>
    </speak>
    """
    config = get_speech_config()
    config.set_speech_synthesis_output_format(
        getattr(speechsdk.SpeechSynthesisOutputFormat, audio_format)
    )
    # Configure audio output to default speaker
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    # Create a speech synthesizer
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_config)
    # Synthesize speech using SSML
    try:
        result = speech_synthesizer.speak_ssml_async(ssml).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Speech synthesized successfully: {text}")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
    except Exception as e:
        print(f"An error occurred: {e}")
