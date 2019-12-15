def create_char_range_list():
    char_range_list = []
    char_range_list.append([32, 127])
    char_range_list.append([51887, 51904]) #使うかもしれない半角記号1 128〜143
    char_range_list.append([52095, 52160]) #使うかもしれない半角記号2 144〜207
    char_range_list.append([52351, 52416]) #使うかもしれない半角記号3 208〜271
    char_range_list.append([14909567, 14909600]) #使うかもしれない全角記号 272〜303
    char_range_list.append([14909823, 14909888]) #ひらがな、カタカナ1 304〜367
    char_range_list.append([14910079, 14910144]) #ひらがな、カタカナ2 368〜431
    char_range_list.append([14910335, 14910400]) #ひらがな、カタカナ3 432〜495
    for i in range(8):  char_range_list.append([14989439+i*256, 14989504+i*256]) #使うかもしれない漢字1 496〜1007
    for i in range(64): char_range_list.append([15040639+i*256, 15040704+i*256]) #使うかもしれない漢字2 1008〜5103
    for i in range(64): char_range_list.append([15106175+i*256, 15106240+i*256]) #使うかもしれない漢字3 5104〜9199
    for i in range(64): char_range_list.append([15171711+i*256, 15187904+i*256]) #使うかもしれない漢字4 9200〜13295
    for i in range(64): char_range_list.append([15237247+i*256, 15237312+i*256]) #使うかもしれない漢字5 13296〜17391
    for i in range(64): char_range_list.append([15302783+i*256, 15302848+i*256]) #使うかもしれない漢字6 17392〜21295
  
    char_range_list.append([52913, 52928]) # ギリシャ α~
    char_range_list.append([53120, 53414]) # ギリシャ π~Х
    char_range_list.append([52892]) # ギリシャ Μ
    char_range_list.append([49831]) # §
    char_range_list.append([50071]) # ×
    char_range_list.append([49826,49855+1])
    char_range_list.append([50055,50108+1])
    char_range_list.append([50305,50335+1])
    char_range_list.append([50571,50605+1])
    char_range_list.append([50571,50605+1])
  
    char_range_list.append([15711361, 15711421]) # 全角記号・数字・アルファベット
    char_range_list.append([15711617, 15711642]) # 全角アルファベット小文字
    char_range_list.append([14844053]) # ―
    char_range_list.append([14844070]) # …
    char_range_list.append([14844091]) # ※
    char_range_list.append([15711644]) # ｜
    char_range_list.append([14844060]) # “
    char_range_list.append([14844061]) # ”
    char_range_list.append([14844083]) # ″
    char_range_list.append([14845586]) # →
    char_range_list.append([15711646]) # ～
    char_range_list.append([14849152]) # ─
  
    char_range_list.append([14844048,14844071]) # 記号
    char_range_list.append([14845344,14845578]) # ローマ数字とか
    char_range_list.append([14850474]) # ♪
    char_range_list.append([14850182]) # ☆
    char_range_list.append([14844092]) # ‼
    char_range_list.append([14844297]) # ⁉
    char_range_list.append([14844296]) # ⁈
  
    char_range_and_num_list = []
    num = 0
    for l in char_range_list:
        if len(l) == 1:
            char_range_and_num_list.append([num, l[0]])
            num += 1
        else:
            char_range_and_num_list.append([num, l[0], l[1]])
            num += l[1] - l[0]
    return char_range_and_num_list

def char2ID(c, li):
    utf8 = int.from_bytes(c.encode("utf-8"), 'big') #文字をutf8に変換
    for l in li:
        if len(l) == 2 and utf8 == l[1]: 
            return l[0]
        if len(l) == 3 and utf8 >= l[1] and utf8 < l[2]:
            return l[0] + utf8 - l[1]
    return -1