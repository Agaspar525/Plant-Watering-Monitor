from PyQt6.QtWidgets import QApplication
from plant_logic import plantWindow

def main():
    """Launch the plant watering tracker."""
    application = QApplication([])
    window = plantWindow()
    window.getGeometry()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()