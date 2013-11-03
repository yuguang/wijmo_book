import os
import glob
import string

from django.shortcuts import render

import settings


def underscore_to_camelcase(s):
    return string.capwords(s, '_').replace('_', ' ')

def gallery(request):
    files = []
    for file in glob.glob(os.path.join(settings.BASE_DIR, 'static/img/*.png')):
        base_file = os.path.basename(file)
        files.append({
            'path': 'img/' + base_file,
            'title': underscore_to_camelcase(os.path.splitext(base_file)[0])
        })
    return render(request, 'gallery.html', { 'images': files })