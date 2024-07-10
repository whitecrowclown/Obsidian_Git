import tkinter as tk
from input_entry import InputEntry
from download_button import DownloadButton
from loading_bar import LoadingBar

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("YTDL_FEC")
        self.root.geometry("600x400")
        
        # 입력 박스 생성
        self.input_entry = InputEntry(self.root, 20, 20, 200, 30)
        self.input_entry.create()

        # 다운로드 버튼 생성
        self.download_button = DownloadButton(self.root, 250, 20, 100, 30, text="다운로드", command=self.on_download_click)
        self.download_button.create()

        # Canvas 생성
        self.canvas = tk.Canvas(self.root, width=200, height=30, bg='white', highlightthickness=0)
        self.canvas.place(x=20, y=70)  # Canvas 배치

        # 로딩바 생성
        self.loading_bar = LoadingBar(self.canvas, 0, 0, 200, 30)

    def on_download_click(self):
        link = self.input_entry.entry.get().strip()

        if not self.loading_bar.is_active:
            # 로딩바가 비활성화된 경우
            self.input_entry.hide()  # 입력 박스 숨기기
            self.download_button.disable()  # 다운로드 버튼 비활성화
            self.loading_bar.start_loading()  # 로딩바 시작
        else:
            # 로딩바가 활성화된 경우
            self.loading_bar.stop_loading()  # 로딩바 중지
            self.input_entry.show()  # 입력 박스 보이기
            self.download_button.enable()  # 다운로드 버튼 활성화

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
