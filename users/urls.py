from django.urls import path
from .views import RegisterView, UserDetailView, PackageListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('me/', UserDetailView.as_view()),
    path('packages/', PackageListView.as_view()),
]
