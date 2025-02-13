from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
            help_text=_('Latitude coordinate for squirrel sighting point'),
            )
    longitude = models.FloatField(
            help_text=_('Longitude coordinate for squirrel sighting point'),
            )
    unique_id = models.CharField(
            max_length =50, 
            help_text=_('Identification tag for each squirrel sighting'),
            )
    
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            )
    
    shift = models.CharField(
            max_length =5,
            choices = SHIFT_CHOICES,
            help_text=_('Sighting occurred in the morning or late afternoon'),
            )

    date = models.CharField(
            max_length =8,
            help_text=_('Concatenation of the sighting session day and month'),
            )
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            )
    
    age= models.CharField(
            max_length =50,
            choices = AGE_CHOICES,
            help_text=_('Value is either Adult or Juvenile'),
            )
    COLOR_CHOICES = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            )
    primary_fur_color= models.CharField(
            max_length =50,
            choices= COLOR_CHOICES,
            help_text=_('Value is either "Gray," "Cinnamon" or "Black."'),
            )
    LOCATION_CHOICES = (
            (GROUND_PLANE , 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            )
    location = models.CharField(
            max_length=50,
            choices=LOCATION_CHOICES,
            help_text=_('Location of where the squirrel was when first sighted'),
            )
    specific_location = models.CharField(
            max_length=300,
            help_text=_('Additional commentary on the squirrel location'),
            )
    quaas = models.BooleanField(
            help_text=_('Whether the squirrel was heard quaaing'),
            )
    moans = models.BooleanField(
            help_text=_('Whether the squirrel was heard moaning'),
            )
    tail_flags = models.BooleanField(
            help_text=_('Whether the squirrel was seen flagging its tail'),
            )
    tail_twitches = models.BooleanField(
            help_text=_('Whether the squirrel was seen twitching its tail'),
            )
    approaches = models.BooleanField(
            help_text=_('Whether the squirrel was seen approaching human, seeking foodl'),
            )
    indifferent = models.BooleanField(
            help_text=_('Whether the Squirrel was indifferent to human presence'),
            )
    runs_from = models.BooleanField(
            help_text=_('Whether the Squirrel was seen running from humans, seeing them as a threat'),
            )

  



# Create your models here.
