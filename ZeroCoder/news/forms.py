from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.utils import timezone

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'News post title'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Short deenition'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'News post text'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Date and time of publication'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for 'pub_date' to current date and time
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")
