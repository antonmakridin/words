from django.db import models

class Words(models.Model):
    slovo = models.CharField(max_length=200, verbose_name='Слово')
    perevod = models.CharField(max_length=200, verbose_name='Перевод')
    is_active = models.BooleanField(default=False, verbose_name='Изучено')

    def unique_error_message(self, model_class, unique_check):
        if unique_check == ('slovo', 'perevod'):
            return "Такая пара уже есть"
        return super().unique_error_message(model_class, unique_check)

    # чтобы отображались красивые названия в админке
    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        unique_together = (( 'slovo', 'perevod'), )

    def __str__(self):
        return self.slovo
    
class Note(models.Model):
    note = models.TextField(verbose_name='Заметка')
    word = models.ForeignKey(
        Words, 
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Пара слов'
    )
    # чтобы отображались красивые названия в админке
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.note