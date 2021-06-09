#!/usr/bin/python
from NodeGraphQt.constants import (NODE_LAYOUT_VERTICAL,
                                   NODE_LAYOUT_HORIZONTAL)
from NodeGraphQt.base.node import NodeObject
from NodeGraphQt.nodes.base_node import BaseNode
from NodeGraphQt.qgraphics.node_group import (GroupNodeItem,
                                              GroupNodeVerticalItem)


class GroupNode(BaseNode):
    """
    The ``NodeGraphQt.GroupNode`` class extends from the
    :class:``NodeGraphQt.BaseNode`` class with the ability to nest other nodes
    inside of it.

    **Inherited from:** :class:`NodeGraphQt.BaseNode`
    """

    NODE_NAME = 'Group'

    def __init__(self, qgraphics_views=None):
        qgraphics_views = qgraphics_views or {
            NODE_LAYOUT_HORIZONTAL: GroupNodeItem,
            NODE_LAYOUT_VERTICAL: GroupNodeVerticalItem
        }
        super(GroupNode, self).__init__(qgraphics_views)
        self._children = set()
    #     self._input_port_nodes = {}
    #     self._output_port_nodes = {}
    #
    # def add_input(self, name='input', multi_input=False, display_name=True,
    #               color=None, locked=False, painter_func=None):
    #     super(GroupNode, self).add_input(name=name,
    #                                      multi_input=multi_input,
    #                                      display_name=display_name,
    #                                      color=color,
    #                                      locked=locked,
    #                                      painter_func=painter_func)
    #     self._input_port_nodes[name] = None
    #
    # def add_output(self, name='output', multi_output=True, display_name=True,
    #                color=None, locked=False, painter_func=None):
    #     super(GroupNode, self).add_output(name=name,
    #                                       multi_output=multi_output,
    #                                       display_name=display_name,
    #                                       color=color,
    #                                       locked=locked,
    #                                       painter_func=painter_func)
    #     self._output_port_nodes[name] = None

    def children(self):
        return list(self._children)

    def add_chid(self, node):
        self._children.add(node)

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)

    def expand(self):
        return

    def collapse(self):
        return