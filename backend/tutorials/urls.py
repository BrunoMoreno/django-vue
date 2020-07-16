from django.urls import path
from tutorials.views import *
 
urlpatterns = [ 
    path('api/tutorials', tutorial_list),
    path('api/tutorials/<int:pk>', tutorial_detail),
    path('api/tutorials/published', tutorial_list_published)
]