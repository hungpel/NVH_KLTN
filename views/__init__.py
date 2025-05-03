from .add_request import AddRequestPage
from .couple_friend import CoupleFriendPage
from .document.detail import DetailDocumentPage
from .document.list import DocumentListView
from .document.upload import UploadDocumentPage
from .forum import AddForumPage, DetailForumPage, ForumPage
from .home import HomePage
from .login import SignIn
from .news import DetailNewsPage, NewsPage
from .profile import MyRequestPage, ProfilePage, UpdateProfilePage
from .register import SignUp
from .send_request import SendRequestPage
from .welcome import WelcomePage
from .room import ChatRoomDetailPage

__all__ = [
    "ChatRoomDetailPage",
    "SignIn",
    "WelcomePage",
    "SignUp",
    "CoupleFriendPage",
    "HomePage",
    "ProfilePage",
    "SendRequestPage",
    "DetailNewsPage",
    "NewsPage",
    "AddForumPage",
    "DetailForumPage",
    "ForumPage",
    "DetailDocumentPage",
    "UploadDocumentPage",
    "UpdateProfilePage",
    "DocumentListView",
    "MyRequestPage",
    "AddRequestPage",
]
