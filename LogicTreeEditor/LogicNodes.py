

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

def init_node_menu(graph, nodes):
    root_menu = graph.get_context_menu('graph')
    node_menu = root_menu.add_menu('&Node')
    for node in nodes:
        node_menu.add_command(node.NODE_NAME, create_node,'')

def create_node(graph):
    pass

class GNode(BaseNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GNode'
    def __init__(self):
        super(GNode, self).__init__()
        self.set_color(25, 58, 51)

        #self.add_input('SkillID', color=(200, 10, 0))
        self.add_input('TitleIn', multi_input=False, display_name=False,
                  color=(255, 10, 0), data_type='Title', painter_func=draw_square_port)
        self.add_output('TitleOut', multi_output=True, display_name=False,
                    color=(255, 10, 0), data_type='Title', painter_func=draw_square_port)

class GSkill(BaseNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GSkill'
    def __init__(self):
        super(GSkill, self).__init__()
        self.set_color(25, 58, 51)

        #self.add_input('SkillID', color=(200, 10, 0))
        self.add_output('TitleOut', multi_output=True, display_name=False,
                        color=(255, 10, 0), data_type='Title', painter_func=draw_square_port)
        self.add_output('SkillID')
        self.add_output('SkillStaTime')
        self.add_output('SkillEndTime')

class GCreateBullet(GNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GCreateBullet'
    def __init__(self):
        super(GCreateBullet, self).__init__()
        self.set_color(25, 58, 51)
        self.add_input('BulletID')
        self.add_text_input('BulletID', 'bullet id', tab='widgets')


class GSkillMove(GNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GSkillMove'
    def __init__(self):
        super(GSkillMove, self).__init__()
        self.set_color(25, 58, 51)
        self.add_input("X")
        self.add_input("Y")
        self.add_input("Z")


class GDoDamage(GNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GDoDamage'
    def __init__(self):
        super(GDoDamage, self).__init__()
        self.set_color(25, 58, 51)
        self.add_input('SkillID')

class GDelay(GNode):
    __identifier__ = 'com.chantasticvfx'
    NODE_NAME = 'GDelay'
    def __init__(self):
        super(GDelay, self).__init__()
        self.add_text_input('Time', 'time delay', tab='widgets')
