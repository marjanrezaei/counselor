from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'blog\\blog.html') 

def single(request):
    return render(request, 'blog\\blog-single.html')
