from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gallery.models import Image

def index(request):
    images = Image.objects.order_by('-image_date').filter(published=True)
    return render(request, 'gallery/index.html', {'cards': images})
def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/image.html', {'image': image})
def search(request):
    images = Image.objects.order_by('-image_date').filter(published=True)
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            images = images.filter(description__icontains=search_term)
            return render(request, 'gallery/search.html', {'cards': images, 'search_term': search_term})
    return render(request, 'gallery/search.html')