from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_file, output_audio_file):
    # 동영상 파일 열기
    video = VideoFileClip(video_file)
    
    # 오디오만 추출하여 저장
    video.audio.write_audiofile(output_audio_file)

    print(f"오디오 추출 완료: {output_audio_file}")

static_folder = 'C:\\Users\\ssmma\\Documents\\신성민\\데이터\\TTS용 데이터\\유튜브 다운로더\\videos\\'

file_name = "태번 마스터 제작진의 또다른 후속작 - 대장장이 마스터"
# 입력 파일 이름
input_file = static_folder + file_name + "\\" + file_name

# 예제로 사용할 파일 경로 설정
video_file = input_file + ".mp4"
output_audio_file = input_file + ".mp3"

# 함수 호출
extract_audio(video_file, output_audio_file)