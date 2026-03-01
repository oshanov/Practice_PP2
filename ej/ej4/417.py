import math

def solve():
    try:
        # Чтение входных данных
        line1 = input().split()
        if not line1: return
        r = float(line1[0])
        
        line2 = input().split()
        if not line2: return
        x1, y1 = map(float, line2)
        
        line3 = input().split()
        if not line3: return
        x2, y2 = map(float, line3)
    except EOFError:
        return

    # Вектор направления dx, dy
    dx = x2 - x1
    dy = y2 - y1
    
    # Квадратное уравнение для t: |A + t*D|^2 <= R^2
    # (x1 + t*dx)^2 + (y1 + t*dy)^2 <= R^2
    # t^2 * (dx^2 + dy^2) + t * 2*(x1*dx + y1*dy) + (x1^2 + y1^2 - R^2) <= 0
    
    a = dx**2 + dy**2
    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - r**2
    
    # Если точки совпадают (a == 0)
    if a == 0:
        if x1**2 + y1**2 <= r**2 + 1e-9:
            print(f"{0.0:.10f}")
        else:
            print(f"{0.0:.10f}")
        return

    # Дискриминант
    dist = b**2 - 4*a*c
    
    if dist < 0:
        # Отрезок полностью вне круга
        print(f"{0.0:.10f}")
        return
    
    # Корни уравнения (пересечение прямой с окружностью)
    t1 = (-b - math.sqrt(dist)) / (2 * a)
    t2 = (-b + math.sqrt(dist)) / (2 * a)
    
    # Находим пересечение интервалов [t1, t2] и [0, 1]
    t_start = max(0, t1)
    t_end = min(1, t2)
    
    if t_start < t_end:
        # Длина отрезка = доля t * полная длина
        full_dist = math.sqrt(dx**2 + dy**2)
        result = (t_end - t_start) * full_dist
        print(f"{result:.10f}")
    else:
        print(f"{0.0:.10f}")

if __name__ == "__main__":
    solve()