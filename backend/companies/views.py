from rest_framework import viewsets

from .models import Company
from .permissions import IsOwnerOrReadOnly
from .serializers import CompanyListSerializer, CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyListSerializer
        return CompanySerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    