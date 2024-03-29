from django.urls import path 
#引入同一文件夹下的views.py
from . import views
#部署app的名字
app_name = 'article'
urlpatterns = [
	#path函数将url映射到视图
	path('article-list/',views.article_list,name='article_list'),
	path('article-detail/<int:id>/',views.article_detail,name='article_detail'),
	path('article-create/',views.article_create,name='article_create'),
	path('articl-delete/<int:id>/',views.article_delete,name='article_delete'),
	path('article-safe-delete/<int:id>/',views.article_safe_delete,name='article_safe_delete'),
	path('article-update/<int:id>/',views.article_update,name='article_update'),
    	# 列表类视图
    	path('list-view/', views.ArticleListView.as_view(), name='list_view'),
  	 # 详情类视图
  	  path('detail-view/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_view'),
   	 # 创建类视图
    	path('create-view/', views.ArticleCreateView.as_view(), name='create_view'),
    # 点赞 +1
    path(
        'increase-likes/<int:id>/', 
        views.IncreaseLikesView.as_view(), 
        name='increase_likes'
    ),
]