class VerboseList(list):
    """A subclass of list that provides verbose output for certain methods"""

    def append(self, item):
        """Override append method to provide verbose output"""
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, iterable):
        """Override extend method to provide verbose output"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items")

    def remove(self, item):
        """Override remove method to provide verbose output"""
        print(f"Removed {item} from the list")
        super().remove(item)

    def pop(self, index=-1):
        """Override pop method to provide verbose output"""
        item = self[index]
        print(f"Popped {item} from the list")
        return super().pop(index)
