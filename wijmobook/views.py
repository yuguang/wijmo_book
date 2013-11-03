from django.shortcuts import render
import settings, os, glob

def gallery(request):
    files = []
    for file in glob.glob(os.path.join(settings.BASE_DIR, 'static/img/*.png')):
        files.append({
            'path': 'img/' + os.path.basename(file),
            'title': os.path.basename(file)
        })
    return render(request, 'gallery.html', { 'images': files })