from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():
    student_roster = []
    student_roster.append(Student("Pandora", 100))
    student_roster.append(Student("Athena", 95))
    student_roster.append(Student("Persephone", 90))
    student_roster.append(Student("Hera", 92))
    student_roster.append(Student("Rhea", 98))
    student_roster.append(Student("Selene", 99))
    student_roster.append(Student("Demeter", 91))
    student_roster.append(Student("Hestia", 89))
    student_roster.append(Student("Artemis", 75))
    student_roster.append(Student("Aphrodite", 82))

    for student in student_roster:
        student.print_student_info()

    print("Average Grade: " + str(average_grade(student_roster)))
