import math

# 计算两个物体是否相撞（两个物体的距离）
def distance(bx, by, ex, ey):
    a = (bx+70) - (ex+52)
    b = (by+40) - (ey-42)
    if math.sqrt(a*a + b*b) < 122:
        return True
    else:
        return False