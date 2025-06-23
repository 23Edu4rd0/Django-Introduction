from django.shortcuts import render, get_object_or_404
from galeria.models import Image



# Create your views here.
def index(request):
    data = Image.objects.all()
    return render(request, "galeria/index.html", {"cards": data})

def image(request, image_id):
    img = get_object_or_404(Image, id=image_id)
    return render(request, "galeria/imagem.html", {"img": img})