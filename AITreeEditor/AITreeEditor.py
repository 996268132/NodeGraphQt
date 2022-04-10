#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


from PySide6 import QtCore, QtGui, QtWidgets

import AINodes as Nodes

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
        Nodes.GRoot,Nodes.GStage,Nodes.GParaller,Nodes.GSelector,Nodes.GRandomor,Nodes.GSequence,Nodes.GDoAction,
        Nodes.GIdle,Nodes.GRandomTarget,Nodes.GMoveToTarget,
        #BackdropNode
        #basic_nodes.FooNode,
        #basic_nodes.BarNode,
        #widget_nodes.DropdownMenuNode,
        #widget_nodes.TextInputNode,
        #widget_nodes.CheckboxNode
    ]
    graph.register_nodes(nodes_to_reg)

    #Nodes
    Nodes.init_ai_node_menu(graph, nodes_to_reg)
    Nodes.graph = graph
    graph.fit_to_selection()
    graph.widget.setWindowTitle("AITreeEditor")
    app.exec_()
