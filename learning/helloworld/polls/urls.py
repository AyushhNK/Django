from django.urls import path
from . import views

app_name="polls"
urlpatterns=[
	path("",views.IndexView),
	path("<int:question_id>/", views.DetailView, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.ResultsView, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.VoteView, name="vote"),
]