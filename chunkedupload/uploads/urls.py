from django.urls import path
from uploads.routers import CommonRouter
from django.urls import include

urlpatterns = [
    path("", include(CommonRouter.urls)),
]
