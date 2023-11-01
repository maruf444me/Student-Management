from django.db import models


# ============================================================
#                    Model For Students
# ============================================================
class StudentDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_image')
    department = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    cgpa = models.FloatField(max_length=4)
    grade = models.CharField(max_length=5)
# ===================== End Model ============================


# ============================================================
# Teacher Verifyin Process Model
# ============================================================
class TeacherVerify(models.Model):
    school_name = models.CharField(max_length=100)
    pin = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.school_name

# ===================== End Model ============================