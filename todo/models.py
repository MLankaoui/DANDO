from django.db import models


# todos model
class Todos(models.Model):
    content = models.CharField(max_length=100, null=False)
    class Meta:
        managed = True
        db_table = 'todos'


    def __str__(self) -> str:
        return self.content