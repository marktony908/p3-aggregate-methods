class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        self.__class__.all.append(self)

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def add_enrollment(self, enrollment):
        if not isinstance(enrollment, Enrollment):
            raise Exception("Must be an instance of Enrollment.")
        self._enrollments.append(enrollment)

    def course_count(self):
        return len(self._enrollments)

    def add_grade(self, enrollment, grade):
        if enrollment not in self._enrollments:
            raise Exception("Enrollment not found for this student.")
        self._grades[enrollment] = grade

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        if num_courses == 0:
            return 0  # Avoid division by zero
        average_grade = total_grades / num_courses
        return average_grade


class Course:
    def __init__(self, name):
        self.name = name
