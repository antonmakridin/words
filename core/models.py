from django.db import models

class Words(models.Model):
    slovo = models.CharField(max_length=200, verbose_name='Слово')
    perevod = models.CharField(max_length=200, verbose_name='Перевод')
    is_active = models.BooleanField(default=False, verbose_name='Изучено')

    # чтобы отображались красивые названия в админке
    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.slovo