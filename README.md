# Time-Table-Generator-TimeTab
The project, Time Table Generator [TimeTab], is a web application developed using the Python Django Framework.

The application manage courses, subjects, staff, and generate a timetable.The user can input the data of the college/university which is required to generate the timetable.
The user must add the following details:
1.Teachers
2.Courses
3.Subjects

Upon successfull entry of the data into sqlite database, the user can navigate to the "Generate Timetable" page to start the process of generating the timetable.
This automatically generate a timetable (for each course, in day(column)/period(day) format) that assigns subjects to periods randomly, ensuring:
■ No staff availability conflicts.
■ Subjects are well-placed throughout the week.

Technologies Used:
1.HTML5 
2.CSS
3.Python 3.11.5
4.Django 5.1.2
5.JavaScript
6.sqlite3

NB: Leveraged the structure of QuickStart – Free Bootstrap 5 Business Website Template from "ThemeWagon" to create the landing page.
