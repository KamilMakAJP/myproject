from django.shortcuts import render

def home(request):
    context = {
        "hobby_name": "Fotografia",
        "description": "Uwielbiam uwieczniać ulotne chwile za pomocą aparatu."
    }
    return render(request, 'lab1/home.html', context)

def about(request):
    return render(request, 'lab1/about.html')

def gallery(request):
    return render(request, 'lab1/gallery.html')