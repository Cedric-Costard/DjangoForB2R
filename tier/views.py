from django.shortcuts import render

# Create your views here.
def tier_index(request):
    return render(request, 'tier/tier_index.html')

def article(request, name):
    return render  (request, 'tier/article.html')