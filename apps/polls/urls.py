from django.urls import path
from .views import IndexView, DetailView, ResultView, vote

app_name = "polls"

urlpatterns = [
    path('', IndexView.as_view() , name="index"),
    path('<int:pk>', DetailView.as_view(), name="detail"),
    path('results/<int:pk>', ResultView.as_view(), name="results"),
    path('vote/<int:question_id>', vote, name="vote"),
]
