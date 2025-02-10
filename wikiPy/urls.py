from django.urls import path
from . import views

app_name = 'wikiPy'

urlpatterns = [
    path('', views.home, name='home'),
    path('newTheme', views.newTheme, name='newTheme'),
    path('newArticle', views.newArticle, name='newArticle'),
    path('themeList', views.themeList, name='themeList'),
    path('articlesByTheme/<str:idTheme>', views.articlesByTheme, name='articlesByTheme'),
    path('view_article/<str:idArticle>', views.view_article, name='view_article')
    
]