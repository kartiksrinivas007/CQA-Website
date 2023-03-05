from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def search_view(request):
    if request.POST:
        return HttpResponse('HI')
    return render(request, "search/search_view.html", {})
