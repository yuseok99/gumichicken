## arr에서 특정 원소 두 개 뽑아 두 수의 합이 target과 같을 수 있는지 확인

def count_table(arr, k):
    table = [0] * (k+1)
    for num in arr:
        if 0 <= num <= k:
            table[num] += 1
    return table

def solution(arr, target):
    table = count_table(arr, target)
    for num in arr:
        complement = target - num
        if 0 <= complement <= target:
            if complement == num:
                if table[num] >= 2:
                    return True
            else:
                if table[complement] >= 1:
                    return True
    
    return False
