class Registry:
    """A registry of runners in a 5K race.  Each runner is identified by
    their email address and is registered in a speed category.

    === Attributes ===
    @param dict groups: runners grouped by category
    """

    # The names of the speed CATEGORIES for a race.
    CATEGORIES = ['<20', '<30', '<40', '>=40']

    def __init__(self):
        """ (Registry) -> NoneType

        Initialize a new race registry with no runners entered.
        """
        self.groups = {}
        for c in Registry.CATEGORIES:
            self.groups[c] = []

    def __eq__(self, other):
        """
        Return whether Registry self is equivalent to other.

        @param Registry self: this Registry
        @param object|Registry other: object to compare to self
        @rtype: bool
        """
        return (type(self) == type(other) and
                self.groups == other.groups)

    def registered_in(self, e):
        """
        Return the category that the runner with email address e is
        registered in, or the empty string if no one with that email
        address is already registered.

        @param Registry self: this Registry
        @param str e: runner's email

        >>> r = Registry()
        >>> r.register('Diane', '<20')
        >>> r.registered_in('Phantom')
        ''
        >>> r.registered_in('Diane')
        '<20'
        >>>
        """
        for c in Registry.CATEGORIES:
            if e in self.groups[c]:
                return c
        return ""

    def register(self, e, c):
        """
        Register a runner with email address e and category c.  If they had
        previously registered, remove them from their old category and
        register them in category c.  c must occur in CATEGORIES.

        @param Registry self: this Registry
        @param str e: runner's email
        @param str c: runner's speed category
        @rtype: None
        """
        old_category = self.registered_in(e)
        if old_category:
            self.groups[old_category].remove(e)
        self.groups[c].append(e)

    def category_roster(self, c):
        """
        Return a list of the email addresses of all the runners registered
        in category c.  c must occur in CATEGORIES.

        @param Registry self: this Registry
        @param str c: speed category
        @rtype: list[str]

        >>> r = Registry()
        >>> r.register('a', '<20')
        >>> r.register('b', '<20')
        >>> r.register('c', '<40')
        >>> r.category_roster('<20')
        ['a', 'b']
        >>> r.category_roster('<30')
        []
        """
        return self.groups[c]

    def __str__(self):
        """
        Return a str describing this Registry, suitable for a user to read.

        @param Registry self: this Registry
        @rtype: str

        >>> r = Registry()
        >>> r.register("a", "<20")
        >>> r.register("b", "<20")
        >>> r.register("c", "<40")
        >>> print(r)
        Runners with speed category <20:
            a
            b
        Runners with speed category <30:
            None
        Runners with speed category <40:
            c
        Runners with speed category >=40:
            None
        <BLANKLINE>
        """
        answer = ""
        for (speed, runners) in sorted(self.groups.items()):
            answer += 'Runners with speed category %s:\n' % speed
            if runners:
                for r in runners:
                    answer += '    %s\n' % r
                    # Remove the final newline character.
                    # answer = answer[:-1]
            else:
                answer += "    None\n"
        return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
