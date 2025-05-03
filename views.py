from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from djangocms_blog.models import Post


def welcome_page_view(request):

    return render(
        request,
        "pages/welcome_page.html",
        context={
            "page_name": "welcome_page",
        },
    )


def login_view(request):

    return render(
        request,
        "pages/login.html",
        context={
            "page_name": "login",
        },
    )


def register_view(request):

    return render(
        request,
        "pages/register.html",
        context={
            "page_name": "register",
        },
    )


def home_view(request):

    posts = Post.objects.order_by("-date_published")
    NUMBER_OUTSTANDING_NEWS = 6
    featured_news_list = posts[:NUMBER_OUTSTANDING_NEWS]

    return render(
        request,
        "pages/home.html",
        context={
            "page_name": "home",
            "featured_news_list": featured_news_list,
        },
    )


def couple_friends_view(request):

    return render(
        request,
        "pages/couple_friends.html",
        context={
            "page_name": "couple_friends",
        },
    )


def send_request_view(request):

    return render(
        request,
        "pages/send_request.html",
        context={
            "page_name": "send_request",
        },
    )


def room_view(request):

    return render(
        request,
        "pages/room.html",
        context={
            "page_name": "room",
        },
    )



def documents_view(request):

    # TODO: add get post in documents

    # posts = Post.objects.order_by("-date_published").prefetch_related(
    #     "translations"
    # )

    PAGE_SIZE = 8
    # paginator = Paginator(posts, PAGE_SIZE)

    current_doucuments_page_number = request.GET.get("page", 1)
    try:
        current_doucuments_page_number = int(current_doucuments_page_number)
    except ValueError:
        print("Error: 'page' is not an integer")
        current_doucuments_page_number = 1

    # forum_paginator = paginator.get_page(current_doucuments_page_number)

    current_page_index = []
    for index in range(PAGE_SIZE):
        current_page_index.append(
            (current_doucuments_page_number - 1) * PAGE_SIZE + index + 1
        )

    return render(
        request,
        "pages/documents.html",
        context={
            "page_name": "documents",
            # "documents_paginator": doucuments_paginator,
            "current_page_index": current_page_index,
        },
    )


def upload_document_view(request):

    return render(
        request,
        "pages/upload_document.html",
        context={
            "page_name": "upload_document",
        },
    )


def detail_document_view(request):

    return render(
        request,
        "pages/detail_document.html",
        context={
            "page_name": "detail_document",
        },
    )


def forum_view(request):

    # TODO: add get post in forum

    # posts = Post.objects.order_by("-date_published").prefetch_related(
    #     "translations"
    # )

    PAGE_SIZE = 8
    # paginator = Paginator(posts, PAGE_SIZE)

    current_forum_page_number = request.GET.get("page", 1)
    try:
        current_forum_page_number = int(current_forum_page_number)
    except ValueError:
        print("Error: 'page' is not an integer")
        current_forum_page_number = 1

    # forum_paginator = paginator.get_page(current_forum_page_number)

    current_page_index = []
    for index in range(PAGE_SIZE):
        current_page_index.append(
            (current_forum_page_number - 1) * PAGE_SIZE + index + 1
        )

    return render(
        request,
        "pages/forum.html",
        context={
            "page_name": "forum",
            # "forum_paginator": forum_paginator,
            "current_page_index": current_page_index,
        },
    )


def detail_forum_view(request):

    return render(
        request,
        "pages/detail_forum.html",
        context={
            "page_name": "detail_forum",
        },
    )


def add_forum_view(request):

    return render(
        request,
        "pages/add_forum.html",
        context={
            "page_name": "add_forum",
        },
    )



def news_view(request):
    posts = Post.objects.order_by("-date_published").prefetch_related(
        "translations"
    )

    PAGE_SIZE = 8
    paginator = Paginator(posts, PAGE_SIZE)

    current_news_page_number = request.GET.get("page", 1)
    try:
        current_news_page_number = int(current_news_page_number)
    except ValueError:
        print("Error: 'page' is not an integer")
        current_news_page_number = 1

    news_paginator = paginator.get_page(current_news_page_number)

    current_page_index = []
    for index in range(PAGE_SIZE):
        current_page_index.append(
            (current_news_page_number - 1) * PAGE_SIZE + index + 1
        )

    return render(
        request,
        "pages/news.html",
        context={
            "page_name": "news",
            "posts": posts,
            "news_paginator": news_paginator,
            "current_page_index": current_page_index,
        },
    )


def detail_news_view(request, post_id):
    posts = Post.objects.order_by("-date_published").prefetch_related(
        "translations"
    )
    post = get_object_or_404(Post, pk=post_id)

    NUMBER_RELATED_NEWS = 4
    NUMBER_NEWS_TAGS = 3

    news_tags = post.tags.all()[:NUMBER_NEWS_TAGS]
    related_news = posts.exclude(pk=post_id)[:NUMBER_RELATED_NEWS]

    return render(
        request,
        "pages/detail_news.html",
        context={
            "page_name": "detail_news",
            "post": post,
            "news_tags": news_tags,
            "related_news": related_news,
        },
    )


def profile_view(request):

    return render(
        request,
        "pages/profile.html",
        context={
            "page_name": "profile",
        },
    )


def update_profile_view(request):

    return render(
        request,
        "pages/update_profile.html",
        context={
            "page_name": "update_profile",
        },
    )
