from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


urlpatterns= [
path('become_vendor/',views.become_vendor,name='become_vendor'),
path('vendor_admin/',views.vendor_admin,name='vendor_admin'),

    path('add_product/',views.add_product,name='add_product'),
    path('edit_product/<int:id>/',views.add_product,name='edit_product'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),


    path('login/',auth_view.LoginView.as_view(template_name='authentication/login.html') ,name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout')


]