from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateApiView, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
# router.register(r"", UserViewSet, basename="users")
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    # path('', include(router.urls)),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshSlidingView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
