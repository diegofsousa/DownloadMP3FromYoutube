# -*- coding: iso-8859-1 -*-
import sys, os, subprocess
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from script import *
from threading import Thread, current_thread

class index(QDialog):
	def __init__(self, parent=None):
		super(index, self).__init__(parent)

		self.setWindowTitle("Fast mp3 downloader")

		label = QLabel("Find the music: ")
		self.info = QLabel("")
		self.nome_lineEdit = QLineEdit("")


		download_button = QPushButton("Download!")
		download_paste = QPushButton("Downloaded files")

		hbox = QHBoxLayout()
		hbox.addWidget(label)
		hbox.addWidget(self.nome_lineEdit)

		hbox1 = QHBoxLayout()

		container_h = QVBoxLayout()
		container_h.addLayout(hbox)
		container_h.addLayout(hbox1)
		
		vbox = QVBoxLayout()
		
		vbox.addWidget(self.info)
		vbox.addWidget(download_button)
		vbox.addWidget(download_paste)

		jbox = QVBoxLayout()
		jbox.addLayout(container_h)
		jbox.addLayout(vbox)

		#events
		self.connect(download_paste, SIGNAL("clicked()"), self.open_download)
		self.connect(download_button, SIGNAL("clicked()"), self.download)
		self.setLayout(jbox)
		self.setGeometry(500,500,430,130)


	def open_download(self):
		abrir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app/files')
		subprocess.Popen(["xdg-open", abrir])

	def download(self):
		texto = self.nome_lineEdit.displayText()
		self.nome_lineEdit.setText("")
		a = self.Th(self.info)
		a.start()		
		down = self.Baixar(texto, self.info)
		down.start()


	class Th(Thread):
		def __init__ (self, container):
			Thread.__init__(self)
			self.container = container

		def run(self):
			self.container.setText("Downloading...")


	class Baixar(Thread):
		def __init__ (self, texto, info):
			Thread.__init__(self)
			self.texto = texto
			self.info = info

		def run(self):
			self.notifyIcon = QSystemTrayIcon()
			self.notifyIcon.setVisible(True)
			titulo, url_final = search_para_url(str(self.texto))
			if titulo == False:
				self.info.setText("")

			self.notifyIcon.showMessage(
				"Download",
				u"Downloading "+ titulo + "!",
				QSystemTrayIcon.Information,3000)

			result = baixar_musica(titulo, url_final)
			if result != False:
				self.notifyIcon.showMessage(
					"Download Finished",
					u"The "+ result + " has finished. :)",
					QSystemTrayIcon.Information,3000)
				self.info.setText("Download Finished")
			else:
				self.notifyIcon.showMessage(
					"Download",
					u"Error downloading :/",
					QSystemTrayIcon.Information,3000)
				self.info.setText("Download Error")


app = QApplication(sys.argv)
dlg = index()
dlg.exec_()
