# web_program.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QAction, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebBrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.input_label = QLabel("Enter URL or search term:")
        self.url_entry = QLineEdit()
        self.url_entry.setPlaceholderText("Enter URL or search term")
        self.url_entry.returnPressed.connect(self.load_url)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.url_entry)

        self.browser_view = QWebEngineView()
        self.layout.addWidget(self.browser_view)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.back_action = QAction("Back", self)
        self.back_action.triggered.connect(self.browser_view.back)
        self.toolbar.addAction(self.back_action)

        self.forward_action = QAction("Forward", self)
        self.forward_action.triggered.connect(self.browser_view.forward)
        self.toolbar.addAction(self.forward_action)

        self.reload_action = QAction("Reload", self)
        self.reload_action.triggered.connect(self.browser_view.reload)
        self.toolbar.addAction(self.reload_action)

        self.show()

    def load_url(self):
        user_input = self.url_entry.text().strip()
        if user_input.lower() == '유튜브':
            url = QUrl('https://www.youtube.com')
        else:
            search_query = '+'.join(user_input.split())
            url = QUrl(f'https://www.google.com/search?q={search_query}')

        self.browser_view.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web_browser = WebBrowserWindow()
    sys.exit(app.exec_())
