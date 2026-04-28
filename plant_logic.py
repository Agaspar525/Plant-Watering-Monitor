import csv
import os
import random
import datetime
from PyQt6.QtWidgets import QMainWindow
from gui2 import Ui_MainWindow

WATER_LOG = "water_log.csv"

class plantWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide status labels when started
        self.ui.needs_water_label.hide()
        self.ui.ok_label.hide()

        # Disables water button until sensor is read
        self.ui.water_button.setEnabled(False)

        # Create the CSV file if it does not exist
        if not os.path.exists(WATER_LOG):
            with open(WATER_LOG, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["plant", "moisture", "date"])

        # Connect buttons to functions
        self.ui.sensor_button.clicked.connect(self.read_sensor)
        self.ui.water_button.clicked.connect(self.water_plant)

    def getGeometry(self) -> None:
        screen = self.screen().availableGeometry()
        window = self.frameGeometry()
        window.moveCenter(screen.center())
        self.move(window.topLeft())

    def read_sensor(self) -> None:
        moisture: int = random.randint(0, 100)

        self.ui.moisture_display.display(moisture)

        # Reset labels
        self.ui.needs_water_label.hide()
        self.ui.ok_label.hide()
        self.ui.water_button.setEnabled(False)

        if moisture < 30:
            self.ui.needs_water_label.show()
            self.ui.water_button.setEnabled(True)
        else:
            self.ui.ok_label.show()

    def water_plant(self) -> None:
        # Log the watering with plant name, moisture level, and date to the CSV file
        plant: str = self.ui.plant_select.currentText()
        moisture: int = self.ui.moisture_display.value()
        date: str = datetime.date.today().strftime("%Y-%m-%d")

        with open(WATER_LOG, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([plant, moisture, date])

        # Reset the display after watering
        self.ui.needs_water_label.hide()
        self.ui.water_button.setEnabled(False)
        self.ui.ok_label.show()
        self.ui.ok_label.setText("Plant has been watered!")