import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QAction, QToolBar, QLabel, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QStandardPaths

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Browser")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 입력창 및 입력창 레이블 생성
        self.input_label = QLabel("Enter URL or search term:")
        self.url_entry = QLineEdit()
        self.url_entry.setPlaceholderText("Enter URL or search term")
        self.url_entry.returnPressed.connect(self.load_url)  # 엔터키 눌렀을 때 load_url 함수 호출
        self.url_entry.setFixedHeight(self.url_entry.sizeHint().height() * 2)  # 세로 크기를 현재 높이의 2배로 설정
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.url_entry)

        # 웹 뷰 생성
        self.browser_view = QWebEngineView()
        self.layout.addWidget(self.browser_view)

        # 툴바 생성
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # 액션 추가
        self.back_action = QAction("Back", self)
        self.back_action.triggered.connect(self.browser_view.back)
        self.toolbar.addAction(self.back_action)

        self.forward_action = QAction("Forward", self)
        self.forward_action.triggered.connect(self.browser_view.forward)
        self.toolbar.addAction(self.forward_action)

        self.reload_action = QAction("Reload", self)
        self.reload_action.triggered.connect(self.browser_view.reload)
        self.toolbar.addAction(self.reload_action)

        self.browser_view.urlChanged.connect(self.update_url_entry)

        self.show()

    def load_url(self):
        user_input = self.url_entry.text().strip()
        if user_input.lower().startswith('file'):
            # "file"로 시작하면 파일 탐색기를 열어 사용자의 파일 경로를 선택할 수 있도록 함
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
            if file_path:
                url = QUrl.fromLocalFile(file_path)
        elif user_input.lower() == '유튜브':
            url = QUrl('https://www.youtube.com')
        else:
            search_query = '+'.join(user_input.split())
            url = QUrl(f'https://www.google.com/search?q={search_query}')

        self.browser_view.setUrl(url)

    def update_url_entry(self, url):
        self.url_entry.setText(url.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    sys.exit(app.exec_())
