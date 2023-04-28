from django.urls import path

from . import views


app_name = "polls" 
urlpatterns = [
    path('',views.index,name="index"),

    path("detail/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("results/<int:question_id>/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("vote/<int:question_id>/", views.vote, name="vote"),

     path("register/", views.register, name="register"),

]
