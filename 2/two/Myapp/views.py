from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self, request, name, age):

        # 查看request对象
        print(dir(request))
        return HttpResponse('name:{0},  age:{1}'.format(name, age))


# ？ 方式传参
# def index2(request):
#     name = request.GET.get('name', '')
#     age = request.GET.get('age', 0)
#     return HttpResponse('name:{0},  age:{1}'.format(name, age))


# / 参数方式传参
# def index2(request,name,age):
#     # name = request.GET.get('name', '')
#     # age = request.GET.get('age', 0)
#     return HttpResponse('name:{0},  age:{1}'.format(name, age))
