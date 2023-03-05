from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from cqa.models import *
from search.forms import SearchForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
context = {}
context["tags"] = ['#' + tag.tag_name for tag in Tags.objects.all()]
context["users"] = [":" + str(id) + "   Name:   "  + str(display_name) for id, display_name in CustomUser.objects.all().values_list('id','display_name')]
# Create your views here.
def search_view(request):
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            return redirect('search_results', search = search)

    form = SearchForm()
    global context
    context["form"] = form
    print(context["users"][1])
    return render(request, "search/search_view.html", context)

class search_results_view(ListView):
    model = Posts
    template_name = 'search/search_results.html'
    paginate_by = 10
    ordering = ['-answer_count']
    context_object_name = 'posts'
    
    def get_queryset(self):
        search = self.kwargs['search']
        # try user 200302
        if(search[0] == ':'):
            search = search[1:]
            q = Posts.objects.filter(Q(owner_user_id__icontains = search))
            return q
        if(search[0] == '#'):
            tags = search.split(',')
            tags = [ '<' + tag[1:].strip() + '>' for tag in tags ]
            string =''.join(tags)
            for tag in tags:
                q = Posts.objects.filter(Q(tags__icontains = string))
            return q
        else:
            return Posts.objects.filter(Q(title__icontains = search) | Q(body__icontains = search))
        
        
    

