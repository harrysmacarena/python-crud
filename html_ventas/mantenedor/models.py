from django.db import models
from django.core.serializers import serialize

# Create your models here.
class Persona(models.Model):
    run = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=50)
    apePaterno = models.CharField(max_length=50, db_column='ape_paterno')
    apeMaterno = models.CharField(max_length=50, db_column='ape_materno')
    imagen = models.CharField(max_length=150)
    #created_at = models.DateTimeField('date published')
    #updated_at = models.DateTimeField('date published')
    #def serialize(self):
    #    return serialize("json", [self], fields=['auto_increment_id','user','component','booked']) 
    class Meta:
        db_table = 'croe_persona'
        #fields = ['id', 'title', 'code', 'linenos', 'language', 'style']   

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Region(models.Model):
    id_region =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, db_column='nombre')
    class Meta:
        db_table = 'croe_region'

class Provincia(models.Model):
    id_provincia =models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=200, db_column='nombre')
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')
    class Meta:
        db_table = 'croe_provincia'

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=200, db_column='nombre')
    stImagen = models.CharField(max_length=200)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='id_provincia')
    #def __str__(self):
    #    return f"{self.id_comuna},{self.nombre_comuna},{self.stImagen}"
    #def serialize(self):
    #    return serialize("json", [self], fields=['id_comuna','nombre_comuna','stImagen'])
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    class Meta:
        db_table = 'croe_comuna'    
"""    
    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.    
"""