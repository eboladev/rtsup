# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Типы операций с оборудованием
class EquipmentOperationType(models.Model):
    name  = models.CharField(max_length=s.EQ_OPER_TYPE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_operation_type'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EquipmentOperationType
    fields = ('id', 'name')
    