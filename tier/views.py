from django.shortcuts import render
from .models import Article

# Create your views here.
def tier_index(request):
    articles = Article.objects.all()
    data = {'articles': articles,}
    return render(request, 'tier/tier_index.html', data)

def article(request, name):
    try:
        article = Article.objects.get(title=name)
        data = {'article': article}
    except:
        data = {'message': 'La réunion que vous avez demandée n\' existe pas'}
    return render  (request, 'tier/article.html', data)