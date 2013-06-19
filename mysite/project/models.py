from django.db import models
from django.forms import ModelForm

# Create your models here.
class Student_info(models.Model):
	Roll_Number = models.IntegerField(primary_key=True)
	def __unicode__(self):
		return u'%s' %(self.Roll_Number)
	Name = models.CharField(max_length=200)
	BRANCH_CHOICES=(
			('IT','IT'),
			('CSE', 'CSE'),
			('ECE','ECE'),
			('CE','CE'),
			('PE','PE'),
			('ME','ME'),
			('EE','EE'),
		)
	Branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
	Father_name=models.CharField(max_length=100)
	Date_of_birth=models.DateField()
	#image = models.ImageField(upload_to='photos/%Y/%m/%d')
	
class Certificate(models.Model):
	
	student_info = models.ForeignKey(Student_info)
	def __unicode__(self):
		return u'%s' %(self.student_info)
	dmc_number= models.IntegerField()
	RECEIVED_CHOICES=(
			('NO','NO'),
			('YES','YES'),
		)
	Received=models.CharField(max_length=5, default="NO", choices=RECEIVED_CHOICES)
	SEMESTER_CHOICES=(
			('1','1'),
			('2','2'),
			('3','3'),
			('4','4'),
			('5','5'),
			('6','6'),
			('7','7'),
			('8','8'),
		)
	Semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES)
	
	Year_of_passing = models.IntegerField()
	Obtained_marks=models.IntegerField()
	Maximum_marks = models.IntegerField()

class Student_infoForm(ModelForm):
   class Meta:
      model = Student_info
      
class CertificateForm(ModelForm):
	class Meta:
		model=Certificate
