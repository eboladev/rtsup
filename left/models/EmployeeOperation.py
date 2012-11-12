# -*- coding: utf-8 -*-

from django.db import models

# Операции с сотрудниками
class EmployeeOperation(models.Model):
    date        = models.DateField()
    type        = models.ForeignKey('EmployeeOperationType')
    employee    = models.ForeignKey('Employee')
    department  = models.ForeignKey('Department')
        
    class Meta:
        app_label = 'left'
        db_table = 'v_employee_operation'
    
    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return