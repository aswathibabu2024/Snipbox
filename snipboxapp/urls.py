from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snipboxapp.views import SnippetViewSet, TagListViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('snippets', SnippetViewSet, basename='snippets')

urlpatterns = [

    path('snipapi/', include(router.urls)),
    path('snipapi/tags/', TagListViewset.as_view({'get': 'list'})),
    path('snipapi/tags/<int:pk>/', TagListViewset.as_view({'get': 'retrieve'})),
    path('snipapi/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('snipapi/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
