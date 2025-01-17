

import sys
sys.path.append("..")

from PySide6 import QtCore, QtGui, QtWidgets


import sys
sys.path.append("..")

from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         PropertiesBinWidget,
                         NodeTreeWidget,
                         setup_context_menu)

# import example nodes from the "example_nodes" package
from example_nodes import basic_nodes, widget_nodes

def draw_triangle_port(painter, rect, info):
    """
    Custom paint function for drawing a Triangle shaped port.

    Args:
        painter (QtGui.QPainter): painter object.
        rect (QtCore.QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    size = int(rect.height() / 2)
    triangle = QtGui.QPolygonF()
    triangle.append(QtCore.QPointF(-size, size))
    triangle.append(QtCore.QPointF(0.0, -size))
    triangle.append(QtCore.QPointF(size, size))

    transform = QtGui.QTransform()
    transform.translate(rect.center().x(), rect.center().y())
    port_poly = transform.map(triangle)

    # mouse over port color.
    if info['hovered']:
        color = QtGui.QColor(14, 45, 59)
        border_color = QtGui.QColor(136, 255, 35)
    # port connected color.
    elif info['connected']:
        color = QtGui.QColor(195, 60, 60)
        border_color = QtGui.QColor(200, 130, 70)
    # default port color
    else:
        color = QtGui.QColor(*info['color'])
        border_color = QtGui.QColor(*info['border_color'])

    pen = QtGui.QPen(border_color, 1.8)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawPolygon(port_poly)

    painter.restore()


def draw_square_port(painter, rect, info):
    """
    Custom paint function for drawing a Square shaped port.

    Args:
        painter (QtGui.QPainter): painter object.
        rect (QtCore.QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    # mouse over port color.
    if info['hovered']:
        color = QtGui.QColor(14, 45, 59)
        border_color = QtGui.QColor(136, 255, 35, 255)
    # port connected color.
    elif info['connected']:
        color = QtGui.QColor(195, 60, 60)
        border_color = QtGui.QColor(200, 130, 70)
    # default port color
    else:
        color = QtGui.QColor(*info['color'])
        border_color = QtGui.QColor(*info['border_color'])

    pen = QtGui.QPen(border_color, 1.8)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawRect(rect)

    painter.restore()

graph = None

def init_ai_node_menu(graph, nodes):
    root_menu = graph.get_context_menu('graph')
    node_menu = root_menu.add_menu('&Node')
    #node_menu = graph.context_nodes_menu()

    for node in nodes:
        node_menu.add_command(node.NODE_NAME, create_ai_node,node.NODE_NAME)
        #node_menu.add_command(node.NODE_NAME, create_node, node_class=node)

def create_ai_node(graph,action):
    print(action.text())
    graph.create_node('com.chantasticvfx.' + action.text())

class GAINode(BaseNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GAINode'
    def __init__(self):
        super(GAINode, self).__init__()
        self.set_color(25, 58, 51)

        #self.add_input('SkillID', color=(200, 10, 0))
        self.add_input('TitleIn', multi_input=False, display_name=False,
                  color=(255, 10, 0), data_type='Title', painter_func=draw_square_port)
        self.add_output('TitleOut', multi_output=True, display_name=False,
                    color=(255, 10, 0), data_type='Title', painter_func=draw_square_port)

class GAIBase(BaseNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GAIBase'
    def __init__(self):
        super(GAIBase, self).__init__()
        self.set_color(25, 58, 51)
        self.add_output('TitleOut', multi_output=True, display_name=False,
                    color=(60, 255, 0), data_type='Title', painter_func=draw_square_port)

class GRoot(GAIBase):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GRoot'
    def __init__(self):
        super(GRoot, self).__init__()
        self.set_color(58, 255, 51)


class GStage(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GStage'
    def __init__(self):
        super(GStage, self).__init__()
        self.set_color(25, 58, 51)
        self.add_text_input("condition", 'stage condition', tab='widgets')


class GParaller(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GParaller'
    def __init__(self):
        super(GParaller, self).__init__()
        self.set_color(25, 58, 51)


class GSelector(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GSelector'
    def __init__(self):
        super(GSelector, self).__init__()
        self.set_color(25, 58, 51)

class GRandomor(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GRandomor'
    def __init__(self):
        super(GRandomor, self).__init__()
        self.set_color(25, 58, 51)

class GSequence(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GSequence'
    def __init__(self):
        super(GSequence, self).__init__()
        self.set_color(25, 58, 51)



class GDoAction(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GDoAction'
    def __init__(self):
        super(GDoAction, self).__init__()
        self.set_color(25, 58, 51)
        self.add_text_input('LogicID', 'ligic id', tab='widgets')
        self.add_text_input('DataID', 'logic data id', tab='widgets')

class GIdle(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GIdle'
    def __init__(self):
        super(GIdle, self).__init__()
        self.add_text_input('Time', 'time idle', tab='widgets')

class GRandomPos(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GRandomPos'
    def __init__(self):
        super(GRandomPos, self).__init__()
        self.set_color(25, 58, 51)
        self.add_text_input('radius', 'random radius', tab='widgets')

class GMoveToTarget(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GMoveToTarget'
    def __init__(self):
        super(GMoveToTarget, self).__init__()
        self.set_color(25, 58, 51)
        self.add_text_input('BuffID', 'buff id', tab='widgets')

class GRandomTarget(GAINode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GRandomTarget'
    def __init__(self):
        super(GRandomTarget, self).__init__()
        self.set_color(25, 58, 51)
        self.add_text_input('radius', 'random radius', tab='widgets')