from pydub import AudioSegment
filename = 'D:/code/vscodeworkplace/homework/neural_net_homework/first0919/num.mp3'
audio_segment = AudioSegment.from_file(filename, format='mp3')


# 生成26个英文字母
# char_dx = [chr(i) for i in range(65, 91)]
# char_xx = [chr(i) for i in range(97, 123)]
# print('26个大写字母：', char_dx)
# print('26个小写字母：', char_xx)

total = int(audio_segment.duration_seconds / 1)  # 计算音频切片后的个数
for i in range(total):
    # 将音频1s切片，并以顺序进行命名
    audio_segment[i*1000:(i+1) *
                  1000].export("C:/Users/rg16x/Desktop/NNDL作业_第一次作业_2022540056_夏艳薇_智研221/2022540056/number_sound/"+str(i)+".mp3", format="mp3")

    # audio_segment[i*1000:(i+1) *
    #               1000].export("number/{0}.wav".format(i), format="wav")

#  缺少结尾的音频片段
audio_segment[total *
              10000:].export("C:/Users/rg16x/Desktop/NNDL作业_第一次作业_2022540056_夏艳薇_智研221/2022540056/00000.mp3", format="mp3")
