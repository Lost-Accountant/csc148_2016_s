class registry:
    """
    a race registery defined by each runners' email address,
    and their speed category.

    The registry itself is not a dictionary.
    The "group" element is a dictionary within a class of registry

    Attributes:
        @param dict groups: runners grouped by speed category
    ===========


    >>> race = registry()
    >>> race = registry.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
    >>> race = registry.enroll('tom@mail.utoronto.ca', 'under 30 minutes')
    """
    # The names of each category
    category = ['under 20 minutes',
                'under 30 minutes',
                'under 40 minutes',
                '40 minutes or over']


    def __init__(self):
        """
        Create a new registry with an empty dictionary based on given groups
        (Reigstry) -> NoneType

        @param registry self: this registry
        """

        self.groups = {}
        for each in self.category:
            self.groups[each] = []

        return

    def __str__(self):
        """
        Return a user-friendly string representation of the registry in table.
        @param: registry self: this registry
        @rtype: str

        >>> race = registry()
        >>> race.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
        >>> race.enroll('tom@mail.utoronto.ca', 'under 30 minutes')
        >>> print(race)
        40 minutes or over:
            None
        under 40 minutes:
            gerhard@mail.utoronto.ca
        under 3o mintues:
            tom@mail.utoronto.ca
        under 20 minutes:
            None
        """
        result = ''
        for group in self.groups:
            result += "{}:\n".format(group)
            for runner in self.groups[group]:
                result += "     {}\n".format(runner)

        return result

    def __eq__(self, other):
        """
        Return whether this race registry is the same as the other.
        @param registry self: this registry
        @param registry | Any other: another registry
        @rtype: bool
        >>> race = registry()
        >>> race.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
        >>> match = registry()
        >>> match.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
        >>> game = registry()
        >>> game.enroll('tom@mail.utoronto.ca', 'under 30 minutes')
        >>> race == match
        True
        >>> race == game
        False
        """
        return (type(self) == type(other)) and (self.groups == other.groups)

    def enroll(self, email, time):
        """
        Enroll a runner to the registry with email and speed category.

        @param registry self: this registry
        @param str email: the email address of the runner
        @param str time: the speed category of the runner
        @rtype: None
        >>> race = registry()
        >>> race.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
        """
        # check whether exists in the registry already
        for group in self.groups:
            if email in self.groups[group]:
                self.groups[group].remove(email)

        self.groups[time].append(email)
        return

    def is_registered(self, email):
        """
        Return whether a runner is registered in the race and return
        their category

        @param registry self: this registry
        @param email:
        @rtype: str

        >>> race = registry()
        >>> race.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
        >>> print(race.is_registered('gerhard@mail.utoronto.ca'))
        under 40 minutes
        >>> print(race.is_registered('a'))
        None
        """
        for group in self.groups:
            if email in self.groups[group]:
                return group
            else:
                return None


if __name__ == '__main__':
    race = registry()
    race.enroll('gerhard@mail.utoronto.ca', 'under 40 minutes')
    race.enroll('tom@mail.utoronto.ca', 'under 30 minutes')
    race.enroll('toni@mail.utoronto.ca', 'under 20 minutes')
    race.enroll('margot@mail.utoronto.ca', 'under 30 minutes')
    race.enroll('gerhard@mail.utoronto.ca', 'under 30 minutes')
    print(race)
    print(race.is_registered('toni@mail.utoronto.ca'))

