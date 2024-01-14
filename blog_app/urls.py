from django.urls import path
from .views import create_post, create_comment, create_reel, view_post, delete_post, view_post_and_comment

urlpatterns = [
    path("createpost/", create_post),
    path("createcomment/", create_comment),
    path("createreel/", create_reel),
    path("all_post/", view_post),
    path("delete_post/<int:id>/", delete_post, name="delete_post"),
    path("post/<int:ID>/<str:title>/", view_post_and_comment, name="full_post")
]