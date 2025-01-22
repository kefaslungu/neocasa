import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY, SPEECH_REGION = os.environ["neospeechkey"], "eastus"
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)

def speak(text):
    # Configure audio output to the default speaker
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    # Configure the speech synthesis voice
    speech_config.speech_synthesis_voice_name = 'en-US-AriaNeural'
    
    # Create a speech synthesizer
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Synthesize the given text to speech
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    
    # Check the result and provide feedback
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized for text: {text}")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print(f"Error details: {cancellation_details.error_details}")
                print("Did you set the speech resource key and region values?")
