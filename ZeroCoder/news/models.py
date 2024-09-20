from django.db import models


class News_post(models.Model):
    title = models.CharField('News title', max_length=50)
    short_description = models.CharField('Short news description', max_length=200)
    text = models.TextField('News text')
    pub_date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News post'
        verbose_name_plural = 'News'
