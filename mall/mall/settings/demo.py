# 快速排序

def quick_sort(sequ):
    if len(sequ) < 2:
        return sequ

    temp = sequ[0]
    left_sequ = [x for x in sequ if x < temp]
    right_sequ = [x for  x in sequ if x > temp]

    return quick_sort(left_sequ) + [temp] + quick_sort(right_sequ)

print(quick_sort([1,4,3,2,7,5,8,6]))

@@@@