from moviepy.video.io.VideoFileClip import VideoFileClip

def cutting(movie_name, max_time):
    # 폴더 이름
    static_folder = 'C:\\Users\\ssmma\\Documents\\신성민\\데이터\\TTS용 데이터\\유튜브 다운로더\\videos\\' + movie_name
    
    # 입력 파일 이름
    input_file = static_folder + "\\" + movie_name

    # 출력 파일 이름
    for i in range(int(max_time // 10)):
        output_form = i
        
        # 시작 시간과 끝 시간 (단위: 초)
        start_time = 10 * i
        end_time = min(10 * (i + 1), max_time - 10) 
        
        # 비디오 클립 생성
        clip = VideoFileClip(input_file + ".mp4").subclip(start_time, end_time)
        
        # 영상 저장
        clip.write_videofile(input_file + str(i) + ".mp4", codec="libx264", fps=24)
        
        # 클립 닫기 (꼭 해 주어야 함)
        clip.close()
        
        # 작업 완료 메시지 출력
        print("영상 자르기 완료!")