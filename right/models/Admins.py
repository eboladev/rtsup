# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

# Администратор
class Admins(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'admins'
    
    
    
import Employee
class Handler( ModelResource ):
    employee     = fields.ForeignKey(Employee.Handler, 'employee')
    employee_id  = fields.IntegerField('employee_id')

    class Meta:
        queryset = Admins.objects.all()
        resource_name = 'admins'

    filtering = {
             'id'         : ALL,
             'employee'   : ALL_WITH_RELATIONS,
    }
    