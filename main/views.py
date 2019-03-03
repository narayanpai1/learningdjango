from django.shortcuts import render
from .models import dishes, filter, nc,comment_on_comment,nc_comments
from .forms import SearchForm


# Create your views here.
def home(request):
    x={'title':'Home'}
    return render(request,'main/home.html',x)


def menus(request):
    search_value=''
    form=SearchForm()
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            search_value=form.cleaned_data['search_value']

    context={'dishes':dishes.objects.all().order_by("nc__id"),'filter':filter.objects.all(),'form':form,'search_value':search_value,'check':"abcdef",'title':"Menus"}
    return render(request,'main/menu.html',context)


def nc_detail(request,nc_id):
    context={'title':nc.objects.all().filter(id=nc_id).first().name,
             'nc':nc.objects.all().filter(id=nc_id).first(),
             'comments':nc_comments.objects.all().filter(nc__id=nc_id),
             'comment_on_comment':comment_on_comment.objects.all()
             }
    return render(request, 'main/nc_detail.html', context)