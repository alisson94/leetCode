def findMedianSortedArrays(nums1, nums2) -> float:

    soma = 0
    for i in range(len(nums2)):
        if nums2[i] in nums1:
            nums1[nums1.index(nums2[i])] = 0
            soma += nums2[i]
        else:
            nums1.append(nums2[i])

    for i in range(len(nums1)):
        soma += nums1[i]

    return soma/len(nums1)

print(findMedianSortedArrays([1,3], [2]))