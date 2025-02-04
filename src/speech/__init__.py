import os
import configparser
import azure.cognitiveservices.speech as speechsdk
#from .config import voice, rate, pitch, volume, bitrate# if I didn't import them like this it did not work, and I don't want to use import *

#bitrate = Riff48Khz16BitMonoPcm

SPEECH_KEY, SPEECH_REGION = os.environ["neospeechkey"], "eastus"
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)

def speak(text, volume="+10%", pitch="0%", rate="+5%", voice="en-US-AriaNeural", audio_format="Riff48Khz16BitMonoPcm"):
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
    speech_config.set_speech_synthesis_output_format(
        getattr(speechsdk.SpeechSynthesisOutputFormat, audio_format)
    )
    # Configure audio output to default speaker
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    # Create a speech synthesizer
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
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
