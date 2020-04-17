from django.urls import path
from . import views
from .views import PostCreateView,PostDetailView,NotesDeleteView,SubjectDeleteView

urlpatterns = [

    path('', views.index, name='index'),
    path('sub/new/',PostCreateView.as_view(), name='post-create'),
    path('sub/<int:pk>/', PostDetailView.as_view(), name='sub-detail'),
    path('sub/<int:pk>/addnotes',views.addnotes, name='sub-addnotes'),
    path('note/<int:pk>/delete',NotesDeleteView.as_view(),name='notes-delete'),
    path('sub/<int:pk>/delete',SubjectDeleteView.as_view(),name='sub-delete'),

]