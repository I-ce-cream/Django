from django.shortcuts import render

# Create your views here.
import requests
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse


# class LessionTwo(View):
#     def get(self, request, message):
#         # message = request.GET.get('message', '这里没有内容')
#         return HttpResponse(message)


class Music(View):

    DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={0}'

    def get(self, request):
        music_name = request.GET.get('musicname','')
        if not music_name:
            return JsonResponse({'errcode': -1, 'errmsg': '音乐名称不能为空'})

        url = self.DOUBAN_MUSIC_API.format(music_name)
        response = requests.get(url)
        data = response.json()
        return JsonResponse({'errcode': 0, 'errmsg': '成功', 'data': data})


class Movie(View):
    DOUBAN_MOVIE_API = 'https://api.douban.com/v2/movie/search?q={0}&apikey=0df993c66c0c636e29ecbb5344252a4a'

    def get(self, request):
        movie_name = request.GET.get('moviename', '')
        if not movie_name:
            return JsonResponse({'errcode': -1, 'errmsg': '电影名称不能为空'})

        url = self.DOUBAN_MOVIE_API.format(movie_name)

        try:
            response = requests.get(url)
        except Exception as e:
            return JsonResponse({'errcode': -1, 'errmsg': str(e)})

        if response.status_code != 200:
            return JsonResponse({'errcode': -1, 'errmsg': '请求豆瓣异常'})

        data = response.json()
        return JsonResponse({'errcode': 0, 'errmsg': '成功', 'data': data})


