from grade import NumericGradeEntry
from grade import LetterGradeEntry

if __name__ == '__main__':
    grades = [NumericGradeEntry('csc148', 1.0, 87),
              NumericGradeEntry('bio150', 2.0, 76),
              LetterGradeEntry('his450', 1.0, 'B+')]
    for g in grades:
        # Use appropriate ??? methods or attributes of g in format
        print("Weight: {}, grade: {}, points: {}".format(g.weight, g.grade, g.grade_points()))

# Use methods or attributes of g to compute weight times points
    total = sum([g.weight * g.grade_points() for g in grades])
        # sum of the list of...
        # ? and ?? are methods or attributes of g
        # using each g in grades
# sum up the credits
total_weight = sum([g.weight for g in grades])
print("GPA = {}".format(total / total_weight))
