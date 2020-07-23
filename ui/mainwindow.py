# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 488)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 617))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 576))
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(1024, 576))
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.home)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.willkommen = QtWidgets.QLabel(self.home)
        self.willkommen.setScaledContents(False)
        self.willkommen.setAlignment(QtCore.Qt.AlignCenter)
        self.willkommen.setObjectName("willkommen")
        self.verticalLayout_2.addWidget(self.willkommen)
        self.willkommenPic = QtWidgets.QLabel(self.home)
        self.willkommenPic.setBaseSize(QtCore.QSize(0, 0))
        self.willkommenPic.setAutoFillBackground(False)
        self.willkommenPic.setText("")
        self.willkommenPic.setPixmap(QtGui.QPixmap(":/bilder/willkommen_pic.png"))
        self.willkommenPic.setScaledContents(True)
        self.willkommenPic.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.willkommenPic.setWordWrap(False)
        self.willkommenPic.setIndent(0)
        self.willkommenPic.setObjectName("willkommenPic")
        self.verticalLayout_2.addWidget(self.willkommenPic)
        self.labeleins = QtWidgets.QLabel(self.home)
        self.labeleins.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labeleins.setObjectName("labeleins")
        self.verticalLayout_2.addWidget(self.labeleins)
        self.nichtMehrAktuell = QtWidgets.QLabel(self.home)
        self.nichtMehrAktuell.setText("")
        self.nichtMehrAktuell.setScaledContents(False)
        self.nichtMehrAktuell.setAlignment(QtCore.Qt.AlignCenter)
        self.nichtMehrAktuell.setObjectName("nichtMehrAktuell")
        self.verticalLayout_2.addWidget(self.nichtMehrAktuell)
        self.tabWidget.addTab(self.home, "")
        self.eintrag = QtWidgets.QWidget()
        self.eintrag.setObjectName("eintrag")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.eintrag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verschWerte = QtWidgets.QGridLayout()
        self.verschWerte.setContentsMargins(-1, -1, 0, -1)
        self.verschWerte.setHorizontalSpacing(6)
        self.verschWerte.setObjectName("verschWerte")
        self.formGewicht = QtWidgets.QFormLayout()
        self.formGewicht.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formGewicht.setContentsMargins(10, 10, 10, 10)
        self.formGewicht.setObjectName("formGewicht")
        self.ueberschrift = QtWidgets.QLabel(self.eintrag)
        self.ueberschrift.setTextFormat(QtCore.Qt.RichText)
        self.ueberschrift.setObjectName("ueberschrift")
        self.formGewicht.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.ueberschrift)
        self.gewichtlabel = QtWidgets.QLabel(self.eintrag)
        self.gewichtlabel.setObjectName("gewichtlabel")
        self.formGewicht.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gewichtlabel)
        self.gewicht = QtWidgets.QLabel(self.eintrag)
        self.gewicht.setObjectName("gewicht")
        self.formGewicht.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gewicht)
        self.dateGewichtLabel = QtWidgets.QLabel(self.eintrag)
        self.dateGewichtLabel.setObjectName("dateGewichtLabel")
        self.formGewicht.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateGewichtLabel)
        self.eintragGewicht = QtWidgets.QPushButton(self.eintrag)
        self.eintragGewicht.setObjectName("eintragGewicht")
        self.formGewicht.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.eintragGewicht)
        self.gewichtLetzt = QtWidgets.QLabel(self.eintrag)
        self.gewichtLetzt.setObjectName("gewichtLetzt")
        self.formGewicht.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gewichtLetzt)
        self.verschWerte.addLayout(self.formGewicht, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verschWerte.addItem(spacerItem, 0, 1, 1, 1)
        self.formTrainingsplan = QtWidgets.QVBoxLayout()
        self.formTrainingsplan.setContentsMargins(10, 10, 10, 10)
        self.formTrainingsplan.setObjectName("formTrainingsplan")
        self.label_6 = QtWidgets.QLabel(self.eintrag)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formTrainingsplan.addWidget(self.label_6)
        self.trainingsplan = QtWidgets.QTextEdit(self.eintrag)
        self.trainingsplan.setObjectName("trainingsplan")
        self.formTrainingsplan.addWidget(self.trainingsplan)
        self.eintragPlan = QtWidgets.QPushButton(self.eintrag)
        self.eintragPlan.setObjectName("eintragPlan")
        self.formTrainingsplan.addWidget(self.eintragPlan)
        self.eintragPlanHinweis = QtWidgets.QLabel(self.eintrag)
        self.eintragPlanHinweis.setAlignment(QtCore.Qt.AlignCenter)
        self.eintragPlanHinweis.setObjectName("eintragPlanHinweis")
        self.formTrainingsplan.addWidget(self.eintragPlanHinweis)
        self.verschWerte.addLayout(self.formTrainingsplan, 0, 2, 3, 1)
        self.formKfa = QtWidgets.QFormLayout()
        self.formKfa.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formKfa.setContentsMargins(10, 10, 10, 10)
        self.formKfa.setObjectName("formKfa")
        self.label_11 = QtWidgets.QLabel(self.eintrag)
        self.label_11.setObjectName("label_11")
        self.formKfa.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.kfa = QtWidgets.QLabel(self.eintrag)
        self.kfa.setScaledContents(False)
        self.kfa.setWordWrap(False)
        self.kfa.setObjectName("kfa")
        self.formKfa.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kfa)
        self.label_13 = QtWidgets.QLabel(self.eintrag)
        self.label_13.setObjectName("label_13")
        self.formKfa.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.kfaLetzt = QtWidgets.QLabel(self.eintrag)
        self.kfaLetzt.setObjectName("kfaLetzt")
        self.formKfa.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kfaLetzt)
        self.eintragKfa = QtWidgets.QPushButton(self.eintrag)
        self.eintragKfa.setObjectName("eintragKfa")
        self.formKfa.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.eintragKfa)
        self.label_10 = QtWidgets.QLabel(self.eintrag)
        self.label_10.setObjectName("label_10")
        self.formKfa.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        self.verschWerte.addLayout(self.formKfa, 2, 0, 1, 1)
        self.formUmfaenge = QtWidgets.QFormLayout()
        self.formUmfaenge.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formUmfaenge.setContentsMargins(10, 10, 10, 10)
        self.formUmfaenge.setObjectName("formUmfaenge")
        self.label = QtWidgets.QLabel(self.eintrag)
        self.label.setObjectName("label")
        self.formUmfaenge.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.eintrag)
        self.label_2.setObjectName("label_2")
        self.formUmfaenge.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.eintrag)
        self.label_3.setObjectName("label_3")
        self.formUmfaenge.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.eintrag)
        self.label_4.setObjectName("label_4")
        self.formUmfaenge.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.eintrag)
        self.label_5.setObjectName("label_5")
        self.formUmfaenge.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.eintragUmfaenge = QtWidgets.QPushButton(self.eintrag)
        self.eintragUmfaenge.setObjectName("eintragUmfaenge")
        self.formUmfaenge.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.eintragUmfaenge)
        self.label_7 = QtWidgets.QLabel(self.eintrag)
        self.label_7.setObjectName("label_7")
        self.formUmfaenge.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.eintrag)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.formUmfaenge.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.oberschenkel = QtWidgets.QLabel(self.eintrag)
        self.oberschenkel.setObjectName("oberschenkel")
        self.formUmfaenge.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.oberschenkel)
        self.bauch = QtWidgets.QLabel(self.eintrag)
        self.bauch.setObjectName("bauch")
        self.formUmfaenge.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bauch)
        self.huefte = QtWidgets.QLabel(self.eintrag)
        self.huefte.setObjectName("huefte")
        self.formUmfaenge.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.huefte)
        self.brust = QtWidgets.QLabel(self.eintrag)
        self.brust.setObjectName("brust")
        self.formUmfaenge.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.brust)
        self.bizeps = QtWidgets.QLabel(self.eintrag)
        self.bizeps.setObjectName("bizeps")
        self.formUmfaenge.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bizeps)
        self.umfaengeLetzt = QtWidgets.QLabel(self.eintrag)
        self.umfaengeLetzt.setObjectName("umfaengeLetzt")
        self.formUmfaenge.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.umfaengeLetzt)
        self.verschWerte.addLayout(self.formUmfaenge, 0, 4, 2, 1)
        self.ernaehrung = QtWidgets.QFormLayout()
        self.ernaehrung.setFormAlignment(QtCore.Qt.AlignCenter)
        self.ernaehrung.setContentsMargins(10, 10, 10, 10)
        self.ernaehrung.setObjectName("ernaehrung")
        self.label3 = QtWidgets.QLabel(self.eintrag)
        self.label3.setObjectName("label3")
        self.ernaehrung.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.label4 = QtWidgets.QLabel(self.eintrag)
        self.label4.setObjectName("label4")
        self.ernaehrung.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label4)
        self.soos = QtWidgets.QLabel(self.eintrag)
        self.soos.setObjectName("soos")
        self.ernaehrung.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.soos)
        self.label2 = QtWidgets.QLabel(self.eintrag)
        self.label2.setObjectName("label2")
        self.ernaehrung.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.eintragErnaehrung = QtWidgets.QPushButton(self.eintrag)
        self.eintragErnaehrung.setObjectName("eintragErnaehrung")
        self.ernaehrung.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.eintragErnaehrung)
        self.label1 = QtWidgets.QLabel(self.eintrag)
        self.label1.setObjectName("label1")
        self.ernaehrung.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.gesamtkcal = QtWidgets.QLabel(self.eintrag)
        self.gesamtkcal.setObjectName("gesamtkcal")
        self.ernaehrung.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gesamtkcal)
        self.kohlenhydrate = QtWidgets.QLabel(self.eintrag)
        self.kohlenhydrate.setObjectName("kohlenhydrate")
        self.ernaehrung.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kohlenhydrate)
        self.protein = QtWidgets.QLabel(self.eintrag)
        self.protein.setObjectName("protein")
        self.ernaehrung.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.protein)
        self.fett = QtWidgets.QLabel(self.eintrag)
        self.fett.setObjectName("fett")
        self.ernaehrung.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fett)
        self.ernaehrungLetzt = QtWidgets.QLabel(self.eintrag)
        self.ernaehrungLetzt.setObjectName("ernaehrungLetzt")
        self.ernaehrung.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ernaehrungLetzt)
        self.label_9 = QtWidgets.QLabel(self.eintrag)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName("label_9")
        self.ernaehrung.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.verschWerte.addLayout(self.ernaehrung, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verschWerte.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.verschWerte)
        self.tabWidget.addTab(self.eintrag, "")
        self.graphen = QtWidgets.QWidget()
        self.graphen.setObjectName("graphen")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.graphen)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verschGraphen = QtWidgets.QGridLayout()
        self.verschGraphen.setObjectName("verschGraphen")
        self.brustCheck = QtWidgets.QCheckBox(self.graphen)
        self.brustCheck.setObjectName("brustCheck")
        self.verschGraphen.addWidget(self.brustCheck, 5, 1, 1, 1)
        self.oberschenkelGraph = QtWidgets.QWidget(self.graphen)
        self.oberschenkelGraph.setObjectName("oberschenkelGraph")
        self.verschGraphen.addWidget(self.oberschenkelGraph, 1, 0, 1, 1)
        self.kfaCheck = QtWidgets.QCheckBox(self.graphen)
        self.kfaCheck.setObjectName("kfaCheck")
        self.verschGraphen.addWidget(self.kfaCheck, 1, 1, 1, 1)
        self.gewichtGraph = QtWidgets.QWidget(self.graphen)
        self.gewichtGraph.setObjectName("gewichtGraph")
        self.verschGraphen.addWidget(self.gewichtGraph, 0, 0, 1, 1)
        self.bizepsCheck = QtWidgets.QCheckBox(self.graphen)
        self.bizepsCheck.setObjectName("bizepsCheck")
        self.verschGraphen.addWidget(self.bizepsCheck, 6, 1, 1, 1)
        self.gewichtCheck = QtWidgets.QCheckBox(self.graphen)
        self.gewichtCheck.setChecked(False)
        self.gewichtCheck.setTristate(False)
        self.gewichtCheck.setObjectName("gewichtCheck")
        self.verschGraphen.addWidget(self.gewichtCheck, 0, 1, 1, 1)
        self.bauchCheck = QtWidgets.QCheckBox(self.graphen)
        self.bauchCheck.setObjectName("bauchCheck")
        self.verschGraphen.addWidget(self.bauchCheck, 3, 1, 1, 1)
        self.huefteGraph = QtWidgets.QWidget(self.graphen)
        self.huefteGraph.setObjectName("huefteGraph")
        self.verschGraphen.addWidget(self.huefteGraph, 2, 0, 1, 1)
        self.oberschenkelCheck = QtWidgets.QCheckBox(self.graphen)
        self.oberschenkelCheck.setObjectName("oberschenkelCheck")
        self.verschGraphen.addWidget(self.oberschenkelCheck, 2, 1, 1, 1)
        self.huefteCheck = QtWidgets.QCheckBox(self.graphen)
        self.huefteCheck.setObjectName("huefteCheck")
        self.verschGraphen.addWidget(self.huefteCheck, 4, 1, 1, 1)
        self.kfaGraph = QtWidgets.QWidget(self.graphen)
        self.kfaGraph.setObjectName("kfaGraph")
        self.verschGraphen.addWidget(self.kfaGraph, 0, 2, 1, 1)
        self.bauchGraph = QtWidgets.QWidget(self.graphen)
        self.bauchGraph.setObjectName("bauchGraph")
        self.verschGraphen.addWidget(self.bauchGraph, 1, 2, 1, 1)
        self.brustGraph = QtWidgets.QWidget(self.graphen)
        self.brustGraph.setObjectName("brustGraph")
        self.verschGraphen.addWidget(self.brustGraph, 2, 2, 1, 1)
        self.bizepsGraph = QtWidgets.QWidget(self.graphen)
        self.bizepsGraph.setObjectName("bizepsGraph")
        self.verschGraphen.addWidget(self.bizepsGraph, 3, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.verschGraphen)
        self.tabWidget.addTab(self.graphen, "")
        self.berechnungen = QtWidgets.QWidget()
        self.berechnungen.setObjectName("berechnungen")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.berechnungen)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verschBerechnungen = QtWidgets.QGridLayout()
        self.verschBerechnungen.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verschBerechnungen.setContentsMargins(0, -1, -1, -1)
        self.verschBerechnungen.setVerticalSpacing(6)
        self.verschBerechnungen.setObjectName("verschBerechnungen")
        self.strongMan = QtWidgets.QLabel(self.berechnungen)
        self.strongMan.setMaximumSize(QtCore.QSize(161, 191))
        self.strongMan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.strongMan.setText("")
        self.strongMan.setPixmap(QtGui.QPixmap(":/bilder/home_pic.png"))
        self.strongMan.setScaledContents(True)
        self.strongMan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.strongMan.setWordWrap(False)
        self.strongMan.setObjectName("strongMan")
        self.verschBerechnungen.addWidget(self.strongMan, 1, 3, 1, 1)
        self.widget = QtWidgets.QWidget(self.berechnungen)
        self.widget.setObjectName("widget")
        self.verschBerechnungen.addWidget(self.widget, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verschBerechnungen.addItem(spacerItem2, 0, 3, 1, 1)
        self.formKfaRechner = QtWidgets.QFormLayout()
        self.formKfaRechner.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formKfaRechner.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formKfaRechner.setContentsMargins(10, 10, 10, 10)
        self.formKfaRechner.setObjectName("formKfaRechner")
        self.label_12 = QtWidgets.QLabel(self.berechnungen)
        self.label_12.setObjectName("label_12")
        self.formKfaRechner.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_15 = QtWidgets.QLabel(self.berechnungen)
        self.label_15.setObjectName("label_15")
        self.formKfaRechner.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.hfBrust = QtWidgets.QSpinBox(self.berechnungen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hfBrust.sizePolicy().hasHeightForWidth())
        self.hfBrust.setSizePolicy(sizePolicy)
        self.hfBrust.setMinimumSize(QtCore.QSize(206, 0))
        self.hfBrust.setObjectName("hfBrust")
        self.formKfaRechner.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hfBrust)
        self.label_16 = QtWidgets.QLabel(self.berechnungen)
        self.label_16.setObjectName("label_16")
        self.formKfaRechner.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.hfBauch = QtWidgets.QSpinBox(self.berechnungen)
        self.hfBauch.setMinimumSize(QtCore.QSize(206, 0))
        self.hfBauch.setObjectName("hfBauch")
        self.formKfaRechner.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hfBauch)
        self.label_14 = QtWidgets.QLabel(self.berechnungen)
        self.label_14.setObjectName("label_14")
        self.formKfaRechner.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.hfOberschenkel = QtWidgets.QSpinBox(self.berechnungen)
        self.hfOberschenkel.setMinimumSize(QtCore.QSize(206, 0))
        self.hfOberschenkel.setObjectName("hfOberschenkel")
        self.formKfaRechner.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hfOberschenkel)
        self.label_17 = QtWidgets.QLabel(self.berechnungen)
        self.label_17.setObjectName("label_17")
        self.formKfaRechner.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.alter = QtWidgets.QSpinBox(self.berechnungen)
        self.alter.setMinimumSize(QtCore.QSize(206, 0))
        self.alter.setObjectName("alter")
        self.formKfaRechner.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.alter)
        self.calcKfaButton = QtWidgets.QPushButton(self.berechnungen)
        self.calcKfaButton.setObjectName("calcKfaButton")
        self.formKfaRechner.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.calcKfaButton)
        self.calcKfaLabel = QtWidgets.QLabel(self.berechnungen)
        self.calcKfaLabel.setObjectName("calcKfaLabel")
        self.formKfaRechner.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.calcKfaLabel)
        self.frame = QtWidgets.QFrame(self.berechnungen)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formKfaRechner.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.verschBerechnungen.addLayout(self.formKfaRechner, 0, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verschBerechnungen.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.verschBerechnungen)
        self.tabWidget.addTab(self.berechnungen, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuInfo = QtWidgets.QMenu(self.menuBar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuInfo.addAction(self.actionInfo)
        self.menuBar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Irgendein langweiliger ToolTip</p></body></html>"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.willkommen.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Track to Fit</span></p></body></html>"))
        self.labeleins.setText(_translate("MainWindow", "<strong>Folgende Einträge sollten aktualisiert werden:</strong>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("MainWindow", "Home"))
        self.ueberschrift.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Gewicht (in kg)<br/></span><span style=\" font-size:10pt; font-weight:600;\">(wöchentlicher Durchschnitt)</span></p></body></html>"))
        self.gewichtlabel.setText(_translate("MainWindow", "Gewicht"))
        self.gewicht.setText(_translate("MainWindow", "TextLabel"))
        self.dateGewichtLabel.setText(_translate("MainWindow", "Letzter Eintrag:"))
        self.eintragGewicht.setText(_translate("MainWindow", "Eintragen"))
        self.gewichtLetzt.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Aktueller Trainingsplan</span></p></body></html>"))
        self.trainingsplan.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">siehe &quot;trainingsplan.txt&quot;-Datei</p></body></html>"))
        self.eintragPlan.setText(_translate("MainWindow", "Ändern"))
        self.eintragPlanHinweis.setText(_translate("MainWindow", "<strong>Trainingsplan geändert</strong>"))
        self.label_11.setText(_translate("MainWindow", "Kfa:"))
        self.kfa.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Letzter Eintrag: "))
        self.kfaLetzt.setText(_translate("MainWindow", "TextLabel"))
        self.eintragKfa.setText(_translate("MainWindow", "Eintragen"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Körperfettanteil (in %)</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Oberschenkel:"))
        self.label_2.setText(_translate("MainWindow", "Bauch:"))
        self.label_3.setText(_translate("MainWindow", "Hüfte:"))
        self.label_4.setText(_translate("MainWindow", "Brust:"))
        self.label_5.setText(_translate("MainWindow", "Bizeps:"))
        self.eintragUmfaenge.setText(_translate("MainWindow", "Eintragen"))
        self.label_7.setText(_translate("MainWindow", "Letzter Eintrag:"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Umfänge (in cm)</span></p></body></html>"))
        self.oberschenkel.setText(_translate("MainWindow", "TextLabel"))
        self.bauch.setText(_translate("MainWindow", "TextLabel"))
        self.huefte.setText(_translate("MainWindow", "TextLabel"))
        self.brust.setText(_translate("MainWindow", "TextLabel"))
        self.bizeps.setText(_translate("MainWindow", "TextLabel"))
        self.umfaengeLetzt.setText(_translate("MainWindow", "TextLabel"))
        self.label3.setText(_translate("MainWindow", "Gesamtkalorien (kcal):"))
        self.label4.setText(_translate("MainWindow", "Kohlenhydrate:"))
        self.soos.setText(_translate("MainWindow", "Proteine:"))
        self.label2.setText(_translate("MainWindow", "Fett:"))
        self.eintragErnaehrung.setText(_translate("MainWindow", "Eintragen"))
        self.label1.setText(_translate("MainWindow", "Letzte Änderung"))
        self.gesamtkcal.setText(_translate("MainWindow", "TextLabel"))
        self.kohlenhydrate.setText(_translate("MainWindow", "TextLabel"))
        self.protein.setText(_translate("MainWindow", "TextLabel"))
        self.fett.setText(_translate("MainWindow", "TextLabel"))
        self.ernaehrungLetzt.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ernährung (in g)</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eintrag), _translate("MainWindow", "Werte eintragen"))
        self.brustCheck.setText(_translate("MainWindow", "Brust"))
        self.kfaCheck.setText(_translate("MainWindow", "Körperfettanteil"))
        self.bizepsCheck.setText(_translate("MainWindow", "Bizeps"))
        self.gewichtCheck.setText(_translate("MainWindow", "Gewicht"))
        self.bauchCheck.setText(_translate("MainWindow", "Bauch"))
        self.oberschenkelCheck.setText(_translate("MainWindow", "Oberschenkel"))
        self.huefteCheck.setText(_translate("MainWindow", "Hüfte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphen), _translate("MainWindow", "Graphen"))
        self.label_12.setText(_translate("MainWindow", "<strong>KFA-Rechner:</strong>"))
        self.label_15.setText(_translate("MainWindow", "Hautfalte Brust"))
        self.label_16.setText(_translate("MainWindow", "Hautfalte Bauch"))
        self.label_14.setText(_translate("MainWindow", "Hautfalte Oberschenkel"))
        self.label_17.setText(_translate("MainWindow", "Alter"))
        self.calcKfaButton.setText(_translate("MainWindow", "Berechnen"))
        self.calcKfaLabel.setText(_translate("MainWindow", "Du dürftest das eigentlich jetzt nicht lesen!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.berechnungen), _translate("MainWindow", "Berechnungen"))
        self.menuInfo.setTitle(_translate("MainWindow", "Datei"))
        self.actionSave.setText(_translate("MainWindow", "Speichern"))
        self.actionInfo.setText(_translate("MainWindow", "Über"))
import resources_rc
