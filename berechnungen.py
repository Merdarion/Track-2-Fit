import csv

from qtpy import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ui.mainwindow import Ui_MainWindow
import matplotlib.pyplot as plt


class Calculations():
    def kfa_berechnen(self, hf_ob, hf_brust, hf_bauch, alter):
        sum = hf_bauch + hf_ob + hf_brust
        formel = 495 / (1.10938 - 0.0008267 * sum + 0.0000016 * sum ** 2 - 0.0002574 * alter) - 450
        kfa = round(formel, 1)
        return str(kfa)


class Plots(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


    def plot_gewicht(self):
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