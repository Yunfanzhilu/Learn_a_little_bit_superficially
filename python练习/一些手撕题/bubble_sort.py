import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 每次内循环把最大的数移动到最后面
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # 交换相邻两个数的位置
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            # 打印每次交换后的列表
            print(f"Pass {i+1}, swap {j+1}: {arr}")
    
    return arr



# 测试用例
def test_bubble_sort():
    # 测试一个空列表
    assert bubble_sort([]) == []
    # 测试一个元素的列表
    assert bubble_sort([42]) == [42]
    # 测试多个元素的无序列表
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort(input_list) == expected_output

    # 测试多个元素的有序列表
    input_list = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected_output

    # 测试多个元素的逆序列表
    input_list = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected_output

    # 测试大量元素的随机列表
    input_list = random.sample(range(1000), 100)
    expected_output = sorted(input_list)
    assert bubble_sort(input_list) == expected_output

    print("All test cases pass")


if __name__ == "__main__":
    test_bubble_sort()
