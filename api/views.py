from rest_framework import generics, exceptions
from rest_framework.permissions import IsAuthenticated

from api.models import Projects, Users
from api.paginations import ListPagination
from api.permissions import IsAdminOrOwnerProject
from api.serializers import ProjectSerializer, RegisterSerializer, ProjectCreateSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectCreateSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        query = Projects.objects.all()
        if self.request.user.isProjectManager:
            if self.request.query_params.get('user'):
                query = query.filter(user__username=self.request.query_params.get('user'))
            return query
        else:
            return query.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrOwnerProject]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

    def perform_destroy(self, instance):
        if self.request.user.isProjectManager:
            instance.delete()
        else:
            raise exceptions.PermissionDenied()


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
