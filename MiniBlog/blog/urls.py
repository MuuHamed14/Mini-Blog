from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<int:id>/',views.detail_post,name='detail_post'),
    path('contact/', views.contact, name='contact'),
    path('AddPost/',views.add_post,name='add_post'),
    path('UpdatePost/<int:id>/',views.update_post,name='update_post'),
    path('DeletePost/<int:id>/',views.delete_post,name='delete_post'),
]
