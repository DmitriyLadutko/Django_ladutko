from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, related_name='student')
    contact_info = models.OneToOneField('ContactInfo', null=True, related_name='student', on_delete=models.SET_NULL)
    diary = models.OneToOneField('Diary', null=True, related_name='student', on_delete=models.SET_NULL)
    hobbies = models.ManyToManyField('Hobby', related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


class Group(models.Model):
    serial_number_group = models.CharField(max_length=4)
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)

    def __str__(self):
        return f'{self.serial_number_group}'


class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f'student phone: {self.phone} student address :{self.address}'


class Diary(models.Model):
    average_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.average_score}'


class Hobby(models.Model):
    name_of_hobby = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'{self.name_of_hobby}'


class Book(models.Model):
    name = models.CharField(max_length=255, default=None)
    number_of_pages = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} {self.number_of_pages}'


class StudentBook(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cw_22_student_book'
        unique_together = ['student', 'book']
