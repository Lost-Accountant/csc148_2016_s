class LinkedListNode:
    """
    Node to be used in linked list

    === Public Attributes ===
    :@param LinkedListNode next_: successor to this LinkedListNode
    :@param object value: data this LinkedListNode represents
    """
    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        :@param value: data of this linked list node
        :@type value: object
        :@param next_: successor to this LinkedListNode.
        :@type next_: LinkedListNode|None
        :@rtype: None
        """
        self.value = value
        self.next_ = next_
