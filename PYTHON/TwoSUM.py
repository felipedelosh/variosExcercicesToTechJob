"""
Dado un array de números enteros y un número objetivo, escribe una función que devuelva los índices de los dos números que sumen el objetivo.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (porque nums[0] + nums[1] = 9)
"""

target = 9
arr = [2, 11, 8, 7, 15, 1, 0, 9]
_find = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Encontrado: ", i, j)
            _find = True
            break
    
    if _find:
        break