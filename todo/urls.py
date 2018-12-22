from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    # 详情页
    path('<int:id>', views.detail, name='detail'),
    # 完成时间
    path('<int:id>/finish', views.finish, name='finish'),
    # 完成
    path('<int:id>/cancel', views.cancel, name='cancel'),
    # 添加
    path('create/', views.create, name="create"),
]