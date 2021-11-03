from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "content"]
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Articles.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title","this title is already taken.Try something new")
        return data 

class ArticleFormold(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def cleaned_title(self):
         title = self.cleaned_data.get("title")
    