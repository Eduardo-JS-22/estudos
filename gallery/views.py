from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gallery.models import Image

def index(request):
    images = Image.objects.all()
    return render(request, 'gallery/index.html', {'cards': images})
def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/image.html', {'image': image})