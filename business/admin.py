from django import forms
from django.contrib import admin
from .models import Faculty, Department, Course, YearlyPQ


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'faculty')
    list_filter = ('faculty', 'department')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            # Get the selected A object from the request
            a_id = request.POST.get('faculty') or request.GET.get('faculty')
            if a_id:
                # Filter the B objects based on the selected A object
                kwargs['queryset'] = Department.objects.filter(faculty_id=a_id)
            else:
                # If no A object is selected, show all B objects
                kwargs['queryset'] = Department.objects.all()
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class YearlyPQAdmin(admin.ModelAdmin):
    list_display = ('course_year', 'department', 'faculty')
    list_filter = ('faculty', 'department',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'department':
            # Get the selected A object from the request
            a_id = request.POST.get('faculty') or request.GET.get('faculty')
            if a_id:
                # Filter the B objects based on the selected A object
                kwargs['queryset'] = Department.objects.filter(faculty_id=a_id)
            else:
                # If no A object is selected, show all B objects
                kwargs['queryset'] = Department.objects.all()
                
        elif db_field.name == 'course':
            # Get the selected A object from the request
            b_id = request.POST.get('department') or request.GET.get('department')
            if b_id:
                # Filter the B objects based on the selected A object
                kwargs['queryset'] = Course.objects.filter(department_id=b_id)
            else:
                # If no A object is selected, show all B objects
                kwargs['queryset'] = Course.objects.all()
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
            
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course, CourseAdmin)
admin.site.register(YearlyPQ, YearlyPQAdmin)



