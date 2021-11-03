from articles.models import Articles
from django.http import HttpResponse
from django.template.loader import render_to_string 

def home(request):
    obj = Articles.objects.all()

    context = {
        "object" : obj 

    }
    string = render_to_string('home.html',context = context)
    return HttpResponse(string)