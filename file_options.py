import os

def txt_file_steaching():
    dir_list = os.listdir()
    txt_files_list = [file for file in dir_list if '.txt' == file[len(file) - 4 :] and file != 'out.txt']
    lines_list = []
    tmp_box = {}

    for file in txt_files_list:
        with open(file, encoding='utf-8') as f:
            tmp_file = f.readlines()
            len_tmp_file = len(tmp_file)
            lines_list.append(len_tmp_file)
            tmp_box[len_tmp_file] = (file, tmp_file)

    lines_list.sort()

    with open('out.txt', 'w', encoding='utf-8') as f:
        for lines in lines_list:
            f.write(tmp_box[lines][0])
            f.write('\n')
            f.write(str(lines))
            f.write('\n')
            f.writelines(tmp_box[lines][1])
            f.write('\n')

