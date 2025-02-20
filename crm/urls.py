from django.urls import path
from .views import (HomeView, RecordDetailView)

urlpatterns = [
	path('', HomeView.as_view(), name='crm-home'),
 	path('record/<int:pk>', RecordDetailView.as_view(), name='record-detail'),
 
]
