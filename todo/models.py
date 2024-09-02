from django.db import models


# todos model
class Todos(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    class Meta:
        managed = False # SO THAT DJANGO DON T DELETE OR ADD TODOS TABLE
        db_table = 'todos'


    def __str__(self) -> str:
        return self.content