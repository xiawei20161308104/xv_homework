from PIL.Image import open

code_number = 0
number_data = open(
    'D:/code/vscodeworkplace/homework/neural_net_homework/first0919/num.jpg')
number_size = number_data.size
num_r = number_size[0]
num_c = number_size[1]
# # 生成26个英文字母
char_dx = [chr(i) for i in range(65, 91)]
char_xx = [chr(i) for i in range(97, 123)]
zeronum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
newdx = char_dx+char_xx+zeronum
print('52个大写字母：', newdx)
# print('26个小写字母：', char_xx)

for i in range(11):
    for j in range(10):
        want_split_r = int(num_r/10)
        want_split_c = int(num_r/16)
        box = (want_split_r*j, want_split_c*i,
               want_split_r*(j+1), want_split_c*(i+1))

        crop_number_data = number_data.crop(box)
        # crop_number_data.show()

        number_name = str(code_number) + ".jpg"
        # name = str(newdx[code_number])
        # name = name+".jpg"
        # print(name)
        # 生成单独文件名称，到这里都是可以正常打印的。加上下面的保存就不可以了
        # crop_number_data.save(
        #     "C:/Users/rg16x/Desktop/NNDL作业_第一次作业_2022540056_夏艳薇_智研221/2022540056/letter"
        #     + "/"+name)
        crop_number_data.save(
            "C:/Users/rg16x/Desktop/NNDL作业_第一次作业_2022540056_夏艳薇_智研221/2022540056/number"
            + "/"+number_name)
        code_number += 1
