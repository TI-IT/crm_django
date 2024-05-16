from django.db import models

class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=255)
    description = models.TextField('Описание', max_length=1000, )
    is_completed = models.BooleanField('Выполнено', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title