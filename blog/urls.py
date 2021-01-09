from django.urls import path

from . import views

'''
app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''

#from .views import BlogListView

from .views import post, blog_posts

app_name = 'blog'
urlpatterns = [
	path('<int:pk>/<slug:slug>/', post, name='post_detail'),
	path('', blog_posts, name='blog_list'),
    #path('', BlogListView.as_view(), name='blog_list'),
]

