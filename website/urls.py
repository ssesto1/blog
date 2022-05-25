from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="all-posts"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("certificates", views.CertificatesView.as_view(), name="certificates")
]
