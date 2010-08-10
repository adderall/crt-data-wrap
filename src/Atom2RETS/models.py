from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    link = models.URLField()

    def __unicode__(self):
        return self.title
       
    def get_absolute_url(self):
    	return self.link
    
