def average_grade(roster):
    sum = 0
    for student in roster:
        sum += student.get_grade()
    return sum / len(roster)
   
