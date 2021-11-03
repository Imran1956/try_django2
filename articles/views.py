from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required

from .form import ArticleForm

def home_detail(request,id):
    try :
         selected_obj = Articles.objects.get(id = id )
    except:
        selected_obj = None
    context = {
        "object" : selected_obj
    }
    return render(request,"articles/home_detail_view.html",context = context)


def search_view(request):

    obj = request.GET
    entity = obj.get("query")
    try:
        obj = Articles.objects.get(id = entity)
    except:
        obj = None

    context = {
        "object" : obj
    }
    return render(request,'articles/search_view.html',context=context)

@login_required
def create_articles(request):
    form = ArticleForm(request.POST or None)
    context = {'form' : form}
    if form.is_valid():
        obj = form.save() 
        context['form']=ArticleForm()
        

    return render(request,"articles/create_article.html",context=context)