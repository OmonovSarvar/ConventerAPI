from mediafiles.docx_files.for_docx import docx_convert_to_latin
from .for_text import text_convert_to_latin, text_convert_to_cyrillic
from .serializer import DocxSerializer

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView


class DocxLatinAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocxSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            yolak = serializer.data['docx_file']
            yolak = str(yolak)
            print(yolak)
            yolak = yolak.replace("/media/docx_files/", "")
            response = docx_convert_to_latin(yolak)
            return Response({
                "result": response
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DocxCyrillicAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocxSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TextView(APIView):
    def post(self, request):
        context = request.data['context']
        pattern = request.data['pattern']
        if pattern == 'latin':
            response = text_convert_to_latin(context)
        elif pattern == 'cyrillic':
            response = text_convert_to_cyrillic(context)
        else:
            return Response({
                "Message": "Wrong Input",
                "You can choose only": "cyrillic or latin"
            })

        return Response({
            "result": f"{response}"
        })
