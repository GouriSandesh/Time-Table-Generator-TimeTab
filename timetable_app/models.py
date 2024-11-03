from django.db import models

class Course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_desc = models.TextField()

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="subjects")

    def __str__(self):
        return self.subject_name


class Staff(models.Model):
    staff_id = models.IntegerField()
    staff_name = models.CharField(max_length=25)
    subject = models.ManyToManyField(Subject, related_name="staff", blank=True)


    def __int__(self):
        return self.staff_name


    def is_available(self, timetable, day, period):
        """Check if the staff member is available on a specific day and period."""
        for entry in timetable:
            if entry['day'] == day and entry['period'] == period and entry['staff'] == self:
                return False
        return True


