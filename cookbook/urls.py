from django.urls import path

from . import views

app_name = 'cookbook'
urlpatterns = [ 
        path('', views.index, name='index'),
        path('new_recipe/', views.new_recipe, name='new_recipe'),
        path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
        path('display_recipe/<recipe_id>/', views.display_recipe, name='display_recipe'),
        path('browse_recipes/', views.browse_recipes, name='browse_recipes'),
        path('signup/', views.create_user, name='create_user'),
        path('login/', views.userLogin, name='login'),
        path('logout/', views.userLogout, name='logout'),
]
