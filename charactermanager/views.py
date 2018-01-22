from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render

from .models import Character, Player, Vampire


def index(request):
    player_list = Player.objects.order_by('name')[:30]
    context = {'player_list': player_list}
    return render(request, 'charactermanager/index.html', context)

def playerlist(request):

    player_list = Player.objects.all()
    paginator = Paginator(player_list.order_by('name'), 10) # Show 25 contacts per page

    page = request.GET.get('page')
    players = paginator.get_page(page)
    return render(request, 'charactermanager/playerlist.html', {'players': players})

    #player_list = Player.objects.order_by('name')[:30]
    #context = {'player_list': player_list}
    #return render(request, 'charactermanager/playerlist.html', context)

def characterlist(request):

    vampire_list = Vampire.objects.all()
    paginator = Paginator(vampire_list.order_by('name'), 10) # Show 25 contacts per page

    page = request.GET.get('page')
    vampires = paginator.get_page(page)
    return render(request, 'charactermanager/characterlist.html', {'vampires': vampires})

    # FOR USE WITH CHARACTER OBJECTS (5E)
    # character_list = Character.objects.all()
    # paginator = Paginator(character_list.order_by('name'), 10) # Show 25 contacts per page
    #
    # page = request.GET.get('page')
    # characters = paginator.get_page(page)
    # return render(request, 'charactermanager/characterlist.html', {'characters': characters})

def playerdetail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'charactermanager/playerdetail.html', {'player': player})

def characterdetail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'charactermanager/characterdetail.html', {'character': character})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
