from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from .forms import RecipeForm, NewUserForm, LoginForm
from cookbook.models import Contributor, RecipeType, Recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request): 
    return render(request, "cookbook/index.html")

# Page containing the form to create a new recipe
@login_required(login_url="/cookbook/login/")
@permission_required('cookbook.add_recipe',raise_exception=True)
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # find if author already exists in db, create new db entry if not
            name = form.cleaned_data['author']
            authorSet = Contributor.objects.filter(name__startswith=name)
            nMatches = len(authorSet)
            if nMatches == 0:
                contributorDbEntry = Contributor(name=name)
            elif nMatches == 1:
                contributorDbEntry = authorSet.first()
            # TODO: handle multiple matches
            elif nMatches > 1:
                contributorDbEntry = authorSet.first()
            contributorDbEntry.save()

            # Get recipe type db entry
            recipeType = form.cleaned_data['recipe_type']
            type_set = RecipeType.objects.filter(name__startswith=recipeType)
            if len(type_set) == 0: 
                typeDbEntry = RecipeType(name=recipeType)
            else:
                typeDbEntry = type_set.first()
            typeDbEntry.save()

            # Create new recipe db entry
            recipeNameInput = form.cleaned_data['recipe_name']
            commentInput = form.cleaned_data['comment']
            ingredientsInput = form.cleaned_data['ingredients']
            instructionsInput = form.cleaned_data['instructions']
            newRecipeDbEntry = Recipe(name=recipeNameInput, 
                    type=typeDbEntry, 
                    author=contributorDbEntry, 
                    comment=commentInput, 
                    ingredients=ingredientsInput, 
                    instructions=instructionsInput)
            newRecipeDbEntry.save()

            return HttpResponseRedirect('/cookbook/')
    else: 
        form = RecipeForm()
    return render(request, "cookbook/create_recipe.html", {'form':form})

@login_required(login_url="/cookbook/login/")
@permission_required('cookbook.change_recipe', raise_exception=True)
def edit_recipe(request, recipe_id): 
    try: 
        recipe = Recipe.objects.get(pk=recipe_id)
    except: 
        raise Http404("Recipe not found")
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # find if author already exists in db, create new db entry if not
            name = form.cleaned_data['author']
            authorSet = Contributor.objects.filter(name__startswith=name)
            nMatches = len(authorSet)
            if nMatches == 0:
                contributorDbEntry = Contributor(name=name)
            elif nMatches == 1:
                contributorDbEntry = authorSet.first()
            # TODO: handle multiple matches
            elif nMatches > 1:
                contributorDbEntry = authorSet.first()
            contributorDbEntry.save()

            # Get recipe type db entry
            recipeType = form.cleaned_data['recipe_type']
            type_set = RecipeType.objects.filter(name__startswith=recipeType)
            if len(type_set) == 0: 
                typeDbEntry = RecipeType(name=recipeType)
            else:
                typeDbEntry = type_set.first()
            typeDbEntry.save()

            recipe.name = form.cleaned_data['recipe_name']
            recipe.type = typeDbEntry
            recipe.author = contributorDbEntry
            recipe.comment = form.cleaned_data['comment']
            recipe.ingredients =  form.cleaned_data['ingredients']
            recipe.instructions  = form.cleaned_data['instructions']
            recipe.save()
            return HttpResponseRedirect(f'/cookbook/display_recipe/{recipe_id}')
    else:
        form = RecipeForm(initial={"recipe_name":recipe.name,
                "recipe_type":recipe.type.name, 
                "author":recipe.author.name, 
                "comment":recipe.comment, 
                "ingredients":recipe.ingredients, 
                "instructions":recipe.instructions})
    return render(request, 'cookbook/edit_recipe.html',
            {'form':form, 'recipe_id':recipe.id})

# Display a recipe
def display_recipe(request, recipe_id): 
    try: 
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredients_list = recipe.ingredients.split(',')
    except: 
        raise Http404("Recipe not found")
    return render(request, 'cookbook/display_recipe.html',{'recipe':recipe, 
        "ingredients":ingredients_list})

def browse_recipes(request):
    try:
        recipes = Recipe.objects.all().order_by('name')
    except: 
        raise Http404("Oops")
    return render(request, 'cookbook/browse_recipes.html', {'recipes':recipes})

def create_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password'] 
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            user = User.objects.create_user(username, first_name=first, 
                    last_name=last, password=password)
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
            return HttpResponseRedirect("/cookbook/")
    else: 
        form = NewUserForm()
    return render(request, 'cookbook/signup.html', {'form':form})

def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] 
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                return HttpResponseRedirect('/cookbook/')
            else: 
                form = LoginForm()
    else: 
        form = LoginForm()
    return render(request, 'cookbook/login.html', {'form':form})

def userLogout(request): 
    logout(request)
    return HttpResponseRedirect('/cookbook/')
