from . import views 
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('success/', views.ContactSuccessView.as_view(), name="success"),
    path('report/', views.reportUser.as_view(), name="report"),
    path('add_post/', views.AddPostView.as_view(), name="add_post"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
]
