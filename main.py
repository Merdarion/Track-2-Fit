import csv

from berechnungen import Calculations
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.entryform import Ui_EntryForm
from PyQt5.QtCore import QDate


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Track to Fit")

        self.signals_connection()
        self.entryDialog = EntryForm()
        self.calc = Calculations()
        self.show_plots()

        self.read_entries()
        self.set_hints()

        self.ui.eintragPlanHinweis.hide()
        self.ui.calcKfaLabel.hide()

        self.ui.gewichtGraph.show()

    def signals_connection(self):
        # Einträge
        self.ui.eintragGewicht.clicked.connect(self.on_entryButton_clicked)
        self.ui.eintragErnaehrung.clicked.connect(self.on_entryButton_clicked)
        self.ui.eintragUmfaenge.clicked.connect(self.on_entryButton_clicked)
        self.ui.eintragKfa.clicked.connect(self.on_entryButton_clicked)
        self.ui.eintragPlan.clicked.connect(self.on_eintragPlan_clicked)

        # Plots
        self.ui.gewichtCheck.clicked.connect(self.checkBox_checked)

        # Über
        self.ui.actionInfo.triggered.connect(self.print_nen_scheiss)

        # KFA Rechner
        self.ui.calcKfaButton.clicked.connect(self.on_calcKfaButton_clicked)

    def print_nen_scheiss(self):
        print("Created by Jens Rüppel")

    def show_plots(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        dates = []
        vals = []

        with open("../daten/gewicht.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)

            for row in data:
                if row[0] == "Datum":
                    continue
                dates_new = row[0][8:10] + "." + row[0][5:7]
                dates.append(dates_new)
                vals.append(float(row[1]))

        ax = self.figure.add_subplot(111)
        ax.plot(dates, vals)
        self.canvas.draw()

    def on_entryButton_clicked(self):
        sender_button = self.sender()

        if sender_button.objectName() == "eintragGewicht":
            self.entryDialog.set_current_index(0)
        elif sender_button.objectName() == "eintragUmfaenge":
            self.entryDialog.set_current_index(1)
        elif sender_button.objectName() == "eintragErnaehrung":
            self.entryDialog.set_current_index(2)
        elif sender_button.objectName() == "eintragKfa":
            self.entryDialog.set_current_index(3)

        self.entryDialog.show()

    def checkBox_checked(self):
        self.plots.plot_gewicht()


    def on_eintragPlan_clicked(self):
        with open("../daten/trainingsplan.txt", "w", encoding="utf-8") as file:
            file.write(self.ui.trainingsplan.toPlainText())
            self.ui.eintragPlanHinweis.show()

    def read_entries(self):
        # Gewicht
        with open("../daten/gewicht.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            row_count = len(data)

            gewicht = data[row_count - 1][1]

            datum = data[row_count - 1][0].split("-")
            gewicht_letzt = ".".join(datum[::-1])

        # Umfänge
        with open("../daten/umfaenge.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            row_count = len(data)

            oberschenkel = data[row_count - 1][1]
            brust = data[row_count - 1][2]
            bizeps = data[row_count - 1][3]
            bauch = data[row_count - 1][4]
            huefte = data[row_count - 1][5]

            datum = data[row_count - 1][0].split("-")
            umfaenge_letzt = ".".join(datum[::-1])

        # Ernährung:
        with open("../daten/ernaehrung.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            row_count = len(data)

            gesamt_kcal = data[row_count - 1][1]
            kohlenhydrate = data[row_count - 1][2]
            protein = data[row_count - 1][3]
            fett = data[row_count - 1][4]

            datum = data[row_count - 1][0].split("-")
            ernaehrung_letzt = ".".join(datum[::-1])

        # KFA:
        with open("../daten/kfa.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            row_count = len(data)

            kfa = data[row_count - 1][1]

            datum = data[row_count - 1][0].split("-")
            kfa_letzt = ".".join(datum[::-1])

        # Trainingsplan:
        with open("../daten/trainingsplan.txt", "r", encoding="utf-8") as file:
            self.ui.trainingsplan.setText(file.read())


        ####################Set Entries:###################
        # Gewicht
        self.ui.gewicht.setText(gewicht)
        self.ui.gewichtLetzt.setText(gewicht_letzt)

        # Umfänge
        self.ui.oberschenkel.setText(oberschenkel)
        self.ui.brust.setText(brust)
        self.ui.bizeps.setText(bizeps)
        self.ui.bauch.setText(bauch)
        self.ui.huefte.setText(huefte)
        self.ui.umfaengeLetzt.setText(umfaenge_letzt)

        # Ernährung
        self.ui.gesamtkcal.setText(gesamt_kcal)
        self.ui.kohlenhydrate.setText(kohlenhydrate)
        self.ui.protein.setText(protein)
        self.ui.fett.setText(fett)
        self.ui.ernaehrungLetzt.setText(ernaehrung_letzt)

        # KFA
        self.ui.kfa.setText(kfa)
        self.ui.kfaLetzt.setText(kfa_letzt)

    def set_hints(self):
        hints = []
        today = QDate.currentDate()
        date_gew = QDate.fromString(self.ui.gewichtLetzt.text(), 'dd.MM.yyyy')
        date_umf = QDate.fromString(self.ui.umfaengeLetzt.text(), 'dd.MM.yyyy')
        date_kfa = QDate.fromString(self.ui.kfaLetzt.text(), 'dd.MM.yyyy')
        diff_date_gew = date_gew.daysTo(today)
        diff_date_umf = date_umf.daysTo(today)
        diff_date_kfa = date_kfa.daysTo(today)
        kfa = float(self.ui.kfa.text())

        if diff_date_gew >= 7:
            hints.append("Gewicht")
        if diff_date_kfa >= 14:
            hints.append("Körperfettanteil")
        if diff_date_umf >= 30:
            hints.append("Umfänge")
        if kfa >= 20:
            hints.append("Ernährung")

        hinweise = ", ".join(hints)
        self.ui.nichtMehrAktuell.setText(hinweise)

    def on_calcKfaButton_clicked(self):
        alter = self.ui.alter.value()
        hf_oberschenkel = self.ui.hfOberschenkel.value()
        hf_brust = self.ui.hfBrust.value()
        hf_bauch = self.ui.hfBauch.value()
        kfa = self.calc.kfa_berechnen(hf_oberschenkel, hf_brust, hf_bauch, alter)

        if float(kfa) < 6:
            self.ui.calcKfaLabel.setText("Da stimmt irgendwas nicht")
        else:
            self.ui.calcKfaLabel.setText(kfa)

        self.ui.calcKfaLabel.show()


class EntryForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_EntryForm()
        self.ui.setupUi(self)

        self.set_todays_date()
        self.ui.lustigLol.hide()

        self.ui.buttonBox.clicked.connect(self.write_entry)

    def set_current_index(self, index):
        self.ui.toolBox.setCurrentIndex(index)

    def set_todays_date(self):
        self.ui.datumGewicht.setDate(QDate.currentDate())
        self.ui.datumUmfaenge.setDate(QDate.currentDate())
        self.ui.datumErnaehrung.setDate(QDate.currentDate())
        self.ui.datumKFA.setDate(QDate.currentDate())

    def write_entry(self):
        umfaenge = [self.ui.oberschenkel.value(),
                    self.ui.huefte.value(),
                    self.ui.bizeps.value(),
                    self.ui.bauch.value(),
                    self.ui.brust.value()]

        ernaehrung = [self.ui.gesamtKcal.value(),
                      self.ui.kohlenhydrate.value(),
                      self.ui.protein.value(),
                      self.ui.fett.value()]

        if self.ui.gewicht.value() != 0.0:
            with open('../daten/gewicht.csv', 'a', newline='') as file:
                write = csv.writer(file, delimiter=",")

                row_content = [
                    self.ui.datumGewicht.date().toPyDate(),
                    self.ui.gewicht.value()
                ]

                write.writerow(row_content)
                self.accept()

        elif 0.0 not in umfaenge:
            with open('../daten/umfaenge.csv', 'a', newline='') as file:
                write = csv.writer(file, delimiter=",")

                row_content = [
                    self.ui.datumGewicht.date().toPyDate(),
                    self.ui.oberschenkel.value(),
                    self.ui.brust.value(),
                    self.ui.bizeps.value(),
                    self.ui.bauch.value(),
                    self.ui.huefte.value()
                ]

                write.writerow(row_content)
                self.accept()

        elif 0 not in ernaehrung:
            with open('../daten/ernaehrung.csv', 'a', newline='') as file:
                write = csv.writer(file, delimiter=",")

                row_content = [
                    self.ui.datumErnaehrung.date().toPyDate(),
                    self.ui.gesamtKcal.value(),
                    self.ui.kohlenhydrate.value(),
                    self.ui.protein.value(),
                    self.ui.fett.value()
                ]

                write.writerow(row_content)
                self.accept()

        elif self.ui.kfa.value() != 0.0:
            with open('../daten/kfa.csv', 'a', newline="") as file:
                write = csv.writer(file, delimiter=",")

                row_content = [
                    self.ui.datumKFA.date().toPyDate(),
                    self.ui.kfa.value()
                ]

                write.writerow(row_content)

                self.accept()
        else:
            self.ui.lustigLol.show()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
