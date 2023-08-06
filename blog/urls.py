from django.urls import path
from .views import bloglist,blog_detail,create_blog,update_blog

app_name='blog'
urlpatterns = [
    path("",bloglist,name='blogs'),
    path("<int:id>/",blog_detail,name='blogdetail'),
    path("add/",create_blog,name="createblog"),
    path("<int:id>/update/",update_blog,name="updateblog")
]