from django.db import models


class Operation(models.Model):
    op_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
