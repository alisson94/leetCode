#1 forca bruta
def twoSumBruteForce(nums, target):
        indice = [0,0]

        for i in range(len(nums)):
            indice[0] = i
            for j in range(i+1, len(nums)):
                indice[1] = j
                if indice[0] + indice[1] == target:
                    return target
                
#2 dois ponteiros, tem q ordenar antes, DEU ERRADO
def twoSumTwoPointers(nums, target):
    copy = nums.copy()
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            indexLeft = copy.index(nums[left])
            indexR = copy[indexLeft+1:].index(nums[right]) + indexLeft + 1
            return (indexLeft, indexR)
        
        elif nums[left] + nums[right] < target:
                left+=1
        else:
                right -=1

#print(twoSum([3,3], 6))

#3 hash table / dicionario
def twoSumHash(nums, target):
    
    hash = dict()
    
    for i in range(len(nums)):
        elemento = nums[i] 
        if target - elemento in hash:
            return (hash[target - elemento], i)
        
        hash[elemento] = i

print(twoSumHash([3,2,4], 6))