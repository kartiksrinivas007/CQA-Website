from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from cqa.models import *
from search.forms import SearchForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
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
            user_id = search.split(' ')[0]
            q = Posts.objects.filter(owner_user_id = int(user_id))
            return q
        if(search[0] == '#'):
            tags = search.split(',')
            tags = [ '<' + tag[1:].strip() + '>' for tag in tags ]
            # string =''.join(tags)
            # for tag in tags:
            #     q = Posts.objects.filter(Q(tags__icontains = string))
            # return q
            string = tags[0]
            q = Posts.objects.filter(tags__icontains = string)
            for tag in tags:
                q = q.union(Posts.objects.filter(tags__icontains = tag))
            return q
        else:
            return Posts.objects.filter(Q(title__icontains = search) | Q(body__icontains = search))
        
        
    

