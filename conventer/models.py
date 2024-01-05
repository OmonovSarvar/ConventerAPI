from django.db import models


class TextModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class TxtModel(models.Model):
    txt = models.FileField(upload_to='txt_files', max_length=254)

    def __str__(self):
        return self.txt


class DocxModel(models.Model):
    docx_file = models.FileField(upload_to='docx_files', max_length=254)


