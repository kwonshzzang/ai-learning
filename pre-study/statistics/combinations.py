from itertools import combinations

arr = ['A', 'B', 'C']

# 원소 중에서 2개를 뽑는 모든 조합 계산
result = list(combinations(arr, 2))
print(result)