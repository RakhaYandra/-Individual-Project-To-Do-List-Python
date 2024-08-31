import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []

        self.layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.add_button = QPushButton("Add Task")
        self.add_button.setEnabled(False) 
        self.task_list = QListWidget()
        self.remove_button = QPushButton("Remove Selected Task")

        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.remove_button)

        self.task_input.textChanged.connect(self.toggle_add_button)
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        self.setLayout(self.layout)

    def toggle_add_button(self):
        self.add_button.setEnabled(bool(self.task_input.text().strip()))

    def add_task(self):
        task = self.task_input.text().strip()
        if task and task not in self.tasks:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()
        elif task in self.tasks:
            QMessageBox.warning(self, "Duplicate Task", "This task already exists!")

    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a task to remove.")
            return
        for item in selected_items:
            self.tasks.remove(item.text())
            self.task_list.takeItem(self.task_list.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
