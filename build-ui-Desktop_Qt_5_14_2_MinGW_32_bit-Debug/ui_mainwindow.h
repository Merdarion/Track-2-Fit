/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSave;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QTabWidget *tabWidget;
    QWidget *home;
    QVBoxLayout *verticalLayout_2;
    QLabel *willkommen;
    QLabel *willkommenPic;
    QLabel *labeleins;
    QLabel *nichtMehrAktuell;
    QWidget *eintrag;
    QWidget *gridLayoutWidget;
    QGridLayout *verschWerte;
    QFormLayout *ernaehrung;
    QLabel *label3;
    QLabel *label4;
    QLabel *soos;
    QLabel *label2;
    QPushButton *eintragErnaehrung;
    QLabel *label1;
    QLabel *gesamtkcal;
    QLabel *kohlenhydrate;
    QLabel *protein;
    QLabel *fett;
    QLabel *ernaehrungLetzt;
    QLabel *label_9;
    QFormLayout *formGewicht;
    QLabel *ueberschrift;
    QLabel *gewichtlabel;
    QLabel *gewicht;
    QLabel *dateGewichtLabel;
    QPushButton *eintragGewicht;
    QLabel *gewichtLetzt;
    QFormLayout *formUmfaenge;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QPushButton *eintragUmfaenge;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *oberschenkel;
    QLabel *bauch;
    QLabel *huefte;
    QLabel *brust;
    QLabel *bizeps;
    QLabel *umfaengeLetzt;
    QFormLayout *formLayout;
    QLabel *label_11;
    QLabel *kfa;
    QLabel *label_13;
    QLabel *kfaLetzt;
    QPushButton *eintragKfa;
    QLabel *label_10;
    QVBoxLayout *formTrainingsplan;
    QLabel *label_6;
    QTextEdit *trainingsplan;
    QPushButton *eintragPlan;
    QLabel *eintragPlanHinweis;
    QWidget *graph;
    QWidget *sonstigeBerechnungen;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(794, 488);
        MainWindow->setLocale(QLocale(QLocale::German, QLocale::Germany));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        centralwidget->setLocale(QLocale(QLocale::German, QLocale::Germany));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        home = new QWidget();
        home->setObjectName(QString::fromUtf8("home"));
        verticalLayout_2 = new QVBoxLayout(home);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        willkommen = new QLabel(home);
        willkommen->setObjectName(QString::fromUtf8("willkommen"));
        willkommen->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(willkommen);

        willkommenPic = new QLabel(home);
        willkommenPic->setObjectName(QString::fromUtf8("willkommenPic"));
        willkommenPic->setBaseSize(QSize(0, 0));
        willkommenPic->setAutoFillBackground(false);
        willkommenPic->setPixmap(QPixmap(QString::fromUtf8("willkommen_pic.png")));
        willkommenPic->setScaledContents(true);
        willkommenPic->setWordWrap(false);
        willkommenPic->setMargin(0);
        willkommenPic->setIndent(-1);

        verticalLayout_2->addWidget(willkommenPic);

        labeleins = new QLabel(home);
        labeleins->setObjectName(QString::fromUtf8("labeleins"));
        labeleins->setAlignment(Qt::AlignHCenter|Qt::AlignTop);

        verticalLayout_2->addWidget(labeleins);

        nichtMehrAktuell = new QLabel(home);
        nichtMehrAktuell->setObjectName(QString::fromUtf8("nichtMehrAktuell"));
        nichtMehrAktuell->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(nichtMehrAktuell);

        tabWidget->addTab(home, QString());
        eintrag = new QWidget();
        eintrag->setObjectName(QString::fromUtf8("eintrag"));
        gridLayoutWidget = new QWidget(eintrag);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(-1, -1, 772, 416));
        verschWerte = new QGridLayout(gridLayoutWidget);
        verschWerte->setObjectName(QString::fromUtf8("verschWerte"));
        verschWerte->setContentsMargins(0, 0, 0, 0);
        ernaehrung = new QFormLayout();
        ernaehrung->setObjectName(QString::fromUtf8("ernaehrung"));
        ernaehrung->setFormAlignment(Qt::AlignCenter);
        ernaehrung->setContentsMargins(10, 10, 10, 10);
        label3 = new QLabel(gridLayoutWidget);
        label3->setObjectName(QString::fromUtf8("label3"));

        ernaehrung->setWidget(1, QFormLayout::LabelRole, label3);

        label4 = new QLabel(gridLayoutWidget);
        label4->setObjectName(QString::fromUtf8("label4"));

        ernaehrung->setWidget(2, QFormLayout::LabelRole, label4);

        soos = new QLabel(gridLayoutWidget);
        soos->setObjectName(QString::fromUtf8("soos"));

        ernaehrung->setWidget(3, QFormLayout::LabelRole, soos);

        label2 = new QLabel(gridLayoutWidget);
        label2->setObjectName(QString::fromUtf8("label2"));

        ernaehrung->setWidget(4, QFormLayout::LabelRole, label2);

        eintragErnaehrung = new QPushButton(gridLayoutWidget);
        eintragErnaehrung->setObjectName(QString::fromUtf8("eintragErnaehrung"));

        ernaehrung->setWidget(6, QFormLayout::SpanningRole, eintragErnaehrung);

        label1 = new QLabel(gridLayoutWidget);
        label1->setObjectName(QString::fromUtf8("label1"));

        ernaehrung->setWidget(5, QFormLayout::LabelRole, label1);

        gesamtkcal = new QLabel(gridLayoutWidget);
        gesamtkcal->setObjectName(QString::fromUtf8("gesamtkcal"));

        ernaehrung->setWidget(1, QFormLayout::FieldRole, gesamtkcal);

        kohlenhydrate = new QLabel(gridLayoutWidget);
        kohlenhydrate->setObjectName(QString::fromUtf8("kohlenhydrate"));

        ernaehrung->setWidget(2, QFormLayout::FieldRole, kohlenhydrate);

        protein = new QLabel(gridLayoutWidget);
        protein->setObjectName(QString::fromUtf8("protein"));

        ernaehrung->setWidget(3, QFormLayout::FieldRole, protein);

        fett = new QLabel(gridLayoutWidget);
        fett->setObjectName(QString::fromUtf8("fett"));

        ernaehrung->setWidget(4, QFormLayout::FieldRole, fett);

        ernaehrungLetzt = new QLabel(gridLayoutWidget);
        ernaehrungLetzt->setObjectName(QString::fromUtf8("ernaehrungLetzt"));

        ernaehrung->setWidget(5, QFormLayout::FieldRole, ernaehrungLetzt);

        label_9 = new QLabel(gridLayoutWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setTextFormat(Qt::RichText);

        ernaehrung->setWidget(0, QFormLayout::SpanningRole, label_9);


        verschWerte->addLayout(ernaehrung, 2, 2, 1, 1);

        formGewicht = new QFormLayout();
        formGewicht->setObjectName(QString::fromUtf8("formGewicht"));
        formGewicht->setFormAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        formGewicht->setContentsMargins(10, 10, 10, 10);
        ueberschrift = new QLabel(gridLayoutWidget);
        ueberschrift->setObjectName(QString::fromUtf8("ueberschrift"));
        ueberschrift->setTextFormat(Qt::RichText);

        formGewicht->setWidget(0, QFormLayout::SpanningRole, ueberschrift);

        gewichtlabel = new QLabel(gridLayoutWidget);
        gewichtlabel->setObjectName(QString::fromUtf8("gewichtlabel"));

        formGewicht->setWidget(1, QFormLayout::LabelRole, gewichtlabel);

        gewicht = new QLabel(gridLayoutWidget);
        gewicht->setObjectName(QString::fromUtf8("gewicht"));

        formGewicht->setWidget(1, QFormLayout::FieldRole, gewicht);

        dateGewichtLabel = new QLabel(gridLayoutWidget);
        dateGewichtLabel->setObjectName(QString::fromUtf8("dateGewichtLabel"));

        formGewicht->setWidget(2, QFormLayout::LabelRole, dateGewichtLabel);

        eintragGewicht = new QPushButton(gridLayoutWidget);
        eintragGewicht->setObjectName(QString::fromUtf8("eintragGewicht"));

        formGewicht->setWidget(3, QFormLayout::SpanningRole, eintragGewicht);

        gewichtLetzt = new QLabel(gridLayoutWidget);
        gewichtLetzt->setObjectName(QString::fromUtf8("gewichtLetzt"));

        formGewicht->setWidget(2, QFormLayout::FieldRole, gewichtLetzt);


        verschWerte->addLayout(formGewicht, 0, 0, 2, 1);

        formUmfaenge = new QFormLayout();
        formUmfaenge->setObjectName(QString::fromUtf8("formUmfaenge"));
        formUmfaenge->setFormAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        formUmfaenge->setContentsMargins(10, 10, 10, 10);
        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        formUmfaenge->setWidget(1, QFormLayout::LabelRole, label);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formUmfaenge->setWidget(2, QFormLayout::LabelRole, label_2);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formUmfaenge->setWidget(3, QFormLayout::LabelRole, label_3);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        formUmfaenge->setWidget(4, QFormLayout::LabelRole, label_4);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        formUmfaenge->setWidget(5, QFormLayout::LabelRole, label_5);

        eintragUmfaenge = new QPushButton(gridLayoutWidget);
        eintragUmfaenge->setObjectName(QString::fromUtf8("eintragUmfaenge"));

        formUmfaenge->setWidget(7, QFormLayout::SpanningRole, eintragUmfaenge);

        label_7 = new QLabel(gridLayoutWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        formUmfaenge->setWidget(6, QFormLayout::LabelRole, label_7);

        label_8 = new QLabel(gridLayoutWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setTextFormat(Qt::RichText);

        formUmfaenge->setWidget(0, QFormLayout::SpanningRole, label_8);

        oberschenkel = new QLabel(gridLayoutWidget);
        oberschenkel->setObjectName(QString::fromUtf8("oberschenkel"));

        formUmfaenge->setWidget(1, QFormLayout::FieldRole, oberschenkel);

        bauch = new QLabel(gridLayoutWidget);
        bauch->setObjectName(QString::fromUtf8("bauch"));

        formUmfaenge->setWidget(2, QFormLayout::FieldRole, bauch);

        huefte = new QLabel(gridLayoutWidget);
        huefte->setObjectName(QString::fromUtf8("huefte"));

        formUmfaenge->setWidget(3, QFormLayout::FieldRole, huefte);

        brust = new QLabel(gridLayoutWidget);
        brust->setObjectName(QString::fromUtf8("brust"));

        formUmfaenge->setWidget(4, QFormLayout::FieldRole, brust);

        bizeps = new QLabel(gridLayoutWidget);
        bizeps->setObjectName(QString::fromUtf8("bizeps"));

        formUmfaenge->setWidget(5, QFormLayout::FieldRole, bizeps);

        umfaengeLetzt = new QLabel(gridLayoutWidget);
        umfaengeLetzt->setObjectName(QString::fromUtf8("umfaengeLetzt"));

        formUmfaenge->setWidget(6, QFormLayout::FieldRole, umfaengeLetzt);


        verschWerte->addLayout(formUmfaenge, 0, 2, 2, 1);

        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setFormAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        formLayout->setContentsMargins(10, 10, 10, 10);
        label_11 = new QLabel(gridLayoutWidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_11);

        kfa = new QLabel(gridLayoutWidget);
        kfa->setObjectName(QString::fromUtf8("kfa"));

        formLayout->setWidget(1, QFormLayout::FieldRole, kfa);

        label_13 = new QLabel(gridLayoutWidget);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_13);

        kfaLetzt = new QLabel(gridLayoutWidget);
        kfaLetzt->setObjectName(QString::fromUtf8("kfaLetzt"));

        formLayout->setWidget(2, QFormLayout::FieldRole, kfaLetzt);

        eintragKfa = new QPushButton(gridLayoutWidget);
        eintragKfa->setObjectName(QString::fromUtf8("eintragKfa"));

        formLayout->setWidget(3, QFormLayout::SpanningRole, eintragKfa);

        label_10 = new QLabel(gridLayoutWidget);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        formLayout->setWidget(0, QFormLayout::SpanningRole, label_10);


        verschWerte->addLayout(formLayout, 2, 0, 1, 1);

        formTrainingsplan = new QVBoxLayout();
        formTrainingsplan->setObjectName(QString::fromUtf8("formTrainingsplan"));
        formTrainingsplan->setContentsMargins(10, 10, 10, 10);
        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setTextFormat(Qt::RichText);
        label_6->setAlignment(Qt::AlignCenter);

        formTrainingsplan->addWidget(label_6);

        trainingsplan = new QTextEdit(gridLayoutWidget);
        trainingsplan->setObjectName(QString::fromUtf8("trainingsplan"));

        formTrainingsplan->addWidget(trainingsplan);

        eintragPlan = new QPushButton(gridLayoutWidget);
        eintragPlan->setObjectName(QString::fromUtf8("eintragPlan"));

        formTrainingsplan->addWidget(eintragPlan);

        eintragPlanHinweis = new QLabel(gridLayoutWidget);
        eintragPlanHinweis->setObjectName(QString::fromUtf8("eintragPlanHinweis"));
        eintragPlanHinweis->setAlignment(Qt::AlignCenter);

        formTrainingsplan->addWidget(eintragPlanHinweis);


        verschWerte->addLayout(formTrainingsplan, 0, 1, 3, 1);

        tabWidget->addTab(eintrag, QString());
        graph = new QWidget();
        graph->setObjectName(QString::fromUtf8("graph"));
        tabWidget->addTab(graph, QString());
        sonstigeBerechnungen = new QWidget();
        sonstigeBerechnungen->setObjectName(QString::fromUtf8("sonstigeBerechnungen"));
        tabWidget->addTab(sonstigeBerechnungen, QString());

        verticalLayout->addWidget(tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSave->setText(QCoreApplication::translate("MainWindow", "Speichern", nullptr));
#if QT_CONFIG(tooltip)
        tabWidget->setToolTip(QCoreApplication::translate("MainWindow", "<html><head/><body><p>dsafs</p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        willkommen->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Fitnesstracker</span></p></body></html>", nullptr));
        willkommenPic->setText(QString());
        labeleins->setText(QCoreApplication::translate("MainWindow", "<strong>Folgende Eintr\303\244ge sollten aktualisiert werden:</strong>", nullptr));
        nichtMehrAktuell->setText(QString());
        tabWidget->setTabText(tabWidget->indexOf(home), QCoreApplication::translate("MainWindow", "Home", nullptr));
        label3->setText(QCoreApplication::translate("MainWindow", "Gesamtkalorien:", nullptr));
        label4->setText(QCoreApplication::translate("MainWindow", "Kohlenhydrate:", nullptr));
        soos->setText(QCoreApplication::translate("MainWindow", "Proteine:", nullptr));
        label2->setText(QCoreApplication::translate("MainWindow", "Fett:", nullptr));
        eintragErnaehrung->setText(QCoreApplication::translate("MainWindow", "Eintragen", nullptr));
        label1->setText(QCoreApplication::translate("MainWindow", "Letzte \303\204nderung", nullptr));
        gesamtkcal->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        kohlenhydrate->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        protein->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        fett->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        ernaehrungLetzt->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ern\303\244hrung (in g):</span></p></body></html>", nullptr));
        ueberschrift->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">W\303\266chentliches<br/>Gewicht (in kg):</span></p></body></html>", nullptr));
        gewichtlabel->setText(QCoreApplication::translate("MainWindow", "Gewicht", nullptr));
        gewicht->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        dateGewichtLabel->setText(QCoreApplication::translate("MainWindow", "Letzter Eintrag:", nullptr));
        eintragGewicht->setText(QCoreApplication::translate("MainWindow", "Eintragen", nullptr));
        gewichtLetzt->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Oberschenkel:", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Bauch:", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "H\303\274fte:", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Brust:", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Bizeps:", nullptr));
        eintragUmfaenge->setText(QCoreApplication::translate("MainWindow", "Eintragen", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Letzter Eintrag:", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Umf\303\244nge (in cm): </span></p></body></html>", nullptr));
        oberschenkel->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        bauch->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        huefte->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        brust->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        bizeps->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        umfaengeLetzt->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "Kfa:", nullptr));
        kfa->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "Letzter Eintrag: ", nullptr));
        kfaLetzt->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        eintragKfa->setText(QCoreApplication::translate("MainWindow", "Eintragen", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">K\303\266rperfettanteil (in %)</span></p></body></html>", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Aktueller Trainingsplan</span></p></body></html>", nullptr));
        trainingsplan->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">siehe &quot;trainingsplan.txt&quot;-Datei</p></body></html>", nullptr));
        eintragPlan->setText(QCoreApplication::translate("MainWindow", "Eintragen", nullptr));
        eintragPlanHinweis->setText(QCoreApplication::translate("MainWindow", "<strong>Trainingsplan ge\303\244ndert</strong>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(eintrag), QCoreApplication::translate("MainWindow", "Werte eintragen", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(graph), QCoreApplication::translate("MainWindow", "Graphen", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(sonstigeBerechnungen), QCoreApplication::translate("MainWindow", "Berechnungen", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
