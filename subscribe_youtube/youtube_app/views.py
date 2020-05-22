from django.shortcuts import render,get_object_or_404,redirect
from .models import youtube
from .forms import createForm
from django.template import RequestContext
# Create your views here.

def index(request):
    Youtube = youtube.objects.all()
    return render(request, 'index.html',{'Youtube':Youtube})

def develop(request):
    Youtube = youtube.objects.all()
    return render(request, 'develop.html',{'Youtube':Youtube})

def detail(request,detail_id):
    detail = get_object_or_404(youtube, pk= detail_id)
    return render(request,'detail.html',{'content':detail})

def new(request):
    form = createForm()
    if request.method =='POST':
        pass
    elif request.method =='GET':
        form = createForm()
        return render(request,'new.html',{'form':form})
    else:
        pass

def create(request):
    Youtube = youtube() 
    Youtube.name = request.POST['name']
    Youtube.creator = request.POST['creator']
    Youtube.subscribe_num = request.POST['subscribe_num']
    Youtube.recommend = request.POST['recommend']
    Youtube.youtube_link_1 = request.POST['youtube_link_1']
    Youtube.youtube_link_2 = request.POST['youtube_link_2']
    Youtube.youtube_link_3 = request.POST['youtube_link_3']
    Youtube.summary = request.POST['summary']
    Youtube.text = request.POST['text']
    Youtube.on_off = request.POST['choices']
    Youtube.photo = request.FILES['photo']
    Youtube.save()
    return redirect('develop')
    