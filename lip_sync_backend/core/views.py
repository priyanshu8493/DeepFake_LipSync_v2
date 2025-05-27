from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import render
from .models import LipSyncRequest

def upload_script(request):
    
    if request.method == 'POST':
        image = request.FILES.get('image')
        script = request.POST.get('script')
        req = LipSyncRequest.objects.create(image=image, script=script)
        # TODO: Generate audio & video
        return render(request, 'result.html', {'req': req})
    return render(request, 'upload.html')
