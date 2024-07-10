import subprocess

class NetworkManager:
    def check_network_status(self):
        try:
            subprocess.run(["ping", "www.google.com"], check=True, capture_output=True, timeout=0.1)
            return True  # 연결됨
        except subprocess.CalledProcessError:
            return False  # 연결 끊김
        except subprocess.TimeoutExpired:
            return None  # 타임아웃 발생
