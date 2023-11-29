from .views import StudentView
from django.urls import path

urlpatterns = [
    path('Student/',StudentView.as_view()),
    path('Student/<str:_id>/',StudentView.as_view()),
    path('Student/<str:_id>/update/', StudentView.as_view()),
]
