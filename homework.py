import random

'''
x是丁y是柯
'''

candidate = {
    "丁守中": {
        "松山區": 46381,
        "信義區": 53955,
        "大安區": 72325,
        "中山區": 46746,
        "中正區": 33897,
        "大同區": 20763,
        "萬華區": 38666,
        "文山區": 68586,
        "南港區": 26282,
        "內湖區": 61566,
        "士林區": 55954,
        "北投區": 52445
    },
    "柯文哲": {
        "松山區": 42356,
        "信義區": 47762,
        "大安區": 60939,
        "中山區": 50604,
        "中正區": 33752,
        "大同區": 31679,
        "萬華區": 43411,
        "文山區": 56479,
        "南港區": 28896,
        "內湖區": 65599,
        "士林區": 63247,
        "北投區": 56096
    }
}

def ding_sum_vote(vo_data): ##要記得改成candidate
    ding_district = vo_data['丁守中']
    print('=====第一輪=====')
    while True:
        ding_chose_district1 = input("請輸入行政區:")
        if ding_chose_district1 in ding_district:
            x1 = ding_district[ding_chose_district1]
            print('你選擇的行政區是{}，丁守中在此區的得票數是{:,}票'.format(ding_chose_district1, x1))
            break
        else:
            print('輸入錯誤')
            continue

    KP_district = vo_data['柯文哲']
    key_KP_district =list(KP_district.keys())
    random.shuffle(key_KP_district)
    KP_chose_district1 = key_KP_district[0]
    y1 = KP_district[KP_chose_district1]
    print('系統選擇的行政區是{}，柯文哲在此處的得票數是{:,}票'.format(KP_chose_district1, y1))
    count_round(x1,y1)

    print('')
    print('=====第二輪=====')
    while True:
        ding_chose_district2 = input("請輸入行政區(請勿重複選擇):")
        if ding_chose_district2 == ding_chose_district1:
            print('請勿重複選擇')
            continue
        elif ding_chose_district2 in ding_district:
            x2 = ding_district[ding_chose_district2]
            print('你選擇的行政區是{}，丁守中在此區的得票數是{:,}票'.format(ding_chose_district2, x2))
            break
        else:
            print('輸入錯誤')
            continue

    KP_chose_district2 = key_KP_district[1]
    y2 = KP_district[KP_chose_district2]
    print('系統選擇的行政區是{}，柯文哲在此處的得票數是{:,}票'.format(KP_chose_district2, y2))
    count_round((x1+x2),(y1+y2))

    print('')
    print('=====第三輪=====')
    while True:
        ding_chose_district3 = input("請輸入行政區(請勿重複選擇):")
        if ding_chose_district3 == ding_chose_district1:
            print('請勿重複選擇')
            continue
        elif ding_chose_district3 == ding_chose_district2:
            print('請勿重複選擇')
            continue
        elif ding_chose_district3 in ding_district:
            x3 = ding_district[ding_chose_district3]
            print('你選擇的行政區是{}，丁守中在此區的得票數是{:,}票'.format(ding_chose_district3, x3))
            break
        else:
            print('輸入錯誤')
            continue

    KP_chose_district3 = key_KP_district[2]
    y3 = KP_district[KP_chose_district3]
    print('系統選擇的行政區是{}，柯文哲在此處的得票數是{:,}票'.format(KP_chose_district3, y3))
    count_round((x1+x2+x3),(y1+y2+y3))
    final_count((x1+x2+x3),(y1+y2+y3))

def KP_sum_vote(vo_data): ##要記得改成candidate
    KP_district = vo_data['柯文哲']
    print('=====第一輪=====')
    while True:
        KP_chose_district1 = input("請輸入行政區:")
        if KP_chose_district1 in KP_district:
            y1 = KP_district[KP_chose_district1]
            print('你選擇的行政區是{}，柯文哲在此區的得票數是{:,}票'.format(KP_chose_district1, y1))
            break
        else:
            print('輸入錯誤')
            continue

    ding_district = vo_data['丁守中']
    key_ding_district =list(ding_district.keys())
    random.shuffle(key_ding_district)
    ding_chose_district1 = key_ding_district[0]
    x1 = ding_district[ding_chose_district1]
    print('系統選擇的行政區是{}，丁守中在此處的得票數是{:,}票'.format(ding_chose_district1, x1))
    count_round(x1,y1)

    print('')
    print('=====第二輪=====')
    while True:
        KP_chose_district2 = input("請輸入行政區(請勿重複選擇):")
        if KP_chose_district2 == KP_chose_district1:
            print('請勿重複選擇')
            continue
        elif KP_chose_district2 in KP_district:
           y2 = KP_district[KP_chose_district2]
           print('你選擇的行政區是{}，柯文哲在此區的得票數是{:,}票'.format(KP_chose_district2, y2))
           break
        else:
            print('輸入錯誤')
            continue

    ding_chose_district2 = key_ding_district[1]
    x2 = ding_district[ding_chose_district2]
    print('系統選擇的行政區是{}，丁守中在此處的得票數是{:,}票'.format(ding_chose_district2, x2))
    count_round((x1+x2),(y1+y2))

    print('')
    print('=====第三輪=====')
    while True:
        KP_chose_district3 = input("請輸入行政區(請勿重複選擇):")
        if KP_chose_district3 == KP_chose_district1:
            print('請勿重複選擇')
            continue
        elif KP_chose_district3 == KP_chose_district2:
            print('請勿重複選擇')
            continue
        elif KP_chose_district3 in KP_district:
            y3 = KP_district[KP_chose_district3]
            print('你選擇的行政區是{}，柯文哲在此區的得票數是{:,}票'.format(KP_chose_district3, y3))
            break
        else:
            print('輸入錯誤')
            continue

    ding_chose_district3 = key_ding_district[2]
    x3 = ding_district[ding_chose_district3]
    print('系統選擇的行政區是{}，丁守中在此處的得票數是{:,}票'.format(ding_chose_district3, x3))
    count_round((x1+x2+x3),(y1+y2+y3))
    final_count((x1+x2+x3),(y1+y2+y3))

def count_round(x,y): ##丁先柯後
    if x > y:
        print('目前丁守中領先，總共領先票數為{:,}票'.format(x-y))
    else:
        print('目前柯文哲領先，總共領先票數為{:,}票'.format(y-x))

def final_count(x,y):
    print('')
    print('=====最終贏家=====')
    if x > y:
        print('最終贏家:丁守中')
        print('總獲得票數{:,}票'.format(x))
        print('贏得對手{:,}票'.format(x-y))
    else:
        print('最終贏家:柯文哲')
        print('總獲得票數{:,}票'.format(y))
        print('贏得對手{:,}票'.format(y-x))

def main():
    print('=====今晚誰來當家=====')
    print('您可以選擇支持丁守中或柯文哲，')
    print(' 並在三輪的開票中，選擇開票的行政區。')
    print('系統將隨機選取行政區與您對決，')
    print('最終獲勝票數最多的候選人即為贏家。')
    print('')
    print('行政區參考：松山區、信義區、大安區、中山區、中正區、')
    print('大同區、萬華區、文山區、南港區、內湖區、士林區、北投區')
    print('')

    while True:
        chose_can = input('請輸入候選人(柯文哲/丁守中):')
        if chose_can == '丁守中':
            ding_sum_vote(candidate)
            break
        elif chose_can == '柯文哲':
            KP_sum_vote(candidate)
            break
        else:
            print('輸入錯誤')
            continue

if __name__ == "__main__":
    main()



    