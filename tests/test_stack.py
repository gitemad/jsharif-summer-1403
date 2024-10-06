import pytest
from stack.stack import Stack

class StackTest:

    def setup_method(self):
        self.st = Stack()

    def test_stack_is_empty(self):
        assert self.st.is_empty()
        assert len(self.st) == 0
        assert repr(self.st) == 'Stack()'
        assert str(self.st) == 'Stack()'
        with pytest.raises(IndexError):
            self.st.pop()

    def test_push_one_item(self):
        self.st.push(2)
        assert not self.st.is_empty()
        assert self.st.top() == 2
        assert repr(self.st) == 'Stack()'
        assert str(self.st) == 'Stack(2)'
    
    @pytest.mark.slow
    def test_push_multiple_items_until_exception_raises(self):
        for i in range(self.st.CAPACITY):
            self.st.push(i)
        assert self.st.is_full()
        with pytest.raises(OverflowError):
            self.st.push(0)
    
    @pytest.mark.parametrize('item', ["3", 4.2, True])
    def test_push_non_integer_item(self, item):
        with pytest.raises(TypeError):
            self.st.push(item)