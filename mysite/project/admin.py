from project.models import Student_info
from django.contrib import admin
from project.models import Certificate
class Student_infoAdmin(admin.ModelAdmin):
	list_display = ('Roll_Number', 'Name','Branch') 
	search_fields=['Roll_Number']
	
class CertificateAdmin(admin.ModelAdmin):
	list_display=('dmc_number','Semester','Year_of_passing','Obtained_marks','Maximum_marks','Received')
	
admin.site.register(Student_info, Student_infoAdmin)
admin.site.register(Certificate,CertificateAdmin)

