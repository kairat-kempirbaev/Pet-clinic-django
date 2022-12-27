from django.urls import path
from graphene_django.views import GraphQLView

from . import views
from rest_framework import routers
from .views import *
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
] + [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
