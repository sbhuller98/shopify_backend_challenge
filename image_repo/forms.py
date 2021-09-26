from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=75)
    category = forms.CharField(max_length=50)
    image = forms.FileField(label='CHoose an image')