import os
import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import subprocess

def toggle_dunst():
    subprocess.run(["dunstctl", "set-paused", "toggle"])

def create_tray_icon(icon_path):
    app = QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon(icon_path), app)  # Adjust the path to your icon
    menu = QMenu()

    # Display the pid of the process
    pid_action = QAction(f"PID: {os.getpid()}", menu)
    pid_action.setEnabled(False)
    menu.addAction(pid_action)

    # Add an option to toggle notifications
    toggle_action = QAction("Toggle Notifications", menu)
    toggle_action.triggered.connect(toggle_dunst)
    menu.addAction(toggle_action)

    # Add an option to quit the application
    quit_action = QAction("Quit", menu)
    quit_action.triggered.connect(app.quit)
    menu.addAction(quit_action)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [1 | 2]")
        print("1: Black bell with white background")
        print("2: White bell with black background")
        sys.exit(1)

    if sys.argv[1] == "1":
        icon_path = "black_bell_white_back.png"
    elif sys.argv[1] == "2":
        icon_path = "white_bell_black_back.png"
    else:
        print(f"Usage: {sys.argv[0]} [1 | 2]")
        print("1: Black bell with white background")
        print("2: White bell with black background")
        sys.exit(1)

    create_tray_icon(icon_path)
