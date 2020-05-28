class GradeEntry:
    """
    The base class for a grade entry in a course.

    This is an abstract class, not intended for instantiating objects
    directly.

    === Public Attributes ===
    :param str course_id: the course identifier
    :param float weight: 1.0 credits for a half-course
    """

    def __init__(self, course_id="", weight=0.0):
        """
        Initializes a grade entry for a given course.

        :param course_id: a course identifier
        :type course_id: str
        :param weight:: 1.0 credits for a half-course,
            2.0 credits for a full course
        :type weight: float
        """
        self.course_id, self.weight = course_id, weight

    def __eq__(self, other):
        """
        Return whether GradeEntry self is equivalent to other.

        :param other: object to compare to GradeEntry self
        :type other: object | GradeEntry
        :rtype: bool
        """
        raise NotImplementedError("Subclass needed")

    def __str__(self):
        """
        Return a str representation of this GradeEntry.

        :rtype: str
        """
        raise NotImplementedError("Subclass needed")

    def grade_points(self):
        """
        A grade entry can generate how many points it is worth, based on
        its grade. The details of how points are generated are left out
        here and implemented in subclasses.

        :rtype: float
        """
        raise NotImplementedError("Subclass needed")


class NumericGradeEntry(GradeEntry):
    """
    A subclass of GradeEntry that represents a numeric grade entry.

    === Public Attributes ===
    :param int grade: numerical grade in this course
    """

    def __init__(self, course_id, weight, grade=0):
        """
        Initializes an object representing a numeric grade entry.

        Extends GradeEntry.__init__

        :param grade: grade in this course
        :type grade: int
        """
        super().__init__(course_id, weight)
        if grade > 100 or grade < 0:
            raise Exception('Invalid grade.')
        else:
            self.grade = grade

    def __str__(self):
        """
        Return a string representing NumericGradeEntry self.

        Overrides GradeEntry.__str__

        :rtype: str

        >>> print(NumericGradeEntry("csc148", 1.0, 79))
        Course: csc148, weight: 1.0, grade: 79
        """
        return "Course: {}, weight: {}, grade: {}".format(self.course_id,
                                                          self.weight,
                                                          self.grade)

    def __eq__(self, other):
        """
        Return whether NumericGradeEntry self is equivalent to other.

        Overrides GradeEntry.__eq__

        :param other: object to compare to self
        :type other: object |NumericGradeEntry
        :rtype: bool

        >>> nge1 = NumericGradeEntry("csc148", 1.0, 79)
        >>> nge2 = NumericGradeEntry("csc148", 2.0, 79)
        >>> nge3 = NumericGradeEntry("csc148", 1.0, 79)
        >>> nge1 == nge2
        False
        >>> nge1 == nge3
        True
        """
        return (type(self) == type(other) and
                (self.grade, self.weight, self.course_id) ==
                (other.grade, other.weight, other.course_id))

    def grade_points(self):
        """
        Returns the point value corresponding to this object's numeric
        grade.

        Overrides GradeEntry.grade_points

        :rtype: float

        >>> mygrade = NumericGradeEntry("csc148", 1.0, 100)
        >>> mygrade.grade_points()
        4.0
        """
        if self.grade >= 90:
            points = 4.0
        elif self.grade >= 85:
            points = 4.0
        elif self.grade >= 80:
            points = 3.7
        elif self.grade >= 77:
            points = 3.3
        elif self.grade >= 73:
            points = 3.0
        elif self.grade >= 70:
            points = 2.7
        elif self.grade >= 67:
            points = 2.3
        elif self.grade >= 63:
            points = 2.0
        elif self.grade >= 60:
            points = 1.7
        elif self.grade >= 57:
            points = 1.3
        elif self.grade >= 53:
            points = 1.0
        elif self.grade >= 50:
            points = 0.7
        else:
            points = 0.0
        return points


# global dictionary that maps each letter grade to its point
# representation according to specs.txt
GRADE_TO_POINTS = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                   'B-': 2.7,
                   'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3,
                   'D': 1.0, 'D-': 0.7, 'F': 0.0}


class LetterGradeEntry(GradeEntry):
    """
    A subclass of GradeEntry that represents a letter grade entry.

    === Public Attributes ===
    :param str grade: grade in this course
    """

    def __init__(self, course_id, weight, grade=''):
        """
        Initializes an object representing a numeric grade entry.

        :param grade: grade in this course
        :type grade: str
        """
        super().__init__(course_id, weight)
        if grade not in GRADE_TO_POINTS:
            raise Exception("Invalid grade.")
        else:
            self.grade = grade

    def __str__(self):
        """
        Return a str representation of LetterGradeEntry self.

        Overrides GradeEntry.__str__

        :rtype: str

        >>> print(LetterGradeEntry("csc148", 1.0, "A"))
        Course: csc148, weight: 1.0, grade: A
        """
        return "Course: {}, weight: {}, grade: {}".format(self.course_id,
                                                          self.weight,
                                                          self.grade)

    def __eq__(self, other):
        """
        Return whether LetterGradeEntry is equivalent to other.

        Overrides GradeEntry.__eq__

        :param other: object to compare to self
        :type other: object|LetterGradeEntry
        :rtype: bool

        >>> lge1 = LetterGradeEntry("csc148", 1.0, "B")
        >>> lge2 = LetterGradeEntry("csc165", 1.0, "B")
        >>> lge3 = LetterGradeEntry("csc148", 1.0, "B")
        >>> lge1 == lge2
        False
        >>> lge1 == lge3
        True
        """
        return (type(self) == type(other) and
                (self.course_id, self.weight, self.grade) ==
                (other.course_id, other.weight, other.grade))

    def grade_points(self):
        """
        Returns the point value corresponding to this object's letter
        grade.

        Overrides GradeEntry.grade_points

        :rtype: float

        >>> mygrade = LetterGradeEntry("csc148", 1.0, "A")
        >>> mygrade.grade_points()
        4.0
        """
        return GRADE_TO_POINTS[self.grade]
