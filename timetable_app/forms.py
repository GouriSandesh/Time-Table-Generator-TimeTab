from django import forms

from timetable_app.models import Course, Subject, Staff


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"



class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"



class CourseSelectionForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        label='Select Courses'
    )

