def solution(m, musicinfos):
    def parse_melody(melody):
        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        return melody

    def generate_played_melody(start, end, melody):
        played_melody = ""
        melody_len = len(melody)
        for i in range(end - start):
            played_melody += melody[i % melody_len]
        return played_melody

    m = parse_melody(m)
    answer = "(None)"
    max_play_time = 0

    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        start_time = int(info[0][:2]) * 60 + int(info[0][3:])
        end_time = int(info[1][:2]) * 60 + int(info[1][3:])
        play_time = end_time - start_time
        title = info[2]
        melody = parse_melody(info[3])

        played_melody = generate_played_melody(start_time, end_time, melody)

        if m in played_melody and play_time > max_play_time:
            max_play_time = play_time
            answer = title

    return answer