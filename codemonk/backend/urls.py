from django.urls import path

from .views import getParagraph, login, postParagraph, searchWord, signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("paragraph/", postParagraph, name="paragraph"),
    path("search/paragraph/", searchWord, name="search_paragraph"),
    path("get/paragraph/", getParagraph, name="get_paragraph"),
]
