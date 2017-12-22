
from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CarForm
from django.http import HttpResponse
from .models import CarModel
import allthreads

class IndexView(View):
    def get(self, request):
        form = CarForm()
        cars = CarModel.objects.all()
        return render(request, 'index.html', {'form': form, 'list' : cars})

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            #print(request.POST)
            link = (request.POST.get('link'))
            states = (request.POST.getlist('states'))
            print(states)
            allthreads.main(states,link)
            return redirect('/')
        else:
            form = CarForm()
        return render(request, 'index.html', {'form': form})

class Remove(View):
    #Post = Post.objects.all()
    def get(self,request,format=None):
        idc = (int(request.GET.get('carid')))
        b = CarModel.objects.get(id=idc)
        b.delete()
        return redirect('/')
class Edit(View):
    def get(self,request,format=None):
        form = CarForm()
        idc = (int(request.GET.get('carid')))
        b = CarModel.objects.get(id=idc)
        print(b.link)
        return render(request, 'edit.html', {'form': form, 'car' : b})
    def post(self,request):
        form = CarForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            idc = (int(request.GET.get('carid')))
            print("ID: ", idc)
            #print("FORM: ", form)
            #print("POST: ", request.POST)
            #print(request.POST)
            link = (request.POST.get('link'))
            states = (request.POST.getlist('states'))
            p = CarModel.objects.get(id=idc)
            p.link = link
            p.states = states
            p.cities = ''
            p.save()
            allthreads.main(states,link)
            return redirect('/')
        else:
            form = CarForm()
        return render(request, 'index.html', {'form': form})
