# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Статус заявки
class TaskState(models.Model):
    name  = models.CharField(max_length=s.TASK_STATE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'task_state'
    
