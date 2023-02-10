from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Prayers, Salat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



@login_required
def salats_index(request):
 

    url = "https://aladhan.p.rapidapi.com/timingsByCity"

    querystring = {"country":"<REQUIRED>","city":"<REQUIRED>"}

    headers = {
        "X-RapidAPI-Key": "24bb28c4ddmshc6ef3b0fcab9be7p12441ejsn667b60715565",
        "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    salats = Salat.objects.select_related().filter(user=request.user)
    return render(request, 'salat/index.html', {'salats': salats})

# @login_required
# def assoc_prayers(request, prayer_id):
#   Beyonce.objects.get(id=beyonce_id).tours.add(tour_id)
#   return redirect('detail', beyonce_id=beyonce_id)

 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      
      user = form.save()
      
      login(request, user)
      
      return redirect('index')
   
    else:
      
      error_message = 'invalid credentials'
  
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error': error_message
  })


class SalatCreate(LoginRequiredMixin, CreateView):
  model = Salat  
  fields = ('name', 'time', 'rakat', 'giblat')
  success_url = '/salats/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SalatUpdate(LoginRequiredMixin, UpdateView):
  model = Salat
  fields = ('name', 'time', 'rakat')

class SalatDelete(LoginRequiredMixin, DeleteView):
  model = Salat
  success_url = '/salats/'

class SalatDetail(LoginRequiredMixin, DeleteView):
  model = Salat

class PrayerIndex(LoginRequiredMixin, ListView):
  model = Prayers

class PrayersDetail(LoginRequiredMixin, DetailView):
  model = Prayers

class PrayerCreate(LoginRequiredMixin, CreateView):
  model = Prayers
  fields = '__all__'

class PrayerUpdate(LoginRequiredMixin, UpdateView):
  model = Prayers
  fields = '__all__'

class PrayerDelete(LoginRequiredMixin, DeleteView):
  model = Prayers
  success_url = '/prayers/'


def prayers_search(request):
  query = request.query_params.get('search',None)
  if query is None:
    return render(request,'search.html')

@login_required
def assoc_prayers(request, salat_id):
  Salat.objects.get(id=salat_id).prayers.add(prayers_id)
  return redirect('detail', salat_id=salat_id)