from rest_framework import viewsets, mixins


class GetPostDeleteViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass
