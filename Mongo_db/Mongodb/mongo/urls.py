from .views import StudentView
from django.urls import path

urlpatterns = [
    path('Student/',StudentView.as_view()),
    path('Student/<int:id>/',StudentView.as_view()),
    path('Student/<int:id>/update/', StudentView.as_view()),
]
