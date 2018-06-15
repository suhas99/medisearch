from __future__ import unicode_literals

from django.db import models,forms

#from .managers import Staff

# Create your models here.


class Address(models.Model):
	line_1 = models.CharField(max_length=128, null=True)
	line_2 = models.CharField(max_length=128, null=True)
	city = models.CharField(max_length=128, null=True)
	state = models.CharField(max_length=128, null=True)
	lat = models.FloatField(default=float(-185))
	lng = models.FloatField(default=float(-185))

	def __unicode__(self):
	 return self.line_1
  
class MedicalShop(models.Model):
	name = models.CharField(max_length=256, null=False, blank=False)
	phone = models.CharField(max_length=13, null=True, blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)
##class Medtypeid1(models.Model):
  ##medtype_id = models.IntegerField(default=1, null=False,blank= False, editable=True)
  ##med_type = models.CharField(max_length=200,default='Not_Valid')

class Type(models.Model):
  medtype_id =models.IntegerField(null=False,blank=False)
  med_type=models.CharField(max_length=2000)
  if medtype_id == 1 :
   med_type = 'tablets'
  elif medtype_id == 2 :
   med_type = 'ointments'
  elif medtype_id == 3 :
   med_type = 'tonics'
  elif medtype_id == 4 :
   med_type = 'cosmetics'
  else:# medtype_id == 5 :
   med_type = 'others'  

  ##print(med_type)
  def __unicode__(self):
   return str(self.medtype_id)
  def Type1():
    #return Type1.medtype_id
   return Type.med_type
  

