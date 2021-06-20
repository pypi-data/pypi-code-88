import gc, sys, joblib,os, traceback
from logging import raiseExceptions
import pyOfficeSheet
from os import close, remove
from typing import Any
from time import sleep

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import pandas as pd
import numpy as np
from webbrowser import open as webbrowser_open
from inspect import getfile
from json import loads as json_loads
from json import dumps as json_dumps
from inspect import getfile
import pyOfficeLearn

def pyofficelearn(screen_width,screen_height):
    image_path = os.path.join(getfile(pyOfficeLearn).replace('__init__.py',''),'pic','icon')

############################################################################################################################################################
############################## read stuff ##################################################################################################################
############################################################################################################################################################
#                                                                    dddddddd                                                                                                        
#                                                                    d::::::d                               tttt                               ffffffffffffffff    ffffffffffffffff  
#                                                                    d::::::d                            ttt:::t                              f::::::::::::::::f  f::::::::::::::::f 
#                                                                    d::::::d                            t:::::t                             f::::::::::::::::::ff::::::::::::::::::f
#                                                                    d:::::d                             t:::::t                             f::::::fffffff:::::ff::::::fffffff:::::f
# rrrrr   rrrrrrrrr       eeeeeeeeeeee    aaaaaaaaaaaaa      ddddddddd:::::d          ssssssssss   ttttttt:::::ttttttt    uuuuuu    uuuuuu   f:::::f       fffffff:::::f       ffffff
# r::::rrr:::::::::r    ee::::::::::::ee  a::::::::::::a   dd::::::::::::::d        ss::::::::::s  t:::::::::::::::::t    u::::u    u::::u   f:::::f             f:::::f             
# r:::::::::::::::::r  e::::::eeeee:::::eeaaaaaaaaa:::::a d::::::::::::::::d      ss:::::::::::::s t:::::::::::::::::t    u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
# rr::::::rrrrr::::::re::::::e     e:::::e         a::::ad:::::::ddddd:::::d      s::::::ssss:::::stttttt:::::::tttttt    u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  r:::::r     r:::::re:::::::eeeee::::::e  aaaaaaa:::::ad::::::d    d:::::d       s:::::s  ssssss       t:::::t          u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  r:::::r     rrrrrrre:::::::::::::::::e aa::::::::::::ad:::::d     d:::::d         s::::::s            t:::::t          u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
#  r:::::r            e::::::eeeeeeeeeee a::::aaaa::::::ad:::::d     d:::::d            s::::::s         t:::::t          u::::u    u::::u   f:::::f             f:::::f             
#  r:::::r            e:::::::e         a::::a    a:::::ad:::::d     d:::::d      ssssss   s:::::s       t:::::t    ttttttu:::::uuuu:::::u   f:::::f             f:::::f             
#  r:::::r            e::::::::e        a::::a    a:::::ad::::::ddddd::::::dd     s:::::ssss::::::s      t::::::tttt:::::tu:::::::::::::::uuf:::::::f           f:::::::f            
#  r:::::r             e::::::::eeeeeeeea:::::aaaa::::::a d:::::::::::::::::d     s::::::::::::::s       tt::::::::::::::t u:::::::::::::::uf:::::::f           f:::::::f            
#  r:::::r              ee:::::::::::::e a::::::::::aa:::a d:::::::::ddd::::d      s:::::::::::ss          tt:::::::::::tt  uu::::::::uu:::uf:::::::f           f:::::::f            
#  rrrrrrr                eeeeeeeeeeeeee  aaaaaaaaaa  aaaa  ddddddddd   ddddd       sssssssssss              ttttttttttt      uuuuuuuu  uuuufffffffff           fffffffff            
                                                                                                                                                                           
    def importJoblib(pick=True,filename=None,filter=None,widget=None): # main importer to load binary file
        global pandas_data
        if pick:
            filter = 'Python Object(*.npobj *.pdobj)'
            filename, filter = QFileDialog.getOpenFileName(None, 'Open File', filter=filter)
        if '.npobj' in filename:
            data = joblib.load(filename)
            header = None
        elif '.pdobj' in filename:
            dataframe = joblib.load(filename)
            header = list(dataframe.keys())
            data = np.array(dataframe)

        if widget !=None:
            widget.setText(filename)

    def loadKerasModel():
        global model
        filename, filter = QFileDialog.getExistingDirectory(None,'Load Keras Model')

        from keras.models import load_model

        model = load_model(filename)

    def load_project_file():
        global keras_model
        filename, filter = QFileDialog.getOpenFileName()
        keras_model = joblib.load(filename)




############################################################################################################################################################
############################# save stuff ###################################################################################################################
############################################################################################################################################################
#                                                                                                                                                                                   
#                                                                                                          tttt                               ffffffffffffffff    ffffffffffffffff  
#                                                                                                       ttt:::t                              f::::::::::::::::f  f::::::::::::::::f 
#                                                                                                       t:::::t                             f::::::::::::::::::ff::::::::::::::::::f
#                                                                                                       t:::::t                             f::::::fffffff:::::ff::::::fffffff:::::f
#     ssssssssss     aaaaaaaaaaaaavvvvvvv           vvvvvvv eeeeeeeeeeee             ssssssssss   ttttttt:::::ttttttt    uuuuuu    uuuuuu   f:::::f       fffffff:::::f       ffffff
#   ss::::::::::s    a::::::::::::av:::::v         v:::::vee::::::::::::ee         ss::::::::::s  t:::::::::::::::::t    u::::u    u::::u   f:::::f             f:::::f             
# ss:::::::::::::s   aaaaaaaaa:::::av:::::v       v:::::ve::::::eeeee:::::ee     ss:::::::::::::s t:::::::::::::::::t    u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
# s::::::ssss:::::s           a::::a v:::::v     v:::::ve::::::e     e:::::e     s::::::ssss:::::stttttt:::::::tttttt    u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#  s:::::s  ssssss     aaaaaaa:::::a  v:::::v   v:::::v e:::::::eeeee::::::e      s:::::s  ssssss       t:::::t          u::::u    u::::u  f::::::::::::f      f::::::::::::f       
#    s::::::s        aa::::::::::::a   v:::::v v:::::v  e:::::::::::::::::e         s::::::s            t:::::t          u::::u    u::::u  f:::::::ffffff      f:::::::ffffff       
#       s::::::s    a::::aaaa::::::a    v:::::v:::::v   e::::::eeeeeeeeeee             s::::::s         t:::::t          u::::u    u::::u   f:::::f             f:::::f             
# ssssss   s:::::s a::::a    a:::::a     v:::::::::v    e:::::::e                ssssss   s:::::s       t:::::t    ttttttu:::::uuuu:::::u   f:::::f             f:::::f             
# s:::::ssss::::::sa::::a    a:::::a      v:::::::v     e::::::::e               s:::::ssss::::::s      t::::::tttt:::::tu:::::::::::::::uuf:::::::f           f:::::::f            
# s::::::::::::::s a:::::aaaa::::::a       v:::::v       e::::::::eeeeeeee       s::::::::::::::s       tt::::::::::::::t u:::::::::::::::uf:::::::f           f:::::::f            
#  s:::::::::::ss   a::::::::::aa:::a       v:::v         ee:::::::::::::e        s:::::::::::ss          tt:::::::::::tt  uu::::::::uu:::uf:::::::f           f:::::::f            
#   sssssssssss      aaaaaaaaaa  aaaa        vvv            eeeeeeeeeeeeee         sssssssssss              ttttttttttt      uuuuuuuu  uuuufffffffff           fffffffff           
# 
# 
 
    def save_project_file(saveAs = False): # save project as a dictionary object using joblib
        filter = "py-office-learn(*.polprj)"
        if saveAs:
            directory, filter = QFileDialog.getSaveFileName(None, 'Save File',filter=filter)

        elif current_file_name !=None:
            directory= current_file_name

        directory = directory+'.polprj' if '.polprj' not in directory else directory

        joblib.dump(keras_model,filename=directory,compress=9)

    def saveKerasModel():
        filename,filter = QFileDialog.getSaveFileName(None,'Save Model')

        from keras.models import save_model
        save_model(model,filename)

        
############################################################################################################################################################
################################# operational functions ##########################################################################################################
############################################################################################################################################################
#                                                                                                                                                                
#     ffffffffffffffff                                                                 tttt            iiii                                                      
#    f::::::::::::::::f                                                             ttt:::t           i::::i                                                     
#   f::::::::::::::::::f                                                            t:::::t            iiii                                                      
#   f::::::fffffff:::::f                                                            t:::::t                                                                      
#   f:::::f       ffffffuuuuuu    uuuuuunnnn  nnnnnnnn        ccccccccccccccccttttttt:::::ttttttt    iiiiiii    ooooooooooo   nnnn  nnnnnnnn        ssssssssss   
#   f:::::f             u::::u    u::::un:::nn::::::::nn    cc:::::::::::::::ct:::::::::::::::::t    i:::::i  oo:::::::::::oo n:::nn::::::::nn    ss::::::::::s  
#  f:::::::ffffff       u::::u    u::::un::::::::::::::nn  c:::::::::::::::::ct:::::::::::::::::t     i::::i o:::::::::::::::on::::::::::::::nn ss:::::::::::::s 
#  f::::::::::::f       u::::u    u::::unn:::::::::::::::nc:::::::cccccc:::::ctttttt:::::::tttttt     i::::i o:::::ooooo:::::onn:::::::::::::::ns::::::ssss:::::s
#  f::::::::::::f       u::::u    u::::u  n:::::nnnn:::::nc::::::c     ccccccc      t:::::t           i::::i o::::o     o::::o  n:::::nnnn:::::n s:::::s  ssssss 
#  f:::::::ffffff       u::::u    u::::u  n::::n    n::::nc:::::c                   t:::::t           i::::i o::::o     o::::o  n::::n    n::::n   s::::::s      
#   f:::::f             u::::u    u::::u  n::::n    n::::nc:::::c                   t:::::t           i::::i o::::o     o::::o  n::::n    n::::n      s::::::s   
#   f:::::f             u:::::uuuu:::::u  n::::n    n::::nc::::::c     ccccccc      t:::::t    tttttt i::::i o::::o     o::::o  n::::n    n::::nssssss   s:::::s 
#  f:::::::f            u:::::::::::::::uun::::n    n::::nc:::::::cccccc:::::c      t::::::tttt:::::ti::::::io:::::ooooo:::::o  n::::n    n::::ns:::::ssss::::::s
#  f:::::::f             u:::::::::::::::un::::n    n::::n c:::::::::::::::::c      tt::::::::::::::ti::::::io:::::::::::::::o  n::::n    n::::ns::::::::::::::s 
#  f:::::::f              uu::::::::uu:::un::::n    n::::n  cc:::::::::::::::c        tt:::::::::::tti::::::i oo:::::::::::oo   n::::n    n::::n s:::::::::::ss  
#  fffffffff                uuuuuuuu  uuuunnnnnn    nnnnnn    cccccccccccccccc          ttttttttttt  iiiiiiii   ooooooooooo     nnnnnn    nnnnnn  sssssssssss    
        
    def alertbox(err): # a function to alert user when error occourse
            alert = QMessageBox()
            alert.setWindowTitle('ERROR')
            alert.setWindowIcon(alert.style().standardIcon(alert.style().SP_MessageBoxCritical))
            alert.setText(str(err))
            alert.setAttribute(Qt.WA_DeleteOnClose) # prevent memory leak
            alert.setTextInteractionFlags(Qt.TextBrowserInteraction)
            alert.exec_()

    class StdoutRedirector:
        '''A class for redirecting stdout to the Text widget.'''
        def __init__(self,widget):
            self.widget = widget
        def write(self,str):
            self.widget.setText(self.widget.toPlainText()+str)

    def Build_and_run_keras():
        try:
            from ast import literal_eval
            import threading

            class newTextBrowser(QTextBrowser):

                appendSignal = Signal(str) # a signal is required to change text in another thread

                def __init__(self):
                    super().__init__()
                    self.appendSignal.connect(lambda x:self.append(str(x)))

                def emitAppend(self,text):
                    self.appendSignal.emit(str(text))


            if keras_model['layers'] == []:
                        alertbox('No layers found')
                        return

            for i in keras_model['layers']:
                if not i.check_submit():   # check if all args is filled

                    alertbox('Not all arguments satisfy, please complete all fields')
                    raise Exception('arguments not satisfy')

            dialog = QDialog()
            dialog.setAttribute(Qt.WA_DeleteOnClose)
            dialog.setGeometry(int(screen_width/6),int(screen_height/6),int(screen_width*2/3),int(screen_height*2/3))
            layout = QVBoxLayout()
            dialog.setLayout(layout)

            label = newTextBrowser()
            label.setStyleSheet('background-color:black;color:white;')

            trainButton = QPushButton('Fit and Train Model')
            trainButton.setDisabled(True)
            layout.addWidget(label)
            layout.addWidget(trainButton)

            def keras_thread():

                def print(string):
                    label.emitAppend(string) # emit signal to change text

                print('Importing Keras from tensorflow...')

                from tensorflow import keras

                from tensorflow.python.client import device_lib

                print(device_lib.list_local_devices())


                try:
                    layers = []

                    classLayers=keras_model.get('layers')

                    print(f'{len(keras_model["layers"])} layers found')

                    if classLayers[0].blockType != 'Input':
                        print('first block is not Input layer')
                        print('automatically insert Input layer...')
                        print('building Input Layer class...')
                        class inputlayer:
                            def __init__(self):
                                self.blockType = 'Input'
                                self.shape = keras_model['input_shape']
                                
                            def check_submit(self):
                                return True

                            def getArgs(self):
                                return [self.shape]
                        
                        new_inputLayer = inputlayer()
                        classLayers.insert(0,new_inputLayer)

                    print('Constructing layers...')

                    for i in classLayers:

                        if i.blockType == 'Input':
                            shape = i.getArgs()[0]
                            layers.append(keras.Input(shape=shape))

                        elif i.blockType == 'Embedding Layer':
                            input_dim,output_dim,initializer,regularizers,mask,inputLength, constraints= i.getArgs()

                            layers.append(keras.layers.Embedding(input_dim=input_dim
                            ,output_dim=output_dim,embeddings_initializer=initializer
                            ,embeddings_regularizer=regularizers,mask_zero=mask,input_length=inputLength
                            ,embeddings_constraint=constraints))

                        elif i.blockType == 'Dense Layer':
                            units,activation,bias,ki,bi,kr,br,ar,kc,bc = i.getArgs()

                            layers.append(keras.layers.Dense(units=units,activation=activation
                            ,use_bias=bias,kernel_initializer=ki,bias_initializer=bi
                            ,kernel_regularizer=kr,bias_regularizer=br
                            ,activity_regularizer=ar,kernel_constraint=kc,bias_constraint=bc))

                        elif i.blockType == 'Dropout Layer':
                            value = i.getArgs()[0]

                            layers.append(keras.layers.Dropout(rate=value))

                        elif i.blockType == 'Masking Layer':
                            a = i.getArgs()[0]

                            layers.append(keras.layers.Masking(mask_value=a))

                        elif i.blockType == 'Activation Layer':
                            a = i.getArgs()[0]

                            layers.append(keras.layers.Activation(a))
                    
                    if 'new_inputLayer' in locals():
                        classLayers.remove(new_inputLayer)

                    if keras_model['sequential']:
                        print('building Sequential model...')

                        model = keras.Sequential()
                        for i in layers:
                            model.add(i)
                    else:
                        print('building Functional Model...')

                        for i in range(len(layers)):
                            if i != 0 :
                                layers[i] = layers[i](layers[i-1])

                        model = keras.Model(inputs=layers[0],outputs=layers[-1])
                    
                    sub = keras_model['compiler']
                    optimizer = sub.optimizer.currentText()
                    loss = None if sub.loss.currentText()== 'None' else sub.loss.currentText()
                    metrics = None if sub.metrics == [] else sub.metrics
                    stepsPerExec = sub.stepsPerExec.value()

                    print('Compiling model...')
                    model.compile(optimizer=optimizer,loss=loss,metrics=metrics,steps_per_execution=stepsPerExec)

                    print('generating summary...\n')
                    model.summary(print_fn=print)

                    keras_model['model'] = model

                    trainButton.setDisabled(False)

                except:
                    print(traceback.format_exc())
                    traceback.print_exc()

            thread = threading.Thread(target=keras_thread,daemon=True)
            thread.start()

            dialog.exec_()

        except :
            alertbox(traceback.format_exc())
            



##############################################################################################################################################
############################ set up ##########################################################################################################
##############################################################################################################################################
#                                               tttt                                               
#                                            ttt:::t                                               
#                                            t:::::t                                               
#                                            t:::::t                                               
#     ssssssssss       eeeeeeeeeeee    ttttttt:::::ttttttt    uuuuuu    uuuuuu ppppp   ppppppppp   
#   ss::::::::::s    ee::::::::::::ee  t:::::::::::::::::t    u::::u    u::::u p::::ppp:::::::::p  
# ss:::::::::::::s  e::::::eeeee:::::eet:::::::::::::::::t    u::::u    u::::u p:::::::::::::::::p 
# s::::::ssss:::::se::::::e     e:::::etttttt:::::::tttttt    u::::u    u::::u pp::::::ppppp::::::p
#  s:::::s  ssssss e:::::::eeeee::::::e      t:::::t          u::::u    u::::u  p:::::p     p:::::p
#    s::::::s      e:::::::::::::::::e       t:::::t          u::::u    u::::u  p:::::p     p:::::p
#       s::::::s   e::::::eeeeeeeeeee        t:::::t          u::::u    u::::u  p:::::p     p:::::p
# ssssss   s:::::s e:::::::e                 t:::::t    ttttttu:::::uuuu:::::u  p:::::p    p::::::p
# s:::::ssss::::::se::::::::e                t::::::tttt:::::tu:::::::::::::::uup:::::ppppp:::::::p
# s::::::::::::::s  e::::::::eeeeeeee        tt::::::::::::::t u:::::::::::::::up::::::::::::::::p 
#  s:::::::::::ss    ee:::::::::::::e          tt:::::::::::tt  uu::::::::uu:::up::::::::::::::pp  
#   sssssssssss        eeeeeeeeeeeeee            ttttttttttt      uuuuuuuu  uuuup::::::pppppppp    
#                                                                               p:::::p            
#                                                                               p:::::p            
#                                                                              p:::::::p           
#                                                                              p:::::::p           
#                                                                              p:::::::p           
#                                                                              ppppppppp  
  
#################### Custom Widgets ##################################################################################################################
 
    class DraggableLabel(QLabel):
        'A custom widget that support drag action'
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.drag_start_position = event.pos()

        def mouseMoveEvent(self, event):
            if not (event.buttons() & Qt.LeftButton):
                return
            if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
                return
            drag = QDrag(self)
            mimedata = QMimeData()
            mimedata.setText(self.text())

            drag.setMimeData(mimedata)
            pixmap = QPixmap(self.size())
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)


    class DropAcceptWidget(QWidget):
        'A custom Widget that support drop action'
        def __init__(self,layout):
            super().__init__()
            self.setAcceptDrops(True)
            self.setLayout(layout)
            self.currentLayout = layout

        def dragEnterEvent(self, event: QDragEnterEvent):
            if event.mimeData().hasText():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event: QDropEvent):
            if event.mimeData().hasText():
                text = event.mimeData().text()
                
                block = LayerBlockWidget(text)
                if text == 'Sequential Model' and keras_model['sequential']==False:
                    self.currentLayout.insertWidget(1,block)
                    keras_model['sequential'] = True
                elif text != 'Sequential Model':
                    self.currentLayout.addWidget(block)
                    keras_model['layers'].append(block)

        def addBlock(self,text,setting=False):
            block = LayerBlockWidget(text)
            if text == 'Sequential Model' and keras_model['sequential']==False:
                self.currentLayout.insertWidget(1,block)
                keras_model['sequential'] = True
            elif text != 'Sequential Model':
                self.currentLayout.addWidget(block)
                keras_model['layers'].append(block)
            if setting:
                exec(setting,locals())


    class LayerBlockWidget(QLabel):
        'A custom widget that represent a single keras layer'
        def __init__(self,blockType:str):
            super().__init__()
            self.index = len(keras_model['layers'])
            self.blockType = blockType

            initializers = ['random_normal','random_uniform','truncated_normal','zeros','ones','glorot_normal','glorot_uniform','identity','orthogonal','constant','variance_scaling']
            activations = ['None','relu','sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']
            regulars = ['None','l1','l2']
            constraints = ['None','max_norm','min_max_norm','non_neg','unit_norm','radial_constraint']

            self.setFixedHeight(int(screen_height/8))
            self.setStyleSheet('background-color:#303030;color:white;')
            self.setAttribute(Qt.WA_DeleteOnClose)
            self.layout = QGridLayout()
            self.layout.setAlignment(Qt.AlignLeft)
            self.layout.setVerticalSpacing(int(screen_height/100))
            self.setLayout(self.layout)

            def deleteBlock():
                if self.blockType != 'Sequential Model':
                    keras_model['layers'].remove(self)
                else:
                    keras_model['sequential'] = False
                self.close()
                self.parentWidget().update()

            blockLabel = QLabel(blockType)
            blockLabel.setStyleSheet('font-size:30px;')
            closeButton = QPushButton()
            closeButton.setIcon(self.style().standardIcon(self.style().SP_DialogCloseButton))
            closeButton.setFlat(True)
            closeButton.clicked.connect(deleteBlock)
            self.layout.addWidget(blockLabel,0,0,1,20)
            self.layout.addWidget(closeButton,0,21,1,1)

            class Label(QLabel):
                def __init__(self, text: str):
                    super().__init__(text)
                    self.setAlignment(Qt.AlignRight)


            if blockType == 'Sequential Model':
                self.setFixedHeight(int(screen_height/16))

            elif blockType == 'Input':

                def change(index,num):
                    self.shape[index] = num

                class customValidate(QValidator):
                    def validate(self, arg__1: str, arg__2: int):
                        print(arg__1)
                        if arg__1.replace(',','').isnumeric()or arg__1 == '':
                            return QValidator.Acceptable,arg__1, arg__2
                        else:
                            return QValidator.Invalid,arg__1,arg__2


                self.shape = (0,0)

                self.inputShape = QLineEdit()
                self.inputShape.setPlaceholderText('shape of array e.g.(3,50,50)')
                self.inputShape.setFixedWidth(int(screen_width/10))
                self.inputShape.setValidator(customValidate())

                self.layout.addWidget(QLabel('Input shape:('),1,0,1,1)
                self.layout.addWidget(self.inputShape,1,1,1,2)
                self.layout.addWidget(QLabel(')'+' '*200),1,3,1,6)

            elif blockType == 'Embedding Layer':
                self.input_dim = QLineEdit()
                self.input_dim.setValidator(QIntValidator())
                self.input_dim.setMaximumWidth(int(screen_width/20))

                self.output_dim = QLineEdit()
                self.output_dim.setValidator(QIntValidator())
                self.output_dim.setMaximumWidth(int(screen_width/20))

                self.initializer = QComboBox()
                self.initializer.addItems(['uniform']+initializers)

                self.regularizer = QComboBox()
                self.regularizer.addItems(regulars)
                self.mask_zero = QCheckBox('mask_zero')
                self.input_length = QLineEdit()
                self.input_length.setValidator(QIntValidator())
                self.input_length.setPlaceholderText('None')
                self.input_length.setMaximumWidth(int(screen_width/20))
                self.constraint = QComboBox()
                self.constraint.addItems(constraints)

                self.layout.addWidget(Label('input dim: '),1,0,1,1)
                self.layout.addWidget(self.input_dim,1,1,1,1)
                self.layout.addWidget(Label('output dim: '),1,2,1,1)
                self.layout.addWidget(self.output_dim,1,3,1,1)
                self.layout.addWidget(Label('  initializer: '),1,4,1,1)
                self.layout.addWidget(self.initializer,1,5,1,1)
                self.layout.addWidget(Label('  regularizer: '),1,6,1,1)
                self.layout.addWidget(self.regularizer,1,7,1,1)
                self.layout.addWidget(self.mask_zero,2,0,1,1)
                self.layout.addWidget(Label('  input Length: '),2,2,1,1)
                self.layout.addWidget(self.input_length,2,3,1,1)
                self.layout.addWidget(Label('  constraint: '),2,4,1,1)
                self.layout.addWidget(self.constraint,2,5,1,2)

            elif blockType == 'Dropout Layer':
                self.rate = QDoubleSpinBox()
                self.rate.setRange(0.00,1.00)
                self.rate.setSingleStep(0.01)
                self.rate.setDecimals(2)
                self.rate.setValue(0.20)
                self.layout.addWidget(Label('rate: '),1,0,1,1)
                self.layout.addWidget(self.rate,1,1,1,1)

            elif blockType == 'Dense Layer':
                self.setFixedHeight(int(screen_height/6))
                self.units = QLineEdit()
                self.units.setValidator(QIntValidator())
                self.units.setMaximumWidth(int(screen_width/20))

                self.activation = QComboBox()
                self.activation.addItems(activations)

                self.use_bias = QCheckBox('Use bias')
                self.use_bias.setChecked(True)

                self.kernel_initializer = QComboBox()
                self.kernel_initializer.addItems(initializers)
                self.kernel_initializer.setCurrentText("glorot_uniform")

                self.bias_initializer = QComboBox()
                self.bias_initializer.addItems(initializers)
                self.bias_initializer.setCurrentText('zeros')

                self.kernel_regularizer = QComboBox()
                self.kernel_regularizer.addItems(regulars)

                self.bias_regularizer = QComboBox()
                self.bias_regularizer.addItems(regulars)

                self.activity_regularizer = QComboBox()
                self.activity_regularizer.addItems(regulars)

                self.kernel_constraint = QComboBox()
                self.kernel_constraint.addItems(constraints)

                self.bias_constraint = QComboBox()
                self.bias_constraint.addItems(constraints)

                self.layout.addWidget(Label('units: '),1,0,1,1)
                self.layout.addWidget(self.units,1,1,1,1)
                self.layout.addWidget(Label('  activation: '),1,2,1,1)
                self.layout.addWidget(self.activation,1,3,1,1)
                self.layout.addWidget(self.use_bias,1,4,1,1)
                self.layout.addWidget(Label('  kernel_init: '),1,5,1,1)
                self.layout.addWidget(self.kernel_initializer,1,6,1,1)
                self.layout.addWidget(Label('bias_init: '),1,7,1,1)
                self.layout.addWidget(self.bias_initializer,1,8,1,1)
                self.layout.addWidget(Label('Regularizers :     kernel:'),2,0,1,2)
                self.layout.addWidget(self.kernel_regularizer,2,2,1,1)
                self.layout.addWidget(Label('    bias:'),2,3,1,1)
                self.layout.addWidget(self.bias_regularizer,2,4,1,1)
                self.layout.addWidget(Label('    activity:'),2,5,1,1)
                self.layout.addWidget(self.activity_regularizer,2,6,1,1)
                self.layout.addWidget(Label('Constraint:         kernel:'),3,0,1,2)
                self.layout.addWidget(self.kernel_constraint,3,2,1,1)
                self.layout.addWidget(Label('    bias:'),3,3,1,1)
                self.layout.addWidget(self.bias_constraint,3,4,1,1)

            elif blockType == 'Masking Layer':
                self.setFixedHeight(int(screen_height/10))
                self.mask_value= QDoubleSpinBox()
                self.mask_value.setRange(0.0,1.0)
                self.mask_value.setSingleStep(0.1)
                self.layout.addWidget(QLabel('mask_value: '),1,0,1,1)
                self.layout.addWidget(self.mask_value,1,1,1,1)
                self.layout.addWidget(QLabel(' '*200),1,2,1,6)

            elif blockType == 'Activation Layer':
                self.setFixedHeight(int(screen_height/10))
                self.activation = QComboBox()
                self.activation.addItems(activations[1:])

                self.layout.addWidget(QLabel('Activation: '),1,0,1,1)
                self.layout.addWidget(self.activation,1,1,1,1)
                self.layout.addWidget(QLabel(' '*200),1,2,1,6)
            
            elif blockType == 'Conv1D Layer':
                self.setFixedHeight(int(screen_height/5))
                self.filter = QLineEdit()
                self.filter.setValidator(QIntValidator())

                self.kernel_size = QLineEdit()
                self.kernel_size.setValidator(QIntValidator())

                self.padding = QComboBox()
                self.padding.addItems(['valid','same','causal'])


                self.strides = QSpinBox()
                self.strides.setRange(1,10)

                self.activation = QComboBox()
                self.activation.addItems(activations)

                self.use_bias = QCheckBox('Use bias')
                self.use_bias.setChecked(True)

                self.kernel_initializer = QComboBox()
                self.kernel_initializer.addItems(initializers)
                self.kernel_initializer.setCurrentText("glorot_uniform")

                self.bias_initializer = QComboBox()
                self.bias_initializer.addItems(initializers)
                self.bias_initializer.setCurrentText('zeros')

                self.kernel_regularizer = QComboBox()
                self.kernel_regularizer.addItems(regulars)

                self.bias_regularizer = QComboBox()
                self.bias_regularizer.addItems(regulars)

                self.activity_regularizer = QComboBox()
                self.activity_regularizer.addItems(regulars)

                self.kernel_constraint = QComboBox()
                self.kernel_constraint.addItems(constraints)

                self.bias_constraint = QComboBox()
                self.bias_constraint.addItems(constraints)

                self.layout.addWidget(Label('filter* : '),1,0,1,1)
                self.layout.addWidget(self.filter,1,1,1,1)
                self.layout.addWidget(Label('kernel_size* : '),1,2,1,1)
                self.layout.addWidget(self.kernel_size,1,3,1,1)
                self.layout.addWidget(Label('  kernel_init: '),1,4,1,1)
                self.layout.addWidget(self.kernel_initializer,1,5,1,1)
                self.layout.addWidget(Label('bias_init: '),1,6,1,1)
                self.layout.addWidget(self.bias_initializer,1,7,1,1)
                self.layout.addWidget(self.use_bias,2,0,1,1)
                self.layout.addWidget(Label('Padding: '),2,1,1,1)
                self.layout.addWidget(self.padding,2,2,1,1)
                self.layout.addWidget(Label('strides: '),2,3,1,1)
                self.layout.addWidget(self.strides,2,4,1,1)
                self.layout.addWidget(Label('regularizers :     kernel:'),3,0,1,2)
                self.layout.addWidget(self.kernel_regularizer,3,2,1,1)
                self.layout.addWidget(Label('    bias:'),3,3,1,1)
                self.layout.addWidget(self.bias_regularizer,3,4,1,1)
                self.layout.addWidget(Label('    activity:'),3,5,1,1)
                self.layout.addWidget(self.activity_regularizer,3,6,1,1)
                self.layout.addWidget(Label('Constraint:         kernel:'),4,0,1,2)
                self.layout.addWidget(self.kernel_constraint,4,2,1,1)
                self.layout.addWidget(Label('    bias:'),4,3,1,1)
                self.layout.addWidget(self.bias_constraint,4,4,1,1)

                

        def check_submit(self): # check if every necessary field / arg is completed
            return True

        def getArgs(self):

            if not self.check_submit:
                raise Exception('not all arguments filled')

            args = []
            
            if self.blockType == 'Input':
                args.append((int(i) for i in self.inputShape.text().split(',')))

            elif self.blockType == 'Embedding Layer':
                args.append(int(self.input_dim.text()))
                args.append(int(self.output_dim.text()))
                args.append(self.initializer.currentText())
                args.append(self.regularizer.currentText())
                args.append(self.mask_zero.isChecked())
                args.append(None if self.input_length.text()=='' else self.input_length.text())
                args.append(self.constraint.currentText())

            elif self.blockType == 'Dense Layer':
                args.append(int(self.units.text()))
                args.append(self.activation.currentText())
                args.append(self.use_bias.isChecked())
                args.append(self.kernel_initializer.currentText())
                args.append(self.bias_initializer.currentText())
                args.append(self.kernel_regularizer.currentText())
                args.append(self.bias_regularizer.currentText())
                args.append(self.activity_regularizer.currentText())
                args.append(self.kernel_constraint.currentText())
                args.append(self.bias_constraint.currentText())

            elif self.blockType == 'Dropout Layer':
                args.append(self.rate.value())

            elif self.blockType == 'Masking Layer':
                args.append(self.mask_value.value())

            elif self.blockType == 'Activation Layer':
                args.append(self.activation.currentText())

            args = [None if i == 'None' else i for i in args]

            return args
            

    class ModelCompilerBlock(QLabel):
        'A custom Widget that represent the Model.compile function'
        def __init__(self):
            super().__init__()
            self.layout = QGridLayout()
            self.layout.setAlignment(Qt.AlignLeft)

            self.setLayout(self.layout)
            self.setStyleSheet('background-color:#303030;color:white;')
            
            self.setFrameStyle(QFrame.StyledPanel)
            self.setFrameShadow(QFrame.Sunken)
            self.setFrameShape(QFrame.StyledPanel)
            self.setFixedHeight(int(screen_height/6))

            label = QLabel('compiler')
            label.setStyleSheet('font-size:30px;')
            self.optimizer = QComboBox()
            self.optimizer.addItems(['adam','rsmprop','sgd','adadelta','adagrad','adamax','nadam','ftrl'])

            self.loss = QComboBox()
            self.loss.addItems(['None','mean_squared_error','mean_absolute_error','mean_absolute_percentage_error'
            ,'mean_squared_logarithmic_error','cosine_similarity','huber','log_cosh','binary_crossentropy'
            ,'categorical_crossentropy','sparse_categorical_crossentropy','poisson','kl_divergence','hinge'
            ,'squared_hinge','categorical_hinge'])

            
            self.metricButton = QToolButton()
            self.metricButton.setText('None')
            self.metricButton.setPopupMode(QToolButton.InstantPopup)

            metricsMenu = QMenu(self.metricButton)
            self.metricButton.setMenu(metricsMenu)

            self.metrics = []

            def setMetrics(metric:str):
                if metric not in self.metrics:
                    self.metrics.append(metric)
                else:
                    self.metrics.remove(metric)
                self.metricButton.setText(str(self.metrics).replace("'",''))
                    
            metric = ['Accuracy','BinaryAccuracy','CategoricalAccuracy','TopKCategoricalAccuracy'
            ,'SparseTopKCategoricalAccuracy','BinaryCrossentropy','CategoricalCrossentropy'
            ,'SparseCategoricalCrossentropy','KLDivergence','Poisson','MeanSquaredError'
            ,'RootMeanSquaredError','MeanAbsoluteError','MeanAbsolutePercentageError'
            ,'MeanSquaredLogarithmicError','CosineSimilarity','LogCoshError','AUC','Precision'
            ,'Recall','TruePositives','TrueNegatives','FalsePositives','FalseNegatives'
            ,'PrecisionAtRecall','SensitivityAtSpecificity','SpecificityAtSensitivity','MeanIoU'
            ,'Hinge','SquaredHinge','CategoricalHinge']
            for i in metric:
                action = metricsMenu.addAction(i)
                action.setCheckable(True)
                exec(f"action.triggered.connect(lambda:setMetrics('{i}'))",locals())

            self.stepsPerExec = QSpinBox()
            self.stepsPerExec.setRange(1,10)

            self.layout.addWidget(label,0,0,1,2)
            self.layout.addWidget(QLabel('optimizer: '),1,0,1,1)
            self.layout.addWidget(self.optimizer,1,1,1,1)
            self.layout.addWidget(QLabel('   loss: '),1,2,1,1)
            self.layout.addWidget(self.loss,1,3,1,1)
            self.layout.addWidget(QLabel('   Metrics: '),1,4,1,1)
            self.layout.addWidget(self.metricButton,1,5,1,1)
            self.layout.addWidget(QLabel('Steps per execution: '),2,0,1,2)
            self.layout.addWidget(self.stepsPerExec,2,2,1,1)

#################################################################################################################################################################

    frameLayout = QVBoxLayout()
    frameLayout.setAlignment(Qt.AlignTop)

    icon_size = int(screen_height/18)

    mainLayout = QHBoxLayout()
    ######################## menu bar ###################################################################################################################

    bar = QToolBar()
    bar.setFixedHeight(int(screen_height/20))
    frameLayout.addWidget(bar)
    
    frameLayout.addLayout(mainLayout)

    bar.addAction('run')

##################### left menu widget ###################################################################################

    def setMenuChecked(index):
        def setCheckFalse():
            left_menuButton.setChecked(False)
            left_codeButton.setChecked(False)

        if index == 0:
            setCheckFalse()
            left_menuButton.setChecked(True)
            left_code_widget.hide()
            left_menu_mainWidget.show()

        if index == 2:
            setCheckFalse()
            left_codeButton.setChecked(True)
            left_menu_mainWidget.hide()
            left_code_widget.show()

    left_menu_widget = QWidget()
    left_menu_widget.setFixedWidth(int(screen_width/5))
    left_menu_layout = QGridLayout()
    left_menu_widget.setLayout(left_menu_layout)

    
    left_menuButton  = QPushButton()
    left_menuButton.setToolTip('Menu')
    left_menuButton.setIcon(QIcon(os.path.join(image_path,'menu.png')))
    left_menuButton.setIconSize(QSize(icon_size,icon_size))
    left_menuButton.setFlat(True)
    left_menuButton.setCheckable(True)
    left_menuButton.setChecked(True)
    left_menuButton.clicked.connect(lambda:setMenuChecked(0))
    left_menu_layout.addWidget(left_menuButton,0,0,1,1)
    
    left_codeButton = QPushButton()
    left_codeButton.setToolTip('code template')
    left_codeButton.setIcon(QIcon(os.path.join(image_path,'code.png')))
    left_codeButton.setIconSize(QSize(icon_size,icon_size))
    left_codeButton.setFlat(True)
    left_codeButton.setCheckable(True)
    left_codeButton.clicked.connect(lambda:setMenuChecked(2))
    left_menu_layout.addWidget(left_codeButton,1,0,1,1)


    # menu

    left_menu_mainWidget = QWidget()
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setWidget(left_menu_mainWidget)
    #left_menu_mainWidget.setStyleSheet('background-color:#303030;')
    left_menu_layout.addWidget(scroll,0,1,10,6)
    

    # first menu layou
    left_menu_mainlayout = QVBoxLayout(left_menu_mainWidget)
    left_menu_mainlayout.setAlignment(Qt.AlignTop)
    left_menu_mainWidget.setLayout(left_menu_mainlayout)

    layerLabel = QLabel('Layers')
    layerLabel.setStyleSheet('font-size:40px;')
    left_menu_mainlayout.addWidget(layerLabel)

    left_menu_mainlayout.addSpacing(int(screen_height/60))

    layers = {'Sequential Model':'Sequential groups a linear stack of layers into a tf.keras.Model and provides training and inference features on this model.'
    ,'Input':'Input is used to instantiate a Keras tensor.'
    ,'Embedding Layer':'Embedding layer: Categorical, text'
    ,'Dense Layer':'Dense layer: All scenario'
    ,'Dropout Layer':'Dropout layer: prevent over fitting'
    ,'LSTM Layer':'LSTM layer: text, time series'
    ,'Activation Layer': 'Applies an activation function to an output.'
    ,'Masking Layer': 'Masks a sequence by using a mask value to skip timesteps.'
    }

    for x,y in layers.items():
        label = DraggableLabel(x)
        label.setToolTip(y)
        left_menu_mainlayout.addWidget(label)

    def expend_shrink(button,widget):
        text = button.text()
        if '▶' in text:
            text = text.replace('▶','▼')
        else:
            text = text.replace('▼', '▶')

        button.setText(text)

        if widget.isHidden():
            widget.show()
        else:
            widget.hide()


    conv_layers = {'Conv1D Layer':'1D convolution layer'}
    conv_widget = QWidget()
    conv_layout = QVBoxLayout()
    conv_widget.setLayout(conv_layout)
    conv_widget.hide()

    for x,y in conv_layers.items():
        label = DraggableLabel(x)
        label.setToolTip(y)
        conv_layout.addWidget(label)

    cov_button = QPushButton('▶ Convolution Layers')
    cov_button.setStyleSheet('text-align:left;font-size: 20px')
    cov_button.setFlat(True)
    cov_button.clicked.connect(lambda:expend_shrink(cov_button,conv_widget))
    left_menu_mainlayout.addWidget(cov_button)
    left_menu_mainlayout.addWidget(conv_widget)


    




    mainLayout.addWidget(left_menu_widget)


    # code

    left_code_widget = QWidget()
    left_code_widget.hide()
    left_menu_layout.addWidget(left_code_widget,0,1,10,6)
    # code template layout
    left_code_layout = QVBoxLayout()
    left_code_layout.setAlignment(Qt.AlignTop)
    codeLabel = QLabel('Code Template')
    codeLabel.setStyleSheet('font-size:30px;')
    left_code_layout.addWidget(codeLabel)
    left_code_widget.setLayout(left_code_layout)

##################### block scroll area #########################################################################

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    vsb = scroll.verticalScrollBar()
    vsb.rangeChanged.connect(lambda:vsb.setValue(vsb.maximum()))

    areaLayout = QVBoxLayout()
    areaLayout.setAlignment(Qt.AlignTop)

    areaWidget = DropAcceptWidget(areaLayout)

    scroll.setWidget(areaWidget)


    genesisblock  = ModelCompilerBlock()
    keras_model['compiler'] = genesisblock

    areaLayout.addWidget(genesisblock)

    mainLayout.addWidget(scroll)

########################## right menu widget ######################################################################

    right_menu_widget = QWidget()
    right_menu_widget.setFixedWidth(int(screen_width/4))
    right_menu_layout = QGridLayout()
    right_menu_widget.setLayout(right_menu_layout)

    BuildButton = QPushButton('Build Model')
    BuildButton.clicked.connect(Build_and_run_keras)
    right_menu_layout.addWidget(BuildButton)
    mainLayout.addWidget(right_menu_widget)

    return frameLayout



# EEEEEEEEEEEEEEEEEEEEEE                                                                                  tttt                              
# E::::::::::::::::::::E                                                                               ttt:::t                              
# E::::::::::::::::::::E                                                                               t:::::t                              
# EE::::::EEEEEEEEE::::E                                                                               t:::::t                              
#   E:::::E       EEEEEExxxxxxx      xxxxxxx eeeeeeeeeeee        ccccccccccccccccuuuuuu    uuuuuuttttttt:::::ttttttt        eeeeeeeeeeee    
#   E:::::E              x:::::x    x:::::xee::::::::::::ee    cc:::::::::::::::cu::::u    u::::ut:::::::::::::::::t      ee::::::::::::ee  
#   E::::::EEEEEEEEEE     x:::::x  x:::::xe::::::eeeee:::::ee c:::::::::::::::::cu::::u    u::::ut:::::::::::::::::t     e::::::eeeee:::::ee
#   E:::::::::::::::E      x:::::xx:::::xe::::::e     e:::::ec:::::::cccccc:::::cu::::u    u::::utttttt:::::::tttttt    e::::::e     e:::::e
#   E:::::::::::::::E       x::::::::::x e:::::::eeeee::::::ec::::::c     cccccccu::::u    u::::u      t:::::t          e:::::::eeeee::::::e
#   E::::::EEEEEEEEEE        x::::::::x  e:::::::::::::::::e c:::::c             u::::u    u::::u      t:::::t          e:::::::::::::::::e 
#   E:::::E                  x::::::::x  e::::::eeeeeeeeeee  c:::::c             u::::u    u::::u      t:::::t          e::::::eeeeeeeeeee  
#   E:::::E       EEEEEE    x::::::::::x e:::::::e           c::::::c     cccccccu:::::uuuu:::::u      t:::::t    tttttte:::::::e           
# EE::::::EEEEEEEE:::::E   x:::::xx:::::xe::::::::e          c:::::::cccccc:::::cu:::::::::::::::uu    t::::::tttt:::::te::::::::e          
# E::::::::::::::::::::E  x:::::x  x:::::xe::::::::eeeeeeee   c:::::::::::::::::c u:::::::::::::::u    tt::::::::::::::t e::::::::eeeeeeee  
# E::::::::::::::::::::E x:::::x    x:::::xee:::::::::::::e    cc:::::::::::::::c  uu::::::::uu:::u      tt:::::::::::tt  ee:::::::::::::e  
# EEEEEEEEEEEEEEEEEEEEEExxxxxxx      xxxxxxx eeeeeeeeeeeeee      cccccccccccccccc    uuuuuuuu  uuuu        ttttttttttt      eeeeeeeeeeeeee  
            
def main():
    print('in construction')
    global plt_setting, saved_file, current_file_name, settings, mainWidget, prjdict, keras_model

######################### handle sys argvs ###########################################################################################################

    print('argvs:'+str(sys.argv))

    if '-help' in sys.argv or '--help' in sys.argv or 'help' in sys.argv:
        print("""Usage: py-office-learn [<option>...]
py-office-learn cross-platform spreadsheet based on keras and numpy for easy machine learning\n
for more information, visit https://github.com/YC-Lammy/py-office-learn
        """)
        return 0


    if '-uninstall' in sys.argv or '--uninstall' in sys.argv or 'uninstall' in sys.argv:

        print('after this operation, py-office-sheet will be uninstalled')

        ans = input('\r\nare you sure you want to uninstall? y/n')

        if ans not in ('y','n'):
            while ans not in ('y','n'): # loop until user anser
                ans = input('are you sure you want to uninstall? y/n')

        if ans == 'y':
            from subprocess import run
            run([sys.executable,'-m','pip','uninstall','py-office-sheet'])
        elif ans == 'n':
            print('\r\n action abort.')
        
        return 0

######################### set up GUI ######################################################################################################################## 
    file = None

    for i in sys.argv:
        if '.pdobj' in i or '.npobj' in i or '.csv' in i:
            file = i 

    saved_file = True #state if the file is modified, notice user to save file
    current_file_name = None #current file name is the file user opened using open file function
    plt_setting = {'set':False}
    settings = {}
    prjdict = {}
    keras_model = {'sequential':False,'layers':[],'compiler':None,'trainer':None,'input_shape':(1,),'model':None}


    def closeEventHandler(event): # this function is called when user tries to close app, line 559

        if saved_file == True: # is nothing is modified, quit normally
            event.accept()
        else:
            m = QMessageBox()
            m.setWindowTitle('file not save')
            ret = m.question(mainWidget,'', "Exit without saving?", m.Yes | m.No,m.No) # default as No

            if ret == m.Yes:
                event.accept() # if user choose yes, exit without saving
            else:
                event.ignore() # when user choose no, stop exit event


    app = QApplication(['-style fusion']+sys.argv)

    screensize= app.primaryScreen().size()
    screen_height = screensize.height()
    screen_width = screensize.width()

    mainWidget = QWidget() # spreedsheet returns a layout
    layout = pyofficelearn(screen_width,screen_height)
    mainWidget.setLayout(layout)
    mainWidget.closeEvent = closeEventHandler # reassign the app's close event
    mainWidget.setWindowState(Qt.WindowMaximized)
    mainWidget.setWindowTitle('py-office-learn') # actual title not desided
    mainWidget.show()
    app.exec_()

    jsonpath = os.path.join(getfile(pyOfficeLearn).replace('__init__.py',''),'config.json')

    with open(jsonpath,'w') as f:
        f.write(json_dumps(settings))
        f.close()
    
    gc.collect()
    sys.exit()

if __name__ == '__main__':
    main()