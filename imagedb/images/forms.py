from django import forms


class ImageForm(forms.ModelForm):
    label_field = forms.CharField(max_length=255)
