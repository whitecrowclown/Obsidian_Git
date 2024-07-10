import total_cut_index.Length_movie as play_movie
import total_cut_index.one_cut as cut

# 영화 제목
movie_title = "태번 마스터 제작진의 또다른 후속작 - 대장장이 마스터"
play_time = play_movie.lengthing(movie_title)
cut.cutting(movie_title, play_time)