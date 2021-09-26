from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import UploadImageForm
from .models import Images
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Images(image=request.FILES['image'], category=request.POST['category'], title=request.POST['title'])
            newdoc.save()

    else:
        form = UploadImageForm()  # An empty, unbound form
    images = Images.objects.all()
    context = {'images': images}
    return render(request, 'image_repo/index.html', context)