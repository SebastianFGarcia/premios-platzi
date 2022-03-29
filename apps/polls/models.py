from datetime import timedelta,timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField("Pregunta", max_length=250)
    pub_date = models.DateTimeField("Fecha Publicación",auto_now=True)
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)
    class Meta:
        verbose_name="Pregunta"
        verbose_name_plural = "Preguntas"

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField("Elección",max_length=250)
    votes = models.IntegerField("Votos",default=0)
    
    def __str__(self):
        return self.choice_text
    
    class Meta:
        verbose_name="Elección"
        verbose_name_plural="Elecciones"
        