from .models import LipSyncRequest
from django.shortcuts import render
from core.utils.audio_gen import generate_audio_from_text
from core.utils.video_gen import generate_lip_sync

def upload_script(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        script = request.POST.get('script')
        req = LipSyncRequest.objects.create(image=image, script=script)

        # Paths
        img_path = req.image.path
        audio_path = f"media/audio/output_{req.id}.wav"
        video_path = f"media/videos/output_{req.id}.mp4"

        # TTS
        generate_audio_from_text(script, audio_path)
        req.audio.name = audio_path.replace('media/', '')

        # Wav2Lip
        generate_lip_sync(img_path, audio_path, video_path)
        req.video.name = video_path.replace('media/', '')
        req.save()

        return render(request, 'result.html', {'req': req})

    return render(request, 'upload.html')
