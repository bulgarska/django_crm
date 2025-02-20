from django.urls import path
from .views import (HomeView, RecordDetailView, RecordDeleteView)

urlpatterns = [
	path('', HomeView.as_view(), name='crm-home'),
 	path('record/<int:pk>', RecordDetailView.as_view(), name='record-detail'),
  	path('record/<int:pk>/delete', RecordDeleteView.as_view(), name='record-delete'),
 
]
