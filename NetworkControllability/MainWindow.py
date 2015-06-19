from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import networkx as nx
import random
import sys
import NetworkModels as NM

GLOBAL_NETWORK = nx.Graph()

class Dialog_ER(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_ER, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 1, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num

    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_WS(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_WS, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Nearest Neighbors k:', parent=self), 1,0,1,1)
        self.number_of_neighbors = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_neighbors, 1, 1, 1,1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 2, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 2, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num
    def NumberofNeighbors(self):
        (k, ok) = self.number_of_neighbors.text().toInt()
        return k
    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_NW(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_NW, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Nearest Neighbors k:', parent=self), 1,0,1,1)
        self.number_of_neighbors = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_neighbors, 1, 1, 1,1)
        grid.addWidget(QtGui.QLabel('Connection Probability p:', parent=self), 2, 0, 1, 1)
        self.connect_probability = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.connect_probability, 2, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num
    def NumberofNeighbors(self):
        (k, ok) = self.number_of_neighbors.text().toInt()
        return k
    def ConnectProbability(self):
        (prob, ok) = self.connect_probability.text().toFloat()
        return prob

class Dialog_BA(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_BA, self).__init__(parent)
        self.resize(300, 200)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Node Number N:', parent=self), 0, 0, 1, 1)
        self.number_of_nodes = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.number_of_nodes, 0, 1, 1, 1)
        grid.addWidget(QtGui.QLabel('Added Nodes m (m0=m) :', parent=self), 1, 0, 1, 1)
        self.added_nodes_num = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.added_nodes_num, 1, 1, 1, 1)

        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QtGui.QSpacerItem(10, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def NumberofNodes(self):
        (node_num, ok) = self.number_of_nodes.text().toInt()
        return node_num

    def NumberofAddedNodes(self):
        (m, ok) = self.added_nodes_num.text().toInt()
        return m

class Dialog_CentralityDisplayResult(QtGui.QDialog):
    def __init__(self, parent=None, name='title'):
        super(Dialog_CentralityDisplayResult, self).__init__(parent)
        self.resize(400, 500)

        grid = QtGui.QGridLayout()
        
        self.edit = QtGui.QTextEdit(self)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        grid.addWidget(self.edit, 0, 0, 1, 1)
        grid.addWidget(buttonBox, 1, 0, 1, 1)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(grid)
        self.setLayout(layout)
    def add_contents(self, label1, label2, data_col1, data_col2):
        self.edit.append(label1+'\t'+label2)
        n = len(data_col1)
        for i in range(n):
            self.edit.append("%d\t%f"%(data_col1[i], data_col2[i]))


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass




class MyStaticMplCanvas(MyMplCanvas):
    def compute_initial_figure(self):
        G=nx.path_graph(10)
        pos=nx.spring_layout(G)
        nx.draw(G,pos,ax=self.axes)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self.update_figure)
        #timer.start(1000)
        #self.update_figure()
        #self.draw_network()
    def compute_initial_figure(self):
        #self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
        pass

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()
    def draw_network(self, G, pos):
        nx.draw(G,pos,ax=self.axes, with_labels=True, font_color='w')
        #nx.draw_networkx_labels(G, pos, ax=self.axes)
        self.draw()

class MyCentralWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyCentralWidget,self).__init__(parent)     
        self.sc = MyDynamicMplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self) 
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.sc)        
        self.setLayout(layout)
    def update_centralWidget(self, G, pos):
        self.sc.draw_network(G, pos)
        

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('Network Controllability Analysis Software')
        self.resize(1000, 800)
        
        # file menu
        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('Open', self.file_menu_open_action)
        self.file_menu.addAction('Quit', self.file_menu_quit_action)
        self.menuBar().addMenu(self.file_menu)

        # network menu
        self.network_menu = QtGui.QMenu('&Networks', self)
        self.network_menu.addAction('Complete Network', self.network_menu_complete_graph_action)
        self.network_menu.addAction('ER Network', self.network_menu_ERNetwork_action)
        self.network_menu.addAction('Directed ER Network', self.directed_network_menu_ERNetwork_action)
        self.network_menu.addSeparator()
        self.network_menu.addAction('WS Small World', self.network_menu_WSNetwork_action)
        self.network_menu.addAction('Directed WS Small World', self.network_menu_directed_WSNetwork_action)
        self.network_menu.addAction('NW Small World', self.network_menu_NWNetwork_action)
        self.network_menu.addAction('Directed NW Small World', self.network_menu_directed_NWNetwork_action)
        self.network_menu.addSeparator()
        self.network_menu.addAction('BA Scale Free Network', self.network_menu_BANetwork_action)
        self.network_menu.addAction('Directed BA Scale Free Network',self.network_menu_directed_BANetwork_action)
        self.network_menu.addAction('SF Scale Free', self.network_menu_SFNetwork_action)
        self.network_menu.addSeparator()
        self.network_menu.addAction('Karate Club Network', self.network_menu_karate_club_network_action)
        self.menuBar().addMenu(self.network_menu)

        # centrality menu
        self.centrality_menu = QtGui.QMenu('&Centrality', self)
        self.centrality_menu.addAction('Degree Centrality', self.centrality_menu_NodeDegree_action)
        self.centrality_menu.addAction('Betweenness Centrality', self.centrality_menu_NodeBetweenness_action)
        self.centrality_menu.addAction('Closeness Centrality', self.centrality_menu_ClosenessBetweenness_action)
        self.centrality_menu.addAction('Eigenvector Centrality', self.centrality_menu_EigenvectorBetweenness_action)
        self.menuBar().addMenu(self.centrality_menu)

        # controllability menu
        self.controllability_menu = QtGui.QMenu('&Controllability', self)
        self.controllability_menu.addAction('Structral Controllability', self.controllability_menu_StructralControllability_action)
        self.controllability_menu.addAction('Exact Controllability', self.controllability_menu_ExactControllability_action)
        self.menuBar().addMenu(self.controllability_menu)

        # Robustness menu
        self.robustness_menu = QtGui.QMenu('&Robustness', self)
        self.robustness_menu.addAction('Random Attack', self.robustness_menu_RondomAttack_action)
        self.robustness_menu.addAction('Recalculated Max-Degree Attack', self.robustness_menu_RecaculatedMaxDegree_action)
        self.robustness_menu.addAction('Recalculated Max-Betweenness Attack', self.robustness_menu_RecaculatedMaxBetweenness_action)
        self.robustness_menu.addAction('Cascaded Attack based on Node-Capacity', self.robustness_menu_CascadeBasedonNodeCapacity_action)
        self.menuBar().addMenu(self.robustness_menu)

        # about menu
        self.about_menu = QtGui.QMenu('&About', self)
        self.about_menu.addAction('About', self.about_menu_About_action)
        self.menuBar().addMenu(self.about_menu)

        # status bar
        #self.statusbar = QtGui.QStatusBar(self)
        self.statusBar().showMessage(nx.info(GLOBAL_NETWORK))

        # central Widget
        self.main_widget = MyCentralWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        G=nx.path_graph(10)
        pos=nx.spring_layout(G)
        self.main_widget.update_centralWidget(G, pos)
   
    def file_menu_open_action(self):
        pass

    def file_menu_quit_action(self):
        QtGui.qApp.exit()

    ##################################################################
    # 
    # Network Models Definitions
    # 
    ##################################################################
    def network_menu_complete_graph_action(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Node Num N:')
        n = int(text)
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.complete_graph(n)
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_ERNetwork_action(self):
        dialog = Dialog_ER(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.erdos_renyi_graph(n, p)
        pos = nx.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def directed_network_menu_ERNetwork_action(self):
        dialog = Dialog_ER(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.erdos_renyi_graph(n, p, directed=True)
        pos = nx.spectral_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)
    
    def network_menu_WSNetwork_action(self):
        dialog = Dialog_WS(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        k = dialog.NumberofNeighbors()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.watts_strogatz_graph(n, k, p)
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_WSNetwork_action(self):
        dialog = Dialog_WS(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        k = dialog.NumberofNeighbors()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = NM.directed_watts_strogatz_graph(n,k,p)
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_NWNetwork_action(self):
        dialog = Dialog_NW(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        k = dialog.NumberofNeighbors()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.newman_watts_strogatz_graph(n, k, p)
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_NWNetwork_action(self):
        dialog = Dialog_NW(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        k = dialog.NumberofNeighbors()
        p = dialog.ConnectProbability()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = NM.directed_newman_watts_strogatz_graph(n,k,p)
        pos = nx.layout.circular_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_BANetwork_action(self):
        dialog = Dialog_BA(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        m = dialog.NumberofAddedNodes()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.barabasi_albert_graph(n, m)
        pos = nx.layout.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)

    def network_menu_directed_BANetwork_action(self):
        dialog = Dialog_BA(self)
        result = dialog.exec_()
        n = dialog.NumberofNodes()
        m = dialog.NumberofAddedNodes()
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = NM.directed_barabasi_albert_graph(n, m)
        pos = nx.layout.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    def network_menu_SFNetwork_action(self):
        pass

    def network_menu_karate_club_network_action(self):
        global GLOBAL_NETWORK
        GLOBAL_NETWORK.clear()
        GLOBAL_NETWORK = nx.karate_club_graph()
        pos = nx.layout.spring_layout(GLOBAL_NETWORK)
        self.main_widget.update_centralWidget(GLOBAL_NETWORK, pos)


    ##################################################################
    # 
    # Centrality (degree, betweenness, closeness, eigenvector)
    # 
    ##################################################################

    def centrality_menu_NodeDegree_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.degree_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Degree Centrality', col1, col2)
        result = dialog.exec_()

    def centrality_menu_NodeBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.betweenness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Betweenness Centrality', col1, col2)
        result = dialog.exec_()

    def centrality_menu_ClosenessBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.closeness_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Closeness Centrality', col1, col2)
        result = dialog.exec_()

    def centrality_menu_EigenvectorBetweenness_action(self):
        dialog = Dialog_CentralityDisplayResult(self)
        col1 = []
        col2 = []
        global GLOBAL_NETWORK
        for x, y in nx.eigenvector_centrality(GLOBAL_NETWORK).iteritems():
            col1.append(x)
            col2.append(y)
        dialog.add_contents('NodeID', 'Eigenvector Centrality', col1, col2)
        result = dialog.exec_()


    def controllability_menu_StructralControllability_action(self):
        pass
    def controllability_menu_ExactControllability_action(self):
        pass

    def robustness_menu_RondomAttack_action(self):
        pass
    def robustness_menu_RecaculatedMaxDegree_action(self):
        pass
    def robustness_menu_RecaculatedMaxBetweenness_action(self):
        pass
    def robustness_menu_CascadeBasedonNodeCapacity_action(self):
        pass


    def about_menu_About_action(self):
        QtGui.QMessageBox.about(self, "About",
        """
        Network Controllability Analysis Software

        Copyright (C) 2015 Xin-Feng Li (silfer.lee@gmail.com)

        This program is distributed under BSD License
        """)        

if __name__ == "__main__":
    qApp = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(qApp.exec_())