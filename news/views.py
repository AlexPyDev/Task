from django.shortcuts import render


def index(request):
    # categories = Category.objects.all()
    return render(request, 'news/index.html')

# Create your views here.
