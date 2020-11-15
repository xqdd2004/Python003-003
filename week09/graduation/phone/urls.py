from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('good', views.index),
    path('good/<str:content>', views.index_search),
    path('comment/<int:content>', views.page_comment)
]
