from django.urls import path                        # new
from .views import HomePageView                     # new


urlpatterns = [                                     # new
    path('', HomePageView.as_view(), name='home'),  # new
]
