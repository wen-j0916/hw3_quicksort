def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_index = start  # 以起始位置作為 pivot
    pivot = array[pivot_index]
    left = start
    right = end

    print('起始範圍:%s，pivot:%s'%(array[start:end+1],pivot))
    while left != right:
        # 從右邊往左找比 pivot 小的值
        while array[right] >= pivot and left < right:
            right -= 1
        # 從左邊往右找比 pivot 大的值
        while array[left] <= pivot and left < right:
            left += 1
        # 交換左右兩邊找到的數值
        if left < right:
            array[left], array[right] = array[right], array[left]
            print('交換:',array)
    # 最後將 pivot 放到正確的位置
    array[start], array[left] = array[left], array[start]
    print("pivot放置完成:",array)
    # 遞迴處理左右區間
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


array = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("原始資料:",array)
quick_sort(array, 0, len(array) - 1)
print("排序結果:", array)
