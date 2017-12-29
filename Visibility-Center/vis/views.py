from django.shortcuts import render

def vis_main(request):
    return render(request, 'vis/layout.html')
