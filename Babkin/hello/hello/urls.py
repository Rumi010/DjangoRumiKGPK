from django.contrib import admin
from django.urls import path, re_path
from web_app import views

urlpatterns = [
    path('', views.index),
    re_path('home/', views.home, name='home'),
    path("registration/", views.registration, name="reg"),
    path("registration/f", views.registration_fail, name="reg_f"),
    path('admin/', admin.site.urls),
    path("import/", views.import_db),
    path('submit/', views.submit_form, name='submit_form'),
    path('submit_reg/', views.registration_form, name='submit_reg_form'),
    path('submit_e/', views.sub_e_form, name='submit_e_form'),
    path("reg/", views.reg_form, name="reg_form"),
    path("lk/", views.lk, name="org"),
    re_path('my_events/', views.my_events, name="my_e"),
    re_path('my_people/', views.my_people, name="my_p"),
    re_path('my_jury', views.my_jury, name="my_j"),
    path("lk/reg_p/", views.registration_jury, name="reg_p"),
    path("lk/profile/", views.profile, name="prof"),
    path("lk/logout/", views.logout_user, name="logout"),
    path("lk/add_event/", views.add_e, name="add_e"),
]
