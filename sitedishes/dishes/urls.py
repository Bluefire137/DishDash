from django.urls import path, register_converter
from . import converters
from . import views

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('recipe/<slug:dish_slug>', views.show_recipe, name='recipe'),
    path('recipe/', views.show_recipe, name='dish'),
    path('types/<int:type_id>', views.show_types, name='types')

]

'''
    path('types/<int:types_id>/', views.types, name='types_id'),
    path('types/<slug:types_text>/', views.types_by_slug, name='types'),
    path('archive/<year4:year>/', views.archive, name='archive')
]
'''
