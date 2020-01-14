from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from market import views

# router = routers.DefaultRouter()
# router.register(r'market', views.market_details)

# urlpatterns = [path('admin/', admin.site.urls), path('wm/market_details', 'market_details')]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('wm/market_details/', views.market_details)
    # path('wm/market_details/<int:id>', views.market_details),
]