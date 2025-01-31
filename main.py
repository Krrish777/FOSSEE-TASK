import sys
from PyQt5.QtWidgets import QApplication
from gui import BridgeCostApp
from database import create_database

if __name__ == "__main__":
    create_database() # Setting up the database
    
    # Entry point of the application
    app = QApplication(sys.argv)
    window = BridgeCostApp()
    window.show()
    sys.exit(app.exec_())