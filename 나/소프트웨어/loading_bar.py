import tkinter as tk
import subprocess  # subprocess 임포트 추가

class LoadingBar:
    def __init__(self, parent, x, y, width, height, max_progress=300):
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_progress = max_progress
        self.progress = 0
        self.bar_width = 0
        self.is_active = False
        
        self.canvas = tk.Canvas(self.parent, width=self.width, height=self.height, bg='white', highlightthickness=0)
        self.canvas.place(x=self.x, y=self.y)

    def start_loading(self):
        if not self.is_active:
            self.draw_loading_bar()
            self.update_loading()
            self.is_active = True
    
    def draw_loading_bar(self):
        self.canvas.create_rectangle(0, 0, self.bar_width, self.height, fill='lightblue', outline='white', tags='progress')
    
    def update_loading(self):
        if self.progress < self.max_progress:
            self.progress += 1
            self.bar_width = self.width * (self.progress / self.max_progress)
            self.canvas.coords('progress', 0, 0, self.bar_width, self.height)
            
            # 네트워크 상태 확인 (예제에서는 ping 명령어 사용)
            try:
                subprocess.run(["ping", "www.google.com"], check=True, capture_output=True, timeout=0.1)
                self.canvas.itemconfig('progress', fill='lightblue')  # 연결 상태에 따라 색상 변경
            except subprocess.CalledProcessError:
                self.canvas.itemconfig('progress', fill='red')  # 연결 끊김
            except subprocess.TimeoutExpired:
                self.canvas.itemconfig('progress', fill='yellow')  # 타임아웃
            
            self.canvas.after(10, self.update_loading)  # 10ms마다 업데이트
    
    def stop_loading(self):
        if self.is_active:
            self.canvas.place_forget()
            self.is_active = False
