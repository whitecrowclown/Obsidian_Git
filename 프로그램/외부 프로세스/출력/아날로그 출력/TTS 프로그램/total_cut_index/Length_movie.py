from moviepy.video.io.VideoFileClip import VideoFileClip

def lengthing(file_name):
    static_folder = 'C:\\Users\\ssmma\\Documents\\신성민\\데이터\\TTS용 데이터\\유튜브 다운로더\\videos\\'

    # 입력 파일 이름
    input_file = static_folder + file_name + "\\" + file_name + ".mp4"

    # 비디오 클립 생성
    clip = VideoFileClip(input_file)

    # 비디오의 총 길이 (단위: 초)
    video_duration = clip.duration

    # 클립 닫기 (꼭 해 주어야 함)
    clip.close()
    return video_duration