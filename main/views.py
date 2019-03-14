from django.shortcuts import render
from .models import dishes, filter, nc
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



def current(request, nc_id):
    if request.method== "POST":
        item_id=int(request.POST.dict().get("add_or_remove"))
        item1=dishes.objects.all().filter(id=item_id).first()
        if item1.currently_present == True:
            item1.currently_present = False
        else:
            item1.currently_present = True
        item1.save()

    context={'dishes':dishes.objects.all().filter(nc__id=nc_id),'nc':nc.objects.all().filter(id=nc_id).first(),'filter':filter.objects.all()}
    return render(request, 'main/current_items.html', context)


def contact_us(request):
    context={'nc': nc.objects.all(), 'title': "Call us"}
    return render(request, 'main/contact_us.html', context)

def api(request):
    s=""
    for item in dishes.objects.all():
        s=s+'{"name":"' + item.name + '", "price":' + str(item.price) + "}"
        if not(item.id == len(dishes.objects.all())):
            s=s+', '
    return HttpResponse('{"context":['+ s + ']}')

def menu_api(request):
    serialized=""
    context=dishes.objects.filter(currently_present=True).order_by('nc__id')
    i=0
    for item in context :
        i=i+1
        dict_obj = model_to_dict(item)
        serialized  = serialized + json.dumps(dict_obj)

        if i != len(context):
            serialized= serialized +', '
    return HttpResponse('{"context":[' +serialized + ']}')
