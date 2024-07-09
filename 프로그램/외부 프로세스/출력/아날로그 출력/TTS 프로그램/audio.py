from pydub import AudioSegment
import numpy as np
from scipy.signal import butter, lfilter
import scipy.io.wavfile as wavfile
import os

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def process_audio(input_file, output_file, lowcut=100, highcut=4000):
    # 오디오 파일 로드
    audio = AudioSegment.from_file(input_file)
    # 샘플링 레이트 가져오기
    fs = audio.frame_rate
    # 오디오 데이터를 numpy 배열로 변환
    samples = np.array(audio.get_array_of_samples())
    # 오디오가 stereo인 경우 하나의 채널만 선택
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
        samples = samples[:, 0]
    # 주파수 필터 적용
    filtered_samples = bandpass_filter(samples, lowcut, highcut, fs)
    # 오디오 데이터 재생성
    filtered_audio = AudioSegment(
        filtered_samples.tobytes(), 
        frame_rate=fs,
        sample_width=audio.sample_width, 
        channels=1
    )
    # 결과 저장
    filtered_audio.export(output_file, format="mp3")
    print(f"Filtered audio saved as: {output_file}")

static_folder = 'C:\\Users\\ssmma\\Documents\\신성민\\데이터\\TTS용 데이터\\유튜브 다운로더\\videos\\'

file_name = "태번 마스터 제작진의 또다른 후속작 - 대장장이 마스터"
# 입력 파일 이름
input_file = static_folder + file_name + "\\" + file_name

# 예제로 사용할 파일 경로 설정
output_audio_file = input_file + ".mp3"
# 입력 및 출력 파일 경로 설정

input_file = output_audio_file
output_file = input_file + "audio.mp3"

# 함수 호출
process_audio(input_file, output_file)
