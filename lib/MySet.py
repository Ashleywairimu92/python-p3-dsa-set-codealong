class MySet:
    def __init__(self, initial_elements=None):
        """Initialize the set with unique elements from a list."""
        self.dictionary = {}
        if initial_elements:
            for element in initial_elements:
                self.add(element)

    def add(self, element):
        """Add an element to the set."""
        if element not in self.dictionary:
            self.dictionary[element] = True

    def delete(self, element):
        """Delete an element from the set if it exists."""
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        """Check if the element exists in the set."""
        return element in self.dictionary

    def size(self):
        """Return the size of the set."""
        return len(self.dictionary)

    def clear(self):
        """Clear all elements from the set."""
        self.dictionary.clear()

    def __str__(self):
        """Return a string representation of the set."""
        return f'MySet: {{{",".join(map(str, self.dictionary.keys()))}}}'


# Test cases for MySet
class TestSet:

    def test_init(self):
        '''Test __init__ set with list'''
        test_set = MySet([1, 2, 3, 4])
        set_list = [1, 2, 3, 4]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_add(self):
        '''Test add() to set'''
        test_set = MySet([1, 2, 3, 4])
        test_set.add(5)
        set_list = [1, 2, 3, 4, 5]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_delete(self):
        '''Test delete()'''
        test_set = MySet([1, 2, 3, 4])
        test_set.delete(2)
        set_list = [1, 3, 4]
        for num in set_list:
            assert(num in test_set.dictionary)

    def test_has(self):
        '''Test has()'''
        test_set = MySet([1, 2, 3, 4])
        assert(test_set.has(1) == True)
        assert(test_set.has(7) == False)

    def test_size(self):
        '''Test size()'''
        test_set = MySet([1, 2, 3, 4])
        assert(test_set.size() == 4)

    # Bonus tests
    def test_clear(self):
        '''Test clearing set'''
        test_set = MySet([1, 2, 3, 4])
        test_set.clear()
        assert(test_set.size() == 0)

    def test_str(self):
        '''Test __str__()'''
        test_set = MySet([1, 2, 3, 4])
        assert(str(test_set) == 'MySet: {1,2,3,4}')

# Example usage
if __name__ == "__main__":
    tester = TestSet()
    tester.test_init()
    tester.test_add()
    tester.test_delete()
    tester.test_has()
    tester.test_size()
    tester.test_clear()
    tester.test_str()
    print("All tests passed!")

