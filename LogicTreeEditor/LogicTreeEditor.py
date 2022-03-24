#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


from PySide6 import QtCore, QtGui, QtWidgets

import LogicNodes as Nodes

# import example nodes from the "example_nodes" package
from example_nodes import basic_nodes, widget_nodes


import sys
sys.path.append("..")
from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         PropertiesBinWidget,
                         NodeTreeWidget,
                         setup_context_menu)






if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication([])

    # create node graph.
    graph = NodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph)

    # widget used for the node graph.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()


    # show the properties bin when a node is "double clicked" in the graph.
    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)
    def show_prop_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()
    graph.node_double_clicked.connect(show_prop_bin)


    # show the nodes list when a node is "double clicked" in the graph.
    node_tree = NodeTreeWidget(node_graph=graph)
    def show_nodes_list(node):
        if not node_tree.isVisible():
            node_tree.update()
            node_tree.show()
    graph.node_double_clicked.connect(show_nodes_list)


    # registered nodes.
    nodes_to_reg = [
        Nodes.GSkill,Nodes.GCreateBullet,Nodes.GSkillMove,Nodes.GDoDamage,Nodes.GDelay,
        Nodes.GAddBuff,Nodes.GCreateNpc,
        #BackdropNode
        #basic_nodes.FooNode,
        #basic_nodes.BarNode,
        #widget_nodes.DropdownMenuNode,
        #widget_nodes.TextInputNode,
        #widget_nodes.CheckboxNode
    ]
    graph.register_nodes(nodes_to_reg)

    #Nodes
    Nodes.init_node_menu(graph, nodes_to_reg)
    Nodes.graph = graph

    '''
    skill_node = graph.create_node('com.chantasticvfx.GSkill')

    createBullet_node = graph.create_node('com.chantasticvfx.GCreateBullet')
    damage_node = graph.create_node('com.chantasticvfx.GDoDamage')
    skillmove_node = graph.create_node('com.chantasticvfx.GSkillMove')
    delay_node = graph.create_node('com.chantasticvfx.GDelay')

    # change node icon.
    this_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(this_path, '../example_nodes', 'pear.png')
    skill_node.set_icon(icon)

    # connect the nodes.
    #skill_node.set_output(0, createBullet_node.input(0))
    #createBullet_node.set_input(0, damage_node.input(0))
    skill_node.set_output(0, createBullet_node.input(0))
    skill_node.set_output(0, skillmove_node.input(0))
    skillmove_node.set_output(0, damage_node.input(0))
    
    

    # auto layout nodes.
    graph.auto_layout_nodes()

    # wrap a backdrop node.
    backdrop_node = graph.create_node('nodeGraphQt.nodes.BackdropNode')
    backdrop_node.wrap_nodes([createBullet_node, damage_node])
    '''
    graph.fit_to_selection()
    graph.widget.setWindowTitle("LogicTreeEditor")
    app.exec_()
