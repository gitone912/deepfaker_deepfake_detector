from django import forms

class VideoUploadForm(forms.Form):
    video = forms.FileField(label='Select a video', widget=forms.FileInput(attrs={'accept': 'video/*'}))
