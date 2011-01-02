from django.db import models

class ZoneParameter(models.Model):
    title = models.CharField(max_length=255)
    
    def __unicode__(self):
        return '%s' % self.title


class KindZone(models.Model):
    title = models.CharField(max_length=255)
    zoneparameters = models.ManyToManyField(ZoneParameter, related_name = 'zoneparameters')
    #staticvisualizations = models.ManyToManyField(ZoneParameter,through='StaticVisualization')
        
    def __unicode__(self):
        return '%s' % self.title
    
class StaticVisualization(models.Model):
    kindzone = models.ForeignKey(KindZone)
    zoneparameter = models.ForeignKey(ZoneParameter)
    
    def __unicode__(self):
        return '%s - %s' % (self.kindzone.title,self.zoneparameter.title)    


class Entity(models.Model):
        
   #user = models.ForeignKey(User)
   name = models.CharField(max_length=200)
   description = models.TextField(blank=True)
   city = models.CharField(max_length=300)
   province = models.CharField(max_length=2)
   cap = models.IntegerField(max_length=5,blank=True)
   phone = models.CharField(max_length=20)
   referent = models.CharField(max_length=200)
   referent_phone = models.CharField(max_length=20,blank=True)
   #dressing_room = models.BooleanField()
   #shower = models.BooleanField()
   #image = models.ImageField(upload_to='tmp_image/%s' % str(user),null=True)
   kindzones = models.ManyToManyField(KindZone,through='PlayZone')
        
   def __unicode__(self):
       return self.name
    
class PlayZone(models.Model):
    
    
    
    entity = models.ForeignKey(Entity)
    kindzone = models.ForeignKey(KindZone)
    number = models.IntegerField("Numero",null=True)
    #books = models.ManyToManyField(User)
    #cover = models.BooleanField("Al coperto",default=False)
    #illumination = models.BooleanField("Illuminazione",default=False)
    limit_players_number = models.IntegerField("Limite giocatori",blank=True,null=True)
    cost_per_hour = models.IntegerField("Costo all'ora")
    note = models.TextField("note",blank=True,null=True)
    #audiance = models.BooleanField("Spazio spettatori",default=False)
    #file = models.FileField(upload_to = 'file')
    
    def __unicode__(self):
        return str(self.plexus) + ': ' + str(self.KIND_CHOICES[self.kind][1])

    
