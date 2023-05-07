from rest_framework import routers

from uploads.views import ChunkedUploadApiViewSet


class BaseRouter(routers.SimpleRouter):
    """Base Router class to be inherited by all Router classes."""

    def extend(self, extended_router=None):
        if extended_router:
            self.registry.extend(extended_router.registry)  # noqa


CommonRouter = BaseRouter()
CommonRouter.register("api", ChunkedUploadApiViewSet, basename="chunk")
