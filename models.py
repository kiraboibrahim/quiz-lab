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
    
class Student(models.Model):  
    first_name =models.CharField(max_length=25) 
    last_name = models.CharField(max_length=25) 
    registrationNumber =models.CharField(max_length=20,unique=True)
    gender = models.CharField(max_length=10,choices=[('M','Male'),('F','Female')])
    contact = models.CharField(max_length=25)
    course_id = models.ForeignKey(Course ,on_delete=models.CASCADE)
    

class Question(models.Model):
    quiz= models.ForeignKey(Quiz,on_delete= models.CASCADE,related_name='questions') 
    text =models.TextField()
       
    

class QuizAttempt(models.Model) :
    session =models.ForeignKey(QuizSession,on_delete=models.CASCADE)   
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    quiz =models.ForeignKey(Quiz,on_delete=models.CASCADE)
    student =models.ForeignKey(Student,on_delete=models.CASCADE)
    option_chosen = models.ForeignKey(Option ,on_delete=models.CASCADE,null=True,blank=True)
    
 
    

