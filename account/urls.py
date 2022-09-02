from django.urls import path

from account.views import AccountViewSet

urlpatterns = [
    path('load_accounts/', AccountViewSet.as_view(actions={'post': 'load_accounts'})),
    path('', AccountViewSet.as_view(actions={'get': 'list'}))
]
