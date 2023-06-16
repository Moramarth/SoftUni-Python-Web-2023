from django.shortcuts import render, redirect, get_object_or_404

from games_play_app.accounts.models import Profile
from games_play_app.games.forms import GameForm, GameDeleteForm
from games_play_app.games.models import Game


# Create your views here.


def create_game(request):
    form = GameForm()
    if request.method == "POST":
        user = Profile.objects.first()
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = GameForm(data)
        if form.is_valid():
            form.save()
            return redirect("display dashboard")
    context = {"form": form}
    return render(request, "create-game.html", context=context)


def game_details(request, pk):
    game = get_object_or_404(Game, pk=pk)
    context = {"game": game}
    return render(request, "details-game.html", context=context)


def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    form = GameForm(initial=game.__dict__)
    if request.method == "POST":
        user = Profile.objects.first()
        data = request.POST.copy()
        data["created_by"] = user.pk
        form = GameForm(data, instance=game)
        if form.is_valid():
            form.save()
            return redirect("display dashboard")
    context = {"form": form}
    return render(request, "edit-game.html", context=context)


def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    form = GameDeleteForm(initial=game.__dict__, instance=game)
    if request.method == "POST":
        game.delete()
        return redirect('display dashboard')
    context = {"form": form}
    return render(request, "delete-game.html", context=context)
