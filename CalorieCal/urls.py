from django.urls import path
from . import views


urlpatterns = [
    path("", views.calorie_input_view, name="input"),
    path("result<int:result_id>/", views.result_view, name="result"),
    path("history/", views.history_view, name="history"),
]
