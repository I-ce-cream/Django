# from django.conf.urls import url
# from .views import index

# from Myapp import views
# from Myapp.views import indexss
# import Myapp.views as views

from django.urls import path
from Myapp.views import Index


urlpatterns = [
    # ？参数方式传参
    # path('', index2)

    # / 方式传参
    # path('<str:name>/<int:age>', index)

    # class视图
    path('<str:name>/<int:age>', Index.as_view())
]