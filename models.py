from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=False)


class Option(models.Model):
    value = models.CharField(max_length=100)
    is_correct = models.BooleanField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)


class QuizSession(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    is_open = models.BooleanField()
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()

