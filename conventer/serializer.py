from rest_framework.serializers import ModelSerializer, Serializer, FileField

from .models import TxtModel, DocxModel


class DocxSerializer(ModelSerializer):
    class Meta:
        model = DocxModel
        fields = ['docx_file']


class TxtFileSerializer(ModelSerializer):
    class Meta:
        model = TxtModel
        fields = ['txt']
