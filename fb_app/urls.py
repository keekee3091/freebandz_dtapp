from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, CategoryViewSet, AccountViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls
