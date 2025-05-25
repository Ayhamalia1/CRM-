from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('createCustomer/',views.Create,name='createCustomer'),
    path('delete/<int:id>',views.deleteUser,name='deleteUser'),
    path('update/<int:id>',views.updateUser,name='updateUser'),
    path('services/<int:id>',views.ShowServices,name='services'),
    path('search/',views.Search,name='search'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('profile/',views.userProfile,name='profile'),

]