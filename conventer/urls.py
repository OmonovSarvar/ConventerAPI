from django.urls import path, include

from .views import TextView, DocxLatinAPIView, DocxCyrillicAPIView, TxtLatinAPIView, TxtCyrillicAPIView

urlpatterns = [
    path('', TextView.as_view(), name='text'),
    path('docx/latin', DocxLatinAPIView.as_view(), name='docx-latin'),
    path('docx/cyrillic', DocxCyrillicAPIView.as_view(), name='docx-cyrillic'),
    path('txt/latin', TxtLatinAPIView.as_view(), name='txt-latin'),
    path('txt/cyrillic', TxtCyrillicAPIView.as_view(), name='txt-cyrillic'),
    path('migration', views.migration, name='migration')
]
