import random

from timetable_app.constants import PERIODS_PER_DAY, DAYS


def generate_timetable(selected_course):
    timetable = {}

    # Ensure selected_course is a valid Course object
    course_subjects = list(selected_course.subjects.all())
    course_staff = {subject: list(subject.staff.all()) for subject in course_subjects}

    # Initialize an empty timetable for each day and period
    course_timetable = {day: [None] * PERIODS_PER_DAY for day in DAYS}

    for day in DAYS:
        for period in range(PERIODS_PER_DAY):
            assigned = False

            # Shuffle subjects for random assignment
            random.shuffle(course_subjects)
            for subject in course_subjects:
                available_staff = [s for s in course_staff[subject] if s.is_available(timetable.get(day, []), day, period)]

                if available_staff:
                    # Randomly choose an available staff member
                    staff_member = random.choice(available_staff)

                    # Assign the subject and staff to the timetable slot
                    course_timetable[day][period] = {
                        "subject": subject,
                        "staff": staff_member,
                    }

                    assigned = True
                    break  # Break out once assigned to avoid multiple assignments

            if not assigned:
                print(f"No available staff for {selected_course} on {day} period {period}")

    # Return the course timetable directly
    return course_timetable
