from django.urls import path
from .views import (HomeView, RecordDetailView, RecordDeleteView, 
                    RecordCreateView, RecordUpdateView)

urlpatterns = [
	path('', HomeView.as_view(), name='crm-home'),
 	path('record/<int:pk>', RecordDetailView.as_view(), name='record-detail'),
  	path('record/<int:pk>/delete', RecordDeleteView.as_view(), name='record-delete'),
	path('record/create', RecordCreateView.as_view(), name='record-create'),
 	path('record/<int:pk>/update', RecordUpdateView.as_view(), name='record-update'),
 
]
