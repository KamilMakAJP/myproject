from django.shortcuts import render

def lab0_view(request):
    return render(request, 'lab0/index.html')