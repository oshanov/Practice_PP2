import math
import sys

def solve_419():
    input_data = sys.stdin.read().split()
    if not input_data: return
    r = float(input_data[0])
    x1, y1 = float(input_data[1]), float(input_data[2])
    x2, y2 = float(input_data[3]), float(input_data[4])

    d2 = (x2 - x1)**2 + (y2 - y1)**2
    d = math.sqrt(d2)
    
    # Проверка на пересечение отрезка с кругом
    # Расстояние от (0,0) до прямой AB
    area = abs(x1*y2 - x2*y1)
    h = area / d
    
    # Проекция центра на прямую AB должна лежать на отрезке
    dot_a = x1*(x2-x1) + y1*(y2-y1)
    dot_b = x2*(x1-x2) + y2*(y1-y2)
    
    if h >= r or dot_a >= 0 or dot_b >= 0:
        print(f"{d:.10f}")
    else:
        # Длины касательных
        l1 = math.sqrt(x1**2 + y1**2 - r**2)
        l2 = math.sqrt(x2**2 + y2**2 - r**2)
        
        # Углы
        alpha = math.acos(r / math.sqrt(x1**2 + y1**2))
        beta = math.acos(r / math.sqrt(x2**2 + y2**2))
        gamma = math.acos((x1*x2 + y1*y2) / (math.sqrt(x1**2 + y1**2) * math.sqrt(x2**2 + y2**2)))
        
        arc_angle = gamma - alpha - beta
        print(f"{l1 + l2 + r * arc_angle:.10f}")

solve_419()

#There is a circular lake centered at (0;0) with radius R. A person starts at point A(x1;y1) and wants to reach point B(x2;y2) 
#without entering the circle. The path may touch the boundary. Points A and B
#are guaranteed to be on or outside the circle. Find the length of the shortest possible path.