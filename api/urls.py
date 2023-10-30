from django.urls import path,include
from .views import article_list, article_detail,ArticleAPIView,ArticleViewSets,GenericAPIView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSets, basename='article')

urlpatterns=[
    path('viewsets/',include(router.urls)),
    path('viewsets/<int:pk>/',include(router.urls)),
    #path('article/',article_list),
    path('article/',ArticleAPIView.as_view()),
    #path('detail/<int:pk>/',article_detail),
    # path('detail/article/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view())

]