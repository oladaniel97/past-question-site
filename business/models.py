from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=225)
    
    class Meta:
        
        verbose_name_plural = 'Faculties'
    

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='faculty', on_delete = models.CASCADE)
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    faculty = models.ForeignKey(Faculty, null=True, blank=True,on_delete = models.CASCADE)
    department = models.ForeignKey(Department, related_name='department', on_delete = models.CASCADE)
    name = models.CharField(max_length = 225)
    
    
    # @property
    # def faculty(self):
    #     return self.department.faculty

    def __str__(self):
        return f" {self.name}"

class YearlyPQ(models.Model):
    faculty = models.ForeignKey(Faculty, null=True, blank=True,on_delete = models.CASCADE)
    department = models.ForeignKey(Department,null=True, blank=True, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, related_name='course',on_delete = models.CASCADE)
    year = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True)
    
    def course_year(self):
        return f"{self.course} {self.year}"
    
    def __str__(self):
        return f"{self.course} {self.year}"