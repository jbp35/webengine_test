from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QSurfaceFormat, QOpenGLContext


# simplified version of app/main.cpp
format = QSurfaceFormat()
format.setVersion( 4, 3 )
format.setProfile( QSurfaceFormat.CoreProfile )
QSurfaceFormat.setDefaultFormat( format )
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
app = QtWidgets.QApplication( [] )



# simplified verison of a qgis plugin using qtwebengine
from PyQt5.QtWebEngineWidgets import QWebEngineView
dlg = QtWidgets.QDialog()
view = QWebEngineView()
layout = QtWidgets.QHBoxLayout()
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(view)
dlg.setLayout(layout)
url = QUrl("https://www.whatsmybrowser.org/")
view.load(url)
dlg.show()




# Print global shared context spec version
global_context = QOpenGLContext.globalShareContext()
print(global_context.format().majorVersion())
print(global_context.format().minorVersion())





app.exec_()



