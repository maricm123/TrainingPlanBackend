from django.urls import path
from .views import TrainingPlanList, TrainingPlanDetail

app_name = 'trainingPlan'

urlpatterns = [
    path('plan/<int:pk>', TrainingPlanDetail.as_view(), name='trainingPlanDetail'),
    path('plan/', TrainingPlanList.as_view(), name='trainingPlanList'),
    
]