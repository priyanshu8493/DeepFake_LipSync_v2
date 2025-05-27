from bark import generate_audio
import os

def generate_audio_from_text(text, output_path="media/audio/generated.wav"):
    audio_array = generate_audio(text)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    import scipy.io.wavfile
    scipy.io.wavfile.write(output_path, rate=22050, data=audio_array)
    
    return output_path
