from django.contrib import admin
 
# add include to the path
from django.urls import path, include
 
# import views from todo

 
# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
 
# create a router object
# router = routers.DefaultRouter()
 
# register the router
# router.register(r'coaches',views.CoachView, 'coach')
# router.register(r'products',views.ProductListView, 'product')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trainingPlan.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='api'))
]

