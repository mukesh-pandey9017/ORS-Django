from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login_id = models.EmailField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=50, default='')
    mobilenumber = models.CharField(max_length=50, default='')
    role_Id = models.IntegerField()
    role_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.firstName + '_' + self.lastName

    class Meta:
        db_table = 'sos_user'


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'ORS_ROLE'


class College(models.Model):
    collegeName = models.CharField(max_length=50)
    collegeAddress = models.CharField(max_length=50)
    collegeState = models.CharField(max_length=50)
    collegeCity = models.CharField(max_length=20)
    collegePhoneNumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'ORS_COLLEGE'


class Course(models.Model):
    courseName = models.CharField(max_length=50)
    courseDescription = models.CharField(max_length=100)
    courseDuration = models.CharField(max_length=100)

    class Meta:
        db_table = 'ORS_COURSE'


class Marksheet(models.Model):
    rollNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'ORS_MARKSHEET'


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    mobileNumber = models.CharField(max_length=20)
    email = models.EmailField()
    college_ID = models.IntegerField()
    collegeName = models.CharField(max_length=50)

    class Meta:
        db_table = 'ORS_STUDENT'


class Subject(models.Model):
    SubjectName = models.CharField(max_length=50)
    SubjectDescription = models.CharField(max_length=50)
    Course_ID = models.IntegerField()
    courseName = models.CharField(max_length=50)

    class Meta:
        db_table = 'ORS_SUBJECT'


class Faculty(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    college_ID = models.IntegerField()
    collegeName = models.CharField(max_length=50)
    subject_ID = models.IntegerField()
    subjectName = models.CharField(max_length=50)
    course_ID = models.IntegerField()
    courseName = models.CharField(max_length=50)

    class Meta:
        db_table = 'ORS_FACULTY'


class TimeTable(models.Model):
    examTime = models.CharField(max_length=40)
    examDate = models.DateField()
    subject_ID = models.IntegerField()
    subjectName = models.CharField(max_length=50)
    course_ID = models.IntegerField()
    courseName = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    class Meta:
        db_table = 'ORS_TIMETABLE'

