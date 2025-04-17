from django.urls import path

from . import views

urlpatterns = [
    path(
        "documents/", views.DocumentListView.as_view(), name="documents-list"
    ),
    path(
        "documents/contribute/",
        views.DocumentCreateView.as_view(),
        name="document-create",
    ),
    path(
        "documents/detail/<int:pk>/",
        views.DocumentDetailView.as_view(),
        name="document-detail",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileDetailView.as_view(), name="profile"),
    path(
        "profile/update/",
        views.ProfileUpdateView.as_view(),
        name="profile-update",
    ),
    path("forums/", views.ForumListView.as_view(), name="forums-list"),
    path(
        "forums/detail/<int:pk>/",
        views.ForumDetailView.as_view(),
        name="forum-detail",
    ),
    path("posts/", views.ArticleListView.as_view(), name="posts-list"),
    path(
        "post/detail/<int:pk>/",
        views.ArticleDetailView.as_view(),
        name="post-detail",
    ),
    path("connects/", views.ConnectListView.as_view(), name="connects-list"),
    path(
        "connects/detail/<int:pk>",
        views.ConnectDetailView.as_view(),
        name="connect-detail",
    ),
    path(
        "add-connect/",
        views.ConnectTicketCreateView.as_view(),
        name="add-connect",
    ),
    path(
        "connects/create/",
        views.ConnectCreateView.as_view(),
        name="connect-create",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),
    path(
        "forums/create/",
        views.ForumCreateView.as_view(),
        name="forum-create",
    ),
    path(
        "your_connect_detail/<int:pk>/",
        views.YourConnectDetailView.as_view(),
        name="your-connect-detail",
    ),
]
