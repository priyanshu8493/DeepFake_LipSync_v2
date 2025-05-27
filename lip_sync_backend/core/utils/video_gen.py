import os
import subprocess

def generate_lip_sync(image_path, audio_path, output_path="media/videos/output.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    command = [
        "python", "Wav2Lip/inference.py",
        "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth",
        "--face", image_path,
        "--audio", audio_path,
        "--outfile", output_path
    ]
    
    subprocess.run(command, check=True)
    return output_path
