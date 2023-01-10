from rest_framework import mixins, viewsets


class GetPostDeleteViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass
