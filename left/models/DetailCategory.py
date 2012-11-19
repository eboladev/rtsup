# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Категория узла
class DetailCategory(models.Model):
    name  = models.CharField(max_length=s.NODE_CATEGORY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'detail_category'
    


class Handler( ModelResource ):
    class Meta:
        queryset = DetailCategory.objects.all()
        resource_name = 'detail_category'

    filtering = {
        'id'     : ALL,
        'name'   : ALL,
    }
