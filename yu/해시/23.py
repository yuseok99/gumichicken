# 속한노래가 많이 재생된 장르 >> 장르 내에서 많이 재생된 노래 >> 장르 내에서 재생 횟수가 같은 노래중에서는 고유 번호가 낮은 노래
# 노래장르 나타내는 문자열 배열 genres 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질때 베스트엘범에 들어갈 노래의 고유번호를 순서대로 변환

def solution(genres, plays):
    answer = [ ]
    genres_dict = { }
    play_dict = { }

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genres_dict:
            genres_dict[genre] = [ ]
            play_dict[genre] = 0
        genres_dict[genre].append((i, play))
        play_dict[genre] += play

    sorted_genres = sorted(play_dict.items(), key = lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dict[genre], key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    return answer

