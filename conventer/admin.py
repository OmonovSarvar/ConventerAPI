from django.contrib import admin

from conventer.models import TxtModel, TextModel, DocxModel

# Register your models here.
admin.site.register(TxtModel)
admin.site.register(TextModel)
admin.site.register(DocxModel)
