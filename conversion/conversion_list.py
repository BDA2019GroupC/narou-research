def create_char_range_list():
    char_range_list = []
    char_range_list.append([32, 127])
    char_range_list.append([14909568, 14909631]) # 3byte記号

    for i in range(3):  char_range_list.append([14909824+i*256, 14909887+i*256]) # ひらがな、カタカナ

    for i in range(8):  char_range_list.append([14989440+i*256, 14989503+i*256])  # 使うかもしれない漢字1
    for i in range(64): char_range_list.append([15040640+i*256, 15040703+i*256]) # 使うかもしれない漢字2
    for i in range(64): char_range_list.append([15106176+i*256, 15106239+i*256]) # 使うかもしれない漢字3
    for i in range(64): char_range_list.append([15171712+i*256, 15171775+i*256]) # 使うかもしれない漢字4
    for i in range(64): char_range_list.append([15237248+i*256, 15237311+i*256]) # 使うかもしれない漢字5
    for i in range(64): char_range_list.append([15302784+i*256, 15302847+i*256]) # 使うかもしれない漢字6

    for i in range(2):  char_range_list.append([15711360+i*256, 15711423+i*256]) # 全角記号・数字・アルファベット
    char_range_list.append([15711872, 15711903]) # 半角カタカナ
    for i in range(2):  char_range_list.append([14844032+i*256, 14844095+i*256]) # 一般句読点


    char_range_list.append([14849152]) # ─
    char_range_list.append([14850464, 14850479]) # 音符とか記号
    char_range_list.append([14850176, 14850191]) # ☆とか記号

    char_range_list.append([49824, 49855]) # §とか´などの2byte記号
    for i in range(6):  char_range_list.append([50048+i*256, 50095+i*256]) # ラテン語修飾1
    for i in range(5):  char_range_list.append([51584+i*256, 51631+i*256]) # ラテン語修飾2 と IPA拡張と合成修飾文字
    for i in range(2):  char_range_list.append([52864+i*256, 52927+i*256]) # ギリシア文字及びコプト文字
    for i in range(4):  char_range_list.append([53376+i*256, 53439+i*256]) # キリル文字
    char_range_list.append([54400, 54463]) # キリル文字補助
    char_range_list.append([54656, 54719]) # アルメニア文字
    for i in range(2):  char_range_list.append([54912+i*256, 54975+i*256]) # ヘブライ文字
    for i in range(4):  char_range_list.append([55424+i*256, 55487+i*256]) # アラビア文字
    char_range_list.append([15710608, 15710639]) # 小字形

    char_range_list.append([14845312, 14845375]) # 数字に準ずるもの
    for i in range(10):  char_range_list.append([14845568+i*256, 14845631+i*256]) # 矢印、数学、技術記号
    for i in range(3):  char_range_list.append([14848384+i*256, 14848447+i*256]) # 囲み英数字
    for i in range(4):  char_range_list.append([14912640+i*256, 14912703+i*256]) # 単位
    char_range_list.append([14845056, 14845119]) # 単位2

    char_range_list.append([14849696, 14849727]) # 幾何学記号1
    char_range_list.append([14849920, 14849983]) # 幾何学記号2

    char_range_list.append([14851229]) # ✝
    char_range_list.append([14851228]) # ✜
    char_range_list.append([14851492]) # ❤
    char_range_list.append([15710350]) # 変なスペース？      ←無視して良いかも
    char_range_list.append([15710351]) # 変なスペース2？    ←無視して良いかも
    char_range_list.append([14849153]) # ━
    char_range_list.append([15712163]) # ￣
    char_range_list.append([14850963]) # ⛓
    char_range_list.append([14849160]) # ┈
    char_range_list.append([14851263]) # ✿
    char_range_list.append([14850432]) # ♀
    char_range_list.append([14851745]) # ➡
    char_range_list.append([14849157]) # ┅
    char_range_list.append([14850434]) # ♂
    char_range_list.append([14850730]) # ⚪
    char_range_list.append([14849155]) # ┃
    char_range_list.append([15712165]) # ￥
    char_range_list.append([14849164]) # ┌
    char_range_list.append([14849168]) # ┐
    char_range_list.append([14727569]) # ๑
    char_range_list.append([14849672]) # █
    char_range_list.append([14851221]) # ✕
    char_range_list.append([50103]) # ÷
    char_range_list.append([14849154]) # │
    char_range_list.append([14849167]) # ┏
    char_range_list.append([14851239]) # ✧
    char_range_list.append([14850195]) # ☓

    char_range_and_num_list = []
    num = 0
    for l in char_range_list:
        if len(l) == 1:
            char_range_and_num_list.append([num, l[0]])
            num += 1
        else:
            char_range_and_num_list.append([num, l[0], l[1]])
            num += (l[1] - l[0] + 1)
            num
    return char_range_and_num_list

def print_if_sentence_char2ID(filename, li):
    with open(filename,"a") as f:
        f.write("def char2ID(c):\n")
        f.write("\tutf8 = int.from_bytes(c.encode(\"utf-8\"), 'big')\n")
        for elm in li:
            if len(elm) == 2:
                f.write("\tif utf8 == {}:\n".format(elm[1]))
                f.write("\t\treturn {} + 32\n".format(elm[0]))
            if len(elm) == 3:
                f.write("\tif utf8 >= {} and utf8 <= {}:\n".format(elm[1],elm[2]))
                f.write("\t\treturn {} + utf8 - {} + 32\n".format(elm[0],elm[1]))
        f.write("\treturn -1\n")

def print_if_sentence_ID2char(filename, li):
    with open(filename,"a") as f:
        f.write("def ID2char(id):\n")
        f.write("\tid = id - 32\n")
        for i in range(len(li)-1):
            if len(li[i]) == 2:
                f.write("\tif id == {}:\n".format(li[i][0]))
                f.write("\t\treturn {}.to_bytes(16, 'big').decode(\"utf-8\")[-1]\n".format(li[i][1]))
            if len(li[i]) == 3:
                f.write("\tif id >= {} and id < {}:\n".format(li[i][0], li[i+1][0]))
                f.write("\t\treturn ({} + id - {}).to_bytes(16, 'big').decode(\"utf-8\")[-1]\n".format(li[i][1], li[i][0]))
        i = len(li)-1
        if len(li[i]) == 2:
            f.write("\tif id == {}:\n".format(li[i][0]))
            f.write("\t\treturn {}.to_bytes(16, 'big').decode(\"utf-8\")[-1]\n".format(li[i][1]))
        if len(li[i]) == 3:
            f.write("\tif id >= {}:\n".format(li[i][0]))
            f.write("\t\treturn ({} + id - {}).to_bytes(16, 'big').decode(\"utf-8\")[-1]\n".format(li[i][1], li[i][0]))
        f.write("\treturn -1\n")
