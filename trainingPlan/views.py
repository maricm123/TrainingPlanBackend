from django.shortcuts import render
from rest_framework import generics
from .models import Plan, Category
from .serializers import PlanSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

# Custom permission
class TrainingPlanUserWritePermissions(BasePermission):
    message = "Editting is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
            # have permission just user that made that object
        return obj.coach == request.user

class TrainingPlanList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class TrainingPlanDetail(generics.RetrieveUpdateDestroyAPIView, TrainingPlanUserWritePermissions):
    permission_classes = [TrainingPlanUserWritePermissions]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer