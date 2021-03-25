class Tree:

    class _Node:

        def __init__(self, element, children):
            self._element = element
            self._children = children

        def get_height(self):
            if self._children.is_empty():
                return 0
            else:
                child_heights = []
                for child in self._children:
                    child_heights.append(child.get_height)
                height = max(child_heights) + 1
                return height

    def __init__(self):
        self._root = None

    def insert(self,
               node: _Node = None,
               as_child_of: _Node = None):
        if as_child_of is None:
            # insert new node as root
            node._children = self._root._children

    def calculate_node_heights(self, node=None):
        if node is None:
            node = self._root

        if node._children.is_empty():
            return 0

        child_heights = []
        for child in node._children:
            child_heights.append(self.calculate_node_heights(node=child))
        height = max(child_heights) + 1

        return height
