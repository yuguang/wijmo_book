from django.shortcuts import render
import settings, os, glob

def gallery(request):
    files = ['img/' + os.path.basename(file) for file in glob.glob(os.path.join(settings.BASE_DIR, 'static/img/*.png'))]
    return render(request, 'gallery.html', { 'images': files })