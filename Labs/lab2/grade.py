class GradeEntry:
    """
    A student grade entry record system at U of T.
    Each grade entry is identified by their course identifier, course weight, and course grade which can be letter grade or numeric grade.

    === Attributes ===
    :@type course: str
        course that identify the course for GradeEntry
    :@type weight: float
        weight for this course
    """
# grade not implemented yet.
    def __init__(self, course_id='', weight=0.0):
        """
        Create an empty Grade
        """
        self.course_id = course_id
        self.weight = weight
        # only grade unique to numeric or letter value
        #self._set_grade()


# setter
    #def _set_course_id(self, course_id):
        #"""
        #Set GradeEntry self's course id

        #:@rtype: None
        #"""
        self._course_id = course_id

    #def _set_weight(self, weight):
        #"""
        #Set GradeEntry self's weight for the course

        #@rtype: None
        #"""
        #self._weight = weight

    #def _set_grade(self):
        #self._grade = -1
        #raise NotImplementedError("Set grade entry in subclass")

# getter
    #def _get_course_id(self):
        #return self._course_id

    #def _get_weight(self):
        #return self._weight

    #def _get_grade(self):
        #return self._weight

# property
    #course_id = property(_get_course_id, _set_course_id)
    #weight = property(_get_weight, _set_weight)
    #grade = property(_get_grade)


# attributes
    def __eq__(self, other):
        """
        Determine if a GradeEntry self is equivalent to GradeEtry other

        :@type self: a GradeEntry
        :@param other: another GradeEntry
        :@type other: GradeEntry
        :@return whether course, grade, and weight are the same as of the other GradeEntry
        :@rtype: bool
        """
        # check type first
        # list has order
        #return (type(self) == type(other) and
         #       self.course_id == other.course_id and
          #      self.grade == other.grade)
        raise NotImplementedError("Subclass needed")

    def __str__(self):
        """
        Produce a user-friendly string representation of GradeEntry self.

        :@return: string representation of GradeEntry self
        :@rtype: str

        """
        #return 'Course: {}, Grade: {}'.format(self.course, self.grade)
        raise NotImplementedError("Subclass needed")

    def grade_points(self):
        """
        A grade entry must also be able to generate how many poits it is worth, based on its grade.The details of how points are generated are left out here and implemented in subclasses.

        :@rtype: float
        """
        raise NotImplementedError("Set grade entry in subclass")

class NumericGradeEntry(GradeEntry):
    """
    A numeric grade entry is a grade entry for which the grade is an integer between 0 and 100 (inclusive)
    === Attributes ===
    :param int numeric_grade: an integer between 0 and 100 (inclusive)
    """
    def __init__(self, course_id, weight, numeric_grade=0):
        """
        Initializes a numeric grade entry for a give course.

        Extends GradeEntry.__init__

        :@param numeric_grade: an integer for the numeric grade
        :@type numeric_grade: int
        """

        # Extend on GradeEntry by borrowing its elements
        super().__init__(course_id, weight)
        self.grade = numeric_grade

    # implement error check
    # setter
    def _set_grade(self, numeric_grade=0):
        """
        Set a numeric grade int to NumericGradeEntry self
        @param numeric_grade: int
        @rtype: None
        """
        if numeric_grade < 0 or numeric_grade > 100:
            raise Exception("Not valid numeric grade!")
        else:
            self._grade = int(numeric_grade)

    # getter
    def _get_grade(self):
        """
        Return the numeric grade of NumericGradeEntry self.
        @type self: NumericGradeEntry
        @rtype: int

        >>> NumericGradeEntry('csc148', 1.0, 95)._get_grade()
        95
        """
        return self._grade

    # property
    grade = property(_get_grade, _set_grade)

    # attributes
    def __str__(self):
        """
        Return a string representing NumericGradeEntry self.

        Overrides GradeEntry.__str__

        @return: string representation of NumericGradeEntry self
        @rtype: str
        >>> print(NumericGradeEntry("csc148", 1.0, 79))
        Course: csc148, weight: 1.0, grade: 79
        """
        return 'Course: {}, weight: {}, grade: {}'.format(
            self.course_id,
            self.weight,
            self.grade)

    def __eq__(self, other):
        """
        Determine if a NumericGradeEntry self is equivalent to NumericGradeEntry other.

        :@type self: a NumericGradeEntry
        :@param other: another Numeric Grade Entry
        :@type other: NumericGradeEntry
        :@return: whether course_id, weight, and numeric grades of NumericGradeEntry self is the same as of the other NumericGradeEntry
        :@rtype: bool

        >>> nge1 = NumericGradeEntry("csc148", 1.0, 79)
        >>> nge2 = NumericGradeEntry("csc148", 2.0, 79)
        >>> nge3 = NumericGradeEntry("csc148", 1.0, 79)
        >>> nge1 == nge2
        False
        >>> nge1 == nge3
        True
        """
        # always check type first
        # can also make it look like tupple which looks nicer
        return (type(self) == type(other) and
                self.course_id == other.course_id and
                self.weight == other.weight and
                self.grade == other.grade)

    def grade_points(self):
        """
        Return the grade points based on the numeric grade entered.

        Overrides GradeEntry.grade_points
        @rtype: float
        >>> mygrade = NumericGradeEntry("csc148", 1.0, 100)
        >>> mygrade.grade_points()
        4.0
        """
        category = {
            4.0: [85, 100],
            3.7: [80, 84],
            3.3: [77, 79],
            3.0: [73, 76],
            2.7: [70, 72],
            2.3: [67, 69],
            2.0: [63, 66],
            1.7: [60, 62],
            1.3: [57, 59],
            1.0: [53, 56],
            0.7: [50, 52],
            0.0: [0, 49]
        }
        for key, (low, high) in category.items():
            if low <= self.grade <= high:
                return key

category = {'A+': 4.0,'A':4.0,'A-':3.7,
            'B+':3.3,'B':3.0,'B-':2.7,
            'C+':2.3,'C':2.0,'C-':1.7,
            'D+':1.3,'D':1.0,'D-':0.7,
            'F':0.0}

class LetterGradeEntry(GradeEntry):
    """
    A letter grade entry is a grade entry for which the grade is a character. The value of the grade is one of {A,B,C,D,F}, with a possible suffix from {+,-}.


    === Attributes ===
    :@param str letter_grade: a string representing grades
    """


    def __init__(self, course_id, weight, letter_grade=''):
        """
        Initializes a letter grade engry for a given course.

        Extends GradeEntry.__init__

        :@param letter_grade: a string for the letter grade
        :@type letter_grade: str
        """
        # call parent init
        super().__init__(course_id, weight)
        self.grade = letter_grade

        # implement error check
        # setter
    def _set_grade(self, letter_grade=''):
        """
        Set a letter grade str to LetterGradeEntry self

        @param letter_grade: str
        @rtype: None
        """
        if letter_grade in category.keys():
            self._grade = letter_grade
        else:
            raise Exception("Not a valid letter grade!")

    # getter
    def _get_grade(self):
        """
        Return the letter grade of LetterGradeEntry self.

        :@type self: LetterGradeEntry
        :@rtype: str

        >>> LetterGradeEntry('csc148',1.0,'A+')._get_grade()
        'A+'
        """
        return self._grade

    # property
    grade = property(_get_grade, _set_grade)

    def __str__(self):
        """
        Return a string representing LetterGradeEntry self.

        Overrides GradeEntry.__str__

        @return: string representation of LetterGradeEntry self
        @rtype: str
        >>> print(LetterGradeEntry("csc148", 1.0, 'A-'))
        Course: csc148, weight: 1.0, grade: A-
        """
        return 'Course: {}, weight: {}, grade: {}'.format(self.course_id,
                                                          self.weight,
                                                          self.grade)
    def __eq__(self, other):
        """
        Determine if a LetterGradeEntry self is equivalent to LetterGradeEntry other.


        :@type self: a LetterGradeEntry
        :@param other: another Letter Grade Entry
        :@type other: LetterGradeEntry
        :@return: whether course_id, weight, and letter grades of LetterGradeEntry self is the same as of the other LetterGradeEntry
        :@rtype: bool

        >>> lge1 = LetterGradeEntry("csc148", 1.0, "B")
        >>> lge2 = LetterGradeEntry("csc165", 1.0, "B")
        >>> lge3 = LetterGradeEntry("csc148", 1.0, "B")
        >>> lge1 == lge2
        False
        >>> lge1 == lge3
        True
        """

        return ((type(self) == type(other)) and
                (self.course_id, self.weight, self.grade) ==
                (other.course_id, other.weight, other.grade))

    def grade_points(self):
        """
        Return the grade points based on the letter grade entered.

        Overrides GradeEntry.grade_points

        @rtype: float

        >>> mygrade = LetterGradeEntry("csc148", 1.0, "A")
        >>> mygrade.grade_points()
        4.0
        """
        return category[self.grade]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
