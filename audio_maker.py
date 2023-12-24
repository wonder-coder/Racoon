import elevenlabs

elevenlabs.set_api_key("################")

voice = elevenlabs.Voice(
        voice_id="5fYjT7EchpKNVeNxTpKL",
        settings=elevenlabs.VoiceSettings(
            stability=0.5,
            similarity_boost=0.75
        )
    )

def generate_speech(text, aud):
    audio = elevenlabs.generate(
        text=text,
        voice=voice,
        
    )
    elevenlabs.save(audio, aud)
