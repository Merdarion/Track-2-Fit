/********************************************************************************
** Form generated from reading UI file 'entryform.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ENTRYFORM_H
#define UI_ENTRYFORM_H

#include <QtCore/QDate>
#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QToolBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_EntryForm
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QToolBox *toolBox;
    QWidget *Gewicht;
    QFormLayout *formLayout;
    QDoubleSpinBox *gewicht;
    QLabel *label_2;
    QLabel *label_3;
    QDateEdit *datumGewicht;
    QWidget *Umfaenge;
    QWidget *widget;
    QGridLayout *gridLayout_2;
    QFrame *frame;
    QFormLayout *formLayout_3;
    QLabel *label_4;
    QDoubleSpinBox *oberschenkel;
    QLabel *label_5;
    QDoubleSpinBox *bauch;
    QLabel *label_6;
    QDoubleSpinBox *huefte;
    QFrame *frame_2;
    QFormLayout *formLayout_4;
    QLabel *label_7;
    QDoubleSpinBox *brust;
    QLabel *label_13;
    QDoubleSpinBox *bizeps;
    QLabel *label_16;
    QDateEdit *datumUmfaenge;
    QWidget *Ernaehrung;
    QFrame *frame_3;
    QFormLayout *formLayout_2;
    QLabel *label_10;
    QSpinBox *protein;
    QLabel *label_11;
    QSpinBox *fett;
    QFrame *frame_4;
    QFormLayout *formLayout_5;
    QLabel *label_8;
    QLabel *label_15;
    QSpinBox *gesamtKcal;
    QLabel *label_9;
    QSpinBox *kohlenhydrate;
    QDateEdit *datumErnaehrung;
    QWidget *Koerperfettanteil;
    QFrame *frame_5;
    QFormLayout *formLayout_6;
    QLabel *label_12;
    QDoubleSpinBox *kfa;
    QLabel *label_14;
    QDateEdit *datumKFA;
    QLabel *lustigLol;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *EntryForm)
    {
        if (EntryForm->objectName().isEmpty())
            EntryForm->setObjectName(QString::fromUtf8("EntryForm"));
        EntryForm->resize(600, 278);
        EntryForm->setLocale(QLocale(QLocale::German, QLocale::Germany));
        verticalLayout = new QVBoxLayout(EntryForm);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(EntryForm);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout->addWidget(label);

        toolBox = new QToolBox(EntryForm);
        toolBox->setObjectName(QString::fromUtf8("toolBox"));
        toolBox->setLocale(QLocale(QLocale::German, QLocale::Germany));
        Gewicht = new QWidget();
        Gewicht->setObjectName(QString::fromUtf8("Gewicht"));
        Gewicht->setGeometry(QRect(0, 0, 582, 69));
        formLayout = new QFormLayout(Gewicht);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        gewicht = new QDoubleSpinBox(Gewicht);
        gewicht->setObjectName(QString::fromUtf8("gewicht"));
        gewicht->setDecimals(1);
        gewicht->setSingleStep(0.100000000000000);

        formLayout->setWidget(0, QFormLayout::FieldRole, gewicht);

        label_2 = new QLabel(Gewicht);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label_2);

        label_3 = new QLabel(Gewicht);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_3);

        datumGewicht = new QDateEdit(Gewicht);
        datumGewicht->setObjectName(QString::fromUtf8("datumGewicht"));
        datumGewicht->setDate(QDate(2000, 1, 4));

        formLayout->setWidget(1, QFormLayout::FieldRole, datumGewicht);

        toolBox->addItem(Gewicht, QString::fromUtf8("Gewicht"));
        Umfaenge = new QWidget();
        Umfaenge->setObjectName(QString::fromUtf8("Umfaenge"));
        Umfaenge->setGeometry(QRect(0, 0, 582, 69));
        widget = new QWidget(Umfaenge);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(10, 0, 511, 111));
        gridLayout_2 = new QGridLayout(widget);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        frame = new QFrame(widget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        formLayout_3 = new QFormLayout(frame);
        formLayout_3->setObjectName(QString::fromUtf8("formLayout_3"));
        label_4 = new QLabel(frame);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        formLayout_3->setWidget(0, QFormLayout::LabelRole, label_4);

        oberschenkel = new QDoubleSpinBox(frame);
        oberschenkel->setObjectName(QString::fromUtf8("oberschenkel"));
        oberschenkel->setDecimals(1);
        oberschenkel->setSingleStep(0.100000000000000);

        formLayout_3->setWidget(0, QFormLayout::FieldRole, oberschenkel);

        label_5 = new QLabel(frame);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        formLayout_3->setWidget(1, QFormLayout::LabelRole, label_5);

        bauch = new QDoubleSpinBox(frame);
        bauch->setObjectName(QString::fromUtf8("bauch"));
        bauch->setDecimals(1);
        bauch->setSingleStep(0.100000000000000);

        formLayout_3->setWidget(1, QFormLayout::FieldRole, bauch);

        label_6 = new QLabel(frame);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        formLayout_3->setWidget(2, QFormLayout::LabelRole, label_6);

        huefte = new QDoubleSpinBox(frame);
        huefte->setObjectName(QString::fromUtf8("huefte"));
        huefte->setDecimals(1);

        formLayout_3->setWidget(2, QFormLayout::FieldRole, huefte);


        gridLayout_2->addWidget(frame, 0, 0, 1, 1);

        frame_2 = new QFrame(widget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        formLayout_4 = new QFormLayout(frame_2);
        formLayout_4->setObjectName(QString::fromUtf8("formLayout_4"));
        label_7 = new QLabel(frame_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        formLayout_4->setWidget(1, QFormLayout::LabelRole, label_7);

        brust = new QDoubleSpinBox(frame_2);
        brust->setObjectName(QString::fromUtf8("brust"));
        brust->setDecimals(1);
        brust->setSingleStep(0.100000000000000);

        formLayout_4->setWidget(1, QFormLayout::FieldRole, brust);

        label_13 = new QLabel(frame_2);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        formLayout_4->setWidget(0, QFormLayout::LabelRole, label_13);

        bizeps = new QDoubleSpinBox(frame_2);
        bizeps->setObjectName(QString::fromUtf8("bizeps"));
        bizeps->setDecimals(1);
        bizeps->setSingleStep(0.100000000000000);

        formLayout_4->setWidget(0, QFormLayout::FieldRole, bizeps);

        label_16 = new QLabel(frame_2);
        label_16->setObjectName(QString::fromUtf8("label_16"));

        formLayout_4->setWidget(2, QFormLayout::LabelRole, label_16);

        datumUmfaenge = new QDateEdit(frame_2);
        datumUmfaenge->setObjectName(QString::fromUtf8("datumUmfaenge"));

        formLayout_4->setWidget(2, QFormLayout::FieldRole, datumUmfaenge);


        gridLayout_2->addWidget(frame_2, 0, 1, 1, 1);

        toolBox->addItem(Umfaenge, QString::fromUtf8("Umf\303\244nge"));
        Ernaehrung = new QWidget();
        Ernaehrung->setObjectName(QString::fromUtf8("Ernaehrung"));
        Ernaehrung->setGeometry(QRect(0, 0, 582, 69));
        frame_3 = new QFrame(Ernaehrung);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setGeometry(QRect(300, 0, 271, 66));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        formLayout_2 = new QFormLayout(frame_3);
        formLayout_2->setObjectName(QString::fromUtf8("formLayout_2"));
        label_10 = new QLabel(frame_3);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        formLayout_2->setWidget(0, QFormLayout::LabelRole, label_10);

        protein = new QSpinBox(frame_3);
        protein->setObjectName(QString::fromUtf8("protein"));
        protein->setMaximum(999);

        formLayout_2->setWidget(0, QFormLayout::FieldRole, protein);

        label_11 = new QLabel(frame_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        formLayout_2->setWidget(1, QFormLayout::LabelRole, label_11);

        fett = new QSpinBox(frame_3);
        fett->setObjectName(QString::fromUtf8("fett"));
        fett->setMaximum(999);

        formLayout_2->setWidget(1, QFormLayout::FieldRole, fett);

        frame_4 = new QFrame(Ernaehrung);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setGeometry(QRect(0, 0, 291, 111));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        formLayout_5 = new QFormLayout(frame_4);
        formLayout_5->setObjectName(QString::fromUtf8("formLayout_5"));
        label_8 = new QLabel(frame_4);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        formLayout_5->setWidget(0, QFormLayout::LabelRole, label_8);

        label_15 = new QLabel(frame_4);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        formLayout_5->setWidget(2, QFormLayout::LabelRole, label_15);

        gesamtKcal = new QSpinBox(frame_4);
        gesamtKcal->setObjectName(QString::fromUtf8("gesamtKcal"));
        gesamtKcal->setMaximum(9999);

        formLayout_5->setWidget(0, QFormLayout::FieldRole, gesamtKcal);

        label_9 = new QLabel(frame_4);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        formLayout_5->setWidget(1, QFormLayout::LabelRole, label_9);

        kohlenhydrate = new QSpinBox(frame_4);
        kohlenhydrate->setObjectName(QString::fromUtf8("kohlenhydrate"));
        kohlenhydrate->setMaximum(999);

        formLayout_5->setWidget(1, QFormLayout::FieldRole, kohlenhydrate);

        datumErnaehrung = new QDateEdit(frame_4);
        datumErnaehrung->setObjectName(QString::fromUtf8("datumErnaehrung"));

        formLayout_5->setWidget(2, QFormLayout::FieldRole, datumErnaehrung);

        toolBox->addItem(Ernaehrung, QString::fromUtf8("Ern\303\244hrung"));
        Koerperfettanteil = new QWidget();
        Koerperfettanteil->setObjectName(QString::fromUtf8("Koerperfettanteil"));
        Koerperfettanteil->setGeometry(QRect(0, 0, 582, 69));
        frame_5 = new QFrame(Koerperfettanteil);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setGeometry(QRect(0, 0, 581, 81));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        formLayout_6 = new QFormLayout(frame_5);
        formLayout_6->setObjectName(QString::fromUtf8("formLayout_6"));
        label_12 = new QLabel(frame_5);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        formLayout_6->setWidget(0, QFormLayout::LabelRole, label_12);

        kfa = new QDoubleSpinBox(frame_5);
        kfa->setObjectName(QString::fromUtf8("kfa"));
        kfa->setDecimals(1);
        kfa->setSingleStep(0.100000000000000);

        formLayout_6->setWidget(0, QFormLayout::FieldRole, kfa);

        label_14 = new QLabel(frame_5);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        formLayout_6->setWidget(1, QFormLayout::LabelRole, label_14);

        datumKFA = new QDateEdit(frame_5);
        datumKFA->setObjectName(QString::fromUtf8("datumKFA"));

        formLayout_6->setWidget(1, QFormLayout::FieldRole, datumKFA);

        toolBox->addItem(Koerperfettanteil, QString::fromUtf8("K\303\266rperfettanteil"));

        verticalLayout->addWidget(toolBox);

        lustigLol = new QLabel(EntryForm);
        lustigLol->setObjectName(QString::fromUtf8("lustigLol"));
        lustigLol->setTextFormat(Qt::RichText);

        verticalLayout->addWidget(lustigLol);

        buttonBox = new QDialogButtonBox(EntryForm);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(EntryForm);
        QObject::connect(buttonBox, SIGNAL(rejected()), EntryForm, SLOT(reject()));

        toolBox->setCurrentIndex(2);
        toolBox->layout()->setSpacing(6);


        QMetaObject::connectSlotsByName(EntryForm);
    } // setupUi

    void retranslateUi(QDialog *EntryForm)
    {
        EntryForm->setWindowTitle(QCoreApplication::translate("EntryForm", "Gewicht eintragen", nullptr));
        label->setText(QCoreApplication::translate("EntryForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Neuer Eintrag:</span></p></body></html>", nullptr));
        label_2->setText(QCoreApplication::translate("EntryForm", "Gewicht:", nullptr));
        label_3->setText(QCoreApplication::translate("EntryForm", "Datum: ", nullptr));
        datumGewicht->setDisplayFormat(QCoreApplication::translate("EntryForm", "dd.MM.yyyy", nullptr));
        toolBox->setItemText(toolBox->indexOf(Gewicht), QCoreApplication::translate("EntryForm", "Gewicht", nullptr));
        label_4->setText(QCoreApplication::translate("EntryForm", "Oberschenkel:", nullptr));
        label_5->setText(QCoreApplication::translate("EntryForm", "Bauch:", nullptr));
        label_6->setText(QCoreApplication::translate("EntryForm", "H\303\274fte:", nullptr));
        label_7->setText(QCoreApplication::translate("EntryForm", "Brust:", nullptr));
        label_13->setText(QCoreApplication::translate("EntryForm", "Bizeps:", nullptr));
        label_16->setText(QCoreApplication::translate("EntryForm", "Datum:", nullptr));
        datumUmfaenge->setDisplayFormat(QCoreApplication::translate("EntryForm", "dd.MM.yyyy", nullptr));
        toolBox->setItemText(toolBox->indexOf(Umfaenge), QCoreApplication::translate("EntryForm", "Umf\303\244nge", nullptr));
        label_10->setText(QCoreApplication::translate("EntryForm", "Protein:", nullptr));
        label_11->setText(QCoreApplication::translate("EntryForm", "Fett:", nullptr));
        label_8->setText(QCoreApplication::translate("EntryForm", "Gesamtkcal:", nullptr));
        label_15->setText(QCoreApplication::translate("EntryForm", "Datum:", nullptr));
        label_9->setText(QCoreApplication::translate("EntryForm", "Kohlenhydrate:", nullptr));
        datumErnaehrung->setDisplayFormat(QCoreApplication::translate("EntryForm", "dd.MM.yyyy", nullptr));
        toolBox->setItemText(toolBox->indexOf(Ernaehrung), QCoreApplication::translate("EntryForm", "Ern\303\244hrung", nullptr));
        label_12->setText(QCoreApplication::translate("EntryForm", "KFA:", nullptr));
        label_14->setText(QCoreApplication::translate("EntryForm", "Datum:", nullptr));
        datumKFA->setDisplayFormat(QCoreApplication::translate("EntryForm", "dd.MM.yyyy", nullptr));
        toolBox->setItemText(toolBox->indexOf(Koerperfettanteil), QCoreApplication::translate("EntryForm", "K\303\266rperfettanteil", nullptr));
        lustigLol->setText(QCoreApplication::translate("EntryForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Escht wird \303\244bs eigetrooche!</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class EntryForm: public Ui_EntryForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ENTRYFORM_H
