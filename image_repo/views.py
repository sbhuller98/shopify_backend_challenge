from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import UploadImageForm
from .models import Images
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    '''Returns all images in database.
    
    :param request: The incoming request object.
    :return: Returns view with all images in database.'''
    images = Images.objects.all()
    context = {'images': images}
    return render(request, 'image_repo/index.html', context)

@login_required
def postImage(request):
    '''Uploads image to database by creting new image object.
    
    :param request: The incoming request object.
    :return: Returns view with all images in database.'''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("here")
            newdoc = Images(image=request.FILES['image'], category=request.POST['category'], title=request.POST['title'])
            newdoc.save()
    url = reverse('index')
    return HttpResponseRedirect(url)

@login_required
def search(request):
    '''Search in database based on Name feature and Category feature.
    
    :param request: The incoming request object.
    :return: Returns view with all images in database that match search criteria.'''
    if request.GET["name"] == "":
        images = Images.objects.filter(category__contains=request.GET["category"])
    elif request.GET["category"] == "":
        images = Images.objects.filter(title__contains=request.GET["name"])
    else:
         images = Images.objects.filter(title__contains=request.GET["name"], category__contains=request.GET["category"])
    context = {'images': images}
    return render(request, 'image_repo/index.html', context)

@login_required
def deleteImages(request):
    '''Deletes specified images from database. Can handle single or multiple images to be deleted at once.
    
    :param request: The incoming request object.
    :return: Returns view with all remaining images in database.'''
    valuesToDelete = request.POST["valuesToDelete"]
    if valuesToDelete == None or valuesToDelete == "":
        url = reverse('index')
        return HttpResponseRedirect(url)
    valuesToDelete = valuesToDelete.split(",")
    for val in valuesToDelete:
        objToDelete = Images.objects.get(id=val)
        objToDelete.image.delete()
        objToDelete.delete()
    url = reverse('index')
    return HttpResponseRedirect(url)