from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import UploadImageForm
from .models import Images
from django.urls import reverse
# Create your views here.

def index(request):
    images = Images.objects.all()
    context = {'images': images}
    return render(request, 'image_repo/index.html', context)

def postImage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("here")
            newdoc = Images(image=request.FILES['image'], category=request.POST['category'], title=request.POST['title'])
            newdoc.save()
    url = reverse('index')
    return HttpResponseRedirect(url)

def search(request):
    if request.GET["name"] == "":
        images = Images.objects.filter(category__contains=request.GET["category"])
    elif request.GET["category"] == "":
        images = Images.objects.filter(title__contains=request.GET["name"])
    else:
         images = Images.objects.filter(title__contains=request.GET["name"], category__contains=request.GET["category"])
    context = {'images': images}
    return render(request, 'image_repo/index.html', context)
    