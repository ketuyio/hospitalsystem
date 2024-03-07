from django import forms
from hopitapp.models import ImageModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']
