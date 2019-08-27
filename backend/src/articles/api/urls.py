# from django.urls import path

# from .views import (
#     ArticleListview,
#     ArticleDetailView,
#     ArticleCreateView,
#     ArticleUpdateView,
#     +
#     ArticleDeleteView

# )
# urlpatterns = [

#     path('', ArticleListview.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),
#     path('<pk>/update', ArticleUpdateView.as_view()),
#     path('<pk>/delete', ArticleDeleteView.as_view())
# ]


from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls
