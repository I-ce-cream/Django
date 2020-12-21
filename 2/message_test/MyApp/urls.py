# coding:utf-8

from django.urls import path
from MyApp.views import Music,Movie

urlpatterns = {
    # path('two', LessionTwo.as_view(), name='two')
    path('music', Music.as_view()),
    path('movie', Movie.as_view())
}
