from django.urls import path
from hello import views

urlpatterns = [
    path('special', views.special, name='special'),
    path('query_time', views.query_time, name='query_time'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
