#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem,QDialog
from PyQt5 import QtCore
import main_window
import os
import re
import sys
import dialog
def QuitButton():
    QApplication.quit()


def DoubleClickToStopEdit(ui):
    ui.treeWidget.closePersistentEditor(ui.treeWidget.currentItem(),ui.treeWidget.currentColumn())
    return 
def DoubleClickToEdit(ui):
    ui.treeWidget.openPersistentEditor(ui.treeWidget.currentItem(),ui.treeWidget.currentColumn())
    return 

def addTreeitemClass(ui,title):
    _translate = QtCore.QCoreApplication.translate
    for i in range(ui.treeWidget.topLevelItemCount()):
        if title == ui.treeWidget.topLevelItem(i).text(0):
            return
    QTreeWidgetItem(ui.treeWidget)
    ui.treeWidget.topLevelItem(ui.treeWidget.topLevelItemCount()-1).setText(0, _translate("MainWindow", title))

def addTreeitemContent(ui,title,parameter,value,note):
    _translate = QtCore.QCoreApplication.translate
    for i in range(ui.treeWidget.topLevelItemCount()):
        if title == ui.treeWidget.topLevelItem(i).text(0):
            for j in  range(ui.treeWidget.topLevelItem(i).childCount()):
                if ui.treeWidget.topLevelItem(i).child(j).text(0) == parameter:
                    ui.treeWidget.topLevelItem(i).child(j).setText(1,_translate("MainWindow",value))
                    ui.treeWidget.topLevelItem(i).child(j).setText(2,_translate("MainWindow",note))
                    pass
            QTreeWidgetItem(ui.treeWidget.topLevelItem(i))
            ui.treeWidget.topLevelItem(i).child(ui.treeWidget.topLevelItem(i).childCount()-1).setText(0,_translate("MainWindow",parameter))
            ui.treeWidget.topLevelItem(i).child(ui.treeWidget.topLevelItem(i).childCount()-1).setText(1,_translate("MainWindow",value))
            ui.treeWidget.topLevelItem(i).child(ui.treeWidget.topLevelItem(i).childCount()-1).setText(2,_translate("MainWindow",note))
            ui.treeWidget.expandAll()
            return
    addTreeitemClass(ui,title)
    addTreeitemContent(ui,title,parameter,value,note)

def ClickToSaveFile(ui):
    f=open(ui.lineEdit.text(), "a+")
    f.seek(0)
    f.truncate()   #清空文件
    for i in range(ui.treeWidget.topLevelItemCount()):
        content = ""
        content = ui.treeWidget.topLevelItem(i).text(0)
        content = '-'*10+content+'-'*10+'\n'
        f.write(content)
        for j in range(ui.treeWidget.topLevelItem(i).childCount()):
            content = ""
            parameter = ui.treeWidget.topLevelItem(i).child(j).text(0)
            value = ui.treeWidget.topLevelItem(i).child(j).text(1)
            note = ui.treeWidget.topLevelItem(i).child(j).text(2)
            if note == "":
                content = parameter +'  =  ' + value +'\n'
            else:
                content = parameter +'  =  ' + value +'  '+ '#'+ note + '\n'
            f.write(content)
    f.close()
    ui.label_2.setText("状态：参数已保存")


def ClickToLoadFile(ui):
    ui.treeWidget.clear()
    title=""
    file_path=ui.lineEdit.text()
    try :
        with open(file_path,'r') as file:
            for line in file:
                match  = re.search(r"--",line)
                parameter=""
                value=""
                note=""
                if(match):
                    match = re.search(r"-(\w+?)-",line)
                    title = line[match.span()[0]+1:match.span()[1]-1]
                    addTreeitemClass(ui,title)
                else:
                    line = line.replace(" ", "")
                    note_match = re.search(r"#",line)
                    if(note_match):
                        note = line[note_match.span()[0]+1:-1]
                        value_match = re.search(r"=",line)
                        parameter = line[0:value_match.span()[0]]
                        value = line[value_match.span()[1]:note_match.span()[0]]
                    else:
                        value_match = re.search(r"=",line)
                        parameter = line[0:value_match.span()[0]]
                        value = line[value_match.span()[1]:-1]
                    addTreeitemContent(ui,title,parameter,value,note)
        ui.label_2.setText("状态：参数已加载")

    except Exception as e:
        ui.label_2.setText("状态：文件路径不存在")

def ClickToStartSim(ui):
    cmd = 'gnome-terminal -t "roscore" -x bash -c "rosrun rcc rcc -c {}"'.format(ui.lineEdit.text())
    os.system(cmd)
    ui.label_2.setText("状态：仿真程序已启动")
    ui.pushButton.setDisabled(True)
    ui.pushButton_2.setDisabled(False)
def ClickToStopSim(ui):
    def end_program(pro_name):
        os.system('%s%s' % ("killall ",pro_name))
    end_program('rcc')
    ui.pushButton_2.setDisabled(True)
    ui.pushButton.setDisabled(False)

def ClickToAddValue(ui):
    title=ui.lineEdit_2.text().replace(" ","")
    parameter=ui.lineEdit_3.text().replace(" ","")
    value=ui.lineEdit_4.text().replace(" ","")
    note=ui.lineEdit_5.text().replace(" ","")
    if title =="" or parameter=="" or value =="":
        ui.label_2.setText("状态：请检查数据合法性,请注意数据中不允许有空格")
        return 
    addTreeitemContent(ui,title,parameter,value,note)
    ui.label_2.setText("状态：数据已添加成功 {}->{}={}#{}".format(title,parameter,value,note))


if __name__ == '__main__':
    _translate = QtCore.QCoreApplication.translate
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.treeWidget.itemDoubleClicked.connect(lambda:DoubleClickToEdit(ui))
    ui.treeWidget.itemChanged.connect(lambda:DoubleClickToStopEdit(ui))
    ui.action_5.triggered.connect(QuitButton)
    ui.action_3.triggered.connect(lambda:ClickToSaveFile(ui))
    ui.action_2.triggered.connect(lambda:ClickToLoadFile(ui))
    ui.pushButton_4.clicked.connect(lambda:ClickToLoadFile(ui))
    ui.pushButton_5.clicked.connect(lambda:ClickToSaveFile(ui))
    ui.pushButton.clicked.connect(lambda:ClickToStartSim(ui))
    ui.pushButton_2.clicked.connect(lambda :ClickToStopSim(ui))
    ui.pushButton_3.clicked.connect(lambda :ClickToAddValue(ui))
    sys.exit(app.exec_())
