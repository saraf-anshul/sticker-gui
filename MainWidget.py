
from PyQt5.QtWidgets import (
	QMainWindow, 
	QWidget, 
	QPushButton, 
	QFileDialog, 
	QLabel, 
	QVBoxLayout, 
	QHBoxLayout, 
	QGroupBox, 
)
from StorageUtils import *
from PyQt5.QtCore import pyqtSlot ,Qt
from LabelEditText import LabelEditText
from FileInfoAndSelectorBox import FileInfoAndSelectorBox


class MainWidget(QMainWindow):

	saveLocation = ""

	def __init__(self):
		super().__init__()
		
		### window attrs
		self.setWindowTitle("Sticker GUI")
		self.resize(300, 300)
		wid = QWidget(self)
		self.setCentralWidget(wid)
		layout = QVBoxLayout()
		wid.setLayout(layout)
		###

		### sticker name label
		self.inputTB = LabelEditText("Sticker name:")
		layout.addWidget(self.inputTB)
		###

		### button select
		self.stickerFileIn = FileInfoAndSelectorBox("Sticker", "png", 1)
		layout.addWidget(self.stickerFileIn)
		###

		### out-file dir select
		self.outputDir = QPushButton('Select output dir', self)
		self.outputDir.clicked.connect(self.on_click_dir)
		layout.addWidget(self.outputDir)
		###

		### horizontal layout (Output)
		horizontalGroupBox = QGroupBox()
		h_layout = QHBoxLayout()

		#### textview says "outupt Dir"
		self.labelOutx = QLabel('', self)
		self.labelOutx.setText("Output directory:")
		self.labelOutx.setAlignment(Qt.AlignCenter)
		h_layout.addWidget(self.labelOutx)
		####

		#### out-file dir textview
		self.labelOut = QLabel('This is label', self)
		self.labelOut.setText("No output directory selected")
		self.labelOut.setAlignment(Qt.AlignCenter)
		h_layout.addWidget(self.labelOut)
		####

		horizontalGroupBox.setLayout(h_layout)
		layout.addWidget(horizontalGroupBox)
		###

		### load save file or create
		try:
			with open( getLocationsFile() ,'r' ) as F:
				self.updateSaveLocation( json.load(F)['last'] )
		except:
			with open( getLocationsFile() ,'w' ) as F:
				json.dump({'last' : getDefaultStorageLocation()} ,F)
			self.updateSaveLocation( getDefaultStorageLocation() )
		###

		### run button
		self.button_run = QPushButton('Create', self)
		self.button_run.setToolTip('Run Script')
		self.button_run.setStyleSheet("QPushButton {background-color:#48A14D; border-radius: 4px; min-height: 22px;}")
		self.button_run.clicked.connect(self.run_script)
		layout.addWidget(self.button_run)
		###

	# download location onClick
	@pyqtSlot()
	def on_click_dir(self):
		dir = self.saveLocation

		dirName = QFileDialog().getExistingDirectory(self, 'Select an directory to save files' ,dir)
		if dirName:
			print(dirName)
			self.updateSaveLocation(dirName)
	
	@pyqtSlot()
	def run_script(self):
		oDir = self.saveLocation
		selectedFiles = self.stickerFileIn.selectedFiles
		if( len(selectedFiles) == 0 ):
			print( "no files selected" )
			return
		
		with open( getLocationsFile() ,'w' ) as F:
			json.dump({'last' : oDir} ,F)

		iDir = selectedFiles[0]
		name = self.inputTB.getText()
		transformAndSave(name, iDir, oDir)

	def updateSaveLocation(self, loc):
		self.labelOut.setText(loc)
		self.saveLocation = loc

