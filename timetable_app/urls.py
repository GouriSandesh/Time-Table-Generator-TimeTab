from django.urls import path

from timetable_app import views


urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('courseView',views.courseView,name="courseView"),
    path('addCourse',views.addCourse,name="addCourse"),
    path('updateCourse /<int:id>/',views.updateCourse,name="updateCourse"),
    path('delCourse /<int:id>/',views.delCourse,name="delCourse"),
    path('subjectView', views.subjectView, name="subjectView"),
    path('addSubject', views.addSubject, name="addSubject"),
    path('updateSubject /<int:id>/', views.updateSubject, name="updateSubject"),
    path('delSubject /<int:id>/', views.delSubject, name="delSubject"),
    path('staffView', views.staffView, name="staffView"),
    path('addStaff', views.addStaff, name="addStaff"),
    path('updateStaff /<int:id>/', views.updateStaff, name="updateStaff"),
    path('delStaff /<int:id>/', views.delStaff, name="delStaff"),

    path('generate_timetable', views.generate_timetable, name="generate_timetable"),
    path('generate_timetable_view', views.generate_timetable_view, name="generate_timetable_view"),

]