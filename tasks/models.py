from django.db import models  # type: ignore


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
