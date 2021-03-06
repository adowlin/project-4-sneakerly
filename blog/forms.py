from django import forms

from .widgets import CustomClearableFileInput
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            'product', 'title', 'image_url', 'image', 'user_profile')

    image = forms.ImageField(
        label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'blog-style-input'
            if field == 'user_profile':
                self.fields[field].widget.attrs['id'] = 'user-hidden-input'
                self.fields[field].label = False
