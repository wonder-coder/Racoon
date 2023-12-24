import elevenlabs

elevenlabs.set_api_key("1a83e0a5cd0957ce76c1da0d7620df78")

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