from django.db import models

class Task(models.Model):
    description = models.CharField(verbose_name='Задача', max_length=3000, null = False, blank=False)
    status = models.CharField(verbose_name='Статус', max_length=12)
    deadline_date = models.DateField(verbose_name='Deadline', auto_now_add=False, auto_now=False, blank = True, null = False)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        return f'Task: {self.description}, Status: {self.status}, deadline: {self.deadline_date}'