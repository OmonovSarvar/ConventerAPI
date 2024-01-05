from django.urls import path, include

from .views import TextView, DocxLatinAPIView, DocxCyrillicAPIView

urlpatterns = [
    path('', TextView.as_view(), name='text'),
    path('docx/latin', DocxLatinAPIView.as_view(), name='docx-latin'),
    path('docx/cyrillic', DocxCyrillicAPIView.as_view(), name='docx-cyrillic'),
]
