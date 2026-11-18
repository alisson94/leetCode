#força bruta
#dá time limit em um dos testes

def maxAreaBrute(height) -> int:
    area = 0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            temp_area = (j-i) * min(height[i], height[j])

            if temp_area > area:
                area = temp_area

    return area


#nova solucao:

def maxArea(height):
    left, right = 0, len(height) - 1
    area = 0
    while left <= right:
        newarea = (right - left) * min(height[left], height[right])
        if newarea > area:
            area = newarea
        if height[left] < height[right]:
            left+=1
            continue

        right-=1

    return area