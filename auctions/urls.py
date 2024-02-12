from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create',views.create_list,name='create_list'),
    path('category',views.category,name='category'),
    path('items/<int:each>',views.items,name='items'),
    path('detailed/<int:item>',views.detailed,name='detailed'),
    path('addToWatchlist/<int:item>',views.addTowatchlist,name='addTowatchlist'),
    path('removeFromWatchlist/<int:item>',views.removeFromWatchlist,name='removeFromWatchlist'),
    path('placebid/<int:item>', views.placebid, name='placebid')

]
