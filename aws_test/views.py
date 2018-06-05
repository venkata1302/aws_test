
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Player
from .forms import PlayerForm
from django.shortcuts import render,redirect,HttpResponseRedirect

class home(View):
    template_name = 'home.html'
    def get(self,request):
        return render(request,self.template_name)

def add_player(request):
    if request.method == 'GET':
        form = PlayerForm()
        return render(request,'addplayer.html',{'form': form})
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

class player_list(ListView):
    model = Player
    query_set = Player.objects.all()
    template_name = 'playerlist.html'

        

        
    
