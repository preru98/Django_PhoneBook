from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('<int:contact_id>/', views.detail, name ='detail'),
    path('all/',views.all,name='all'),
    path('delete/<int:contact_id>/',views.delete,name='delete'),
    path('insert/',views.insert,name='insert'),
    path('add/',views.add,name='add'),
] 