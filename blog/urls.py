# from .views import home,post,category
from django.urls import path
from blog import views


urlpatterns = [
    path('',views.index),
    path('blog/<slug:url>', views.post,),
    path('category/<slug:url>',views.category),
    path ('about/',views.about),
]