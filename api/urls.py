from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, ConnectTicketViewSet, LikeViewSet

router = DefaultRouter()
router.register(r"comment", CommentViewSet, basename="comment")
router.register(r"like", LikeViewSet, basename="like")
router.register(r"connect", ConnectTicketViewSet, basename="connect_ticket")
urlpatterns = router.urls
