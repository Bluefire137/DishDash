from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Dishes

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Рецепты', 'url_name': 'dish'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

types_db = [
    {'id': 1, 'name': 'Салаты'},
    {'id': 2, 'name': 'Супы'},
    {'id': 3, 'name': 'Горячее'},
    {'id': 4, 'name': 'Десерты'}
]


def index(request):
    recipes = Dishes.objects.all()
    data = {'title': 'Рандомное блюдо на каждый день!',
            'menu': menu,
            'dishes': recipes
            }
    return render(request, 'dishes/index.html', context=data)


def about(request):
    return render(request, 'dishes/about.html', {'title': 'О сайте', 'menu': menu})


def show_recipe(request, dish_slug):
    recipe = get_object_or_404(Dishes, slug=dish_slug)
    data = {'title': recipe.title,
            'type': recipe.type,
            'time_to_cook': recipe.time_to_cook,
            'description': recipe.description,
            'link': recipe.link,
            'menu': menu,
            'recipe': recipe,
            'typ_selected': 1
            }
    return render(request, 'dishes/recipe.html', data)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_types(request, type_id):
    return index(request)


'''
def types(request, types_id):
    return HttpResponse(f"<h1>Выберите тип</h1><p>id: {types_id}</p>")


def types_by_slug(request, types_text):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Выберите тип</h1><p>Блюдо: {types_text}</p>")


def archive(request, year):
    if year > 2024:
        uri = reverse('types', args=('dish',))
        return redirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")'''


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
