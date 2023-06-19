from django.shortcuts import render, redirect, get_object_or_404

from recipes_app.recipes.forms import RecipeForm, RecipeDeleteForm
from recipes_app.recipes.models import Recipe


# Create your views here.


def home_page(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "index.html", context)


def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    context = {"form": form}
    return render(request, "create.html", context)


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(initial=recipe.__dict__)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home page")
    context = {"form": form}
    return render(request, "edit.html", context)


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeDeleteForm(initial=recipe.__dict__, instance=recipe)
    if request.method == "POST":
        recipe.delete()
        return redirect("home page")
    context = {"form": form}
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.split(", ")
    context = {
        "recipe": recipe,
        "ingredients": ingredients,
    }
    return render(request, "details.html", context)
