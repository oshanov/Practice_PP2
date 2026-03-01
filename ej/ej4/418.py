import sys

def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        x1, y1 = map(float, line1)
        
        line2 = sys.stdin.readline().split()
        if not line2: return
        x2, y2 = map(float, line2)
    except EOFError:
        return

    y1_abs = abs(y1)
    y2_abs = abs(y2)
    
    # Формула на основе подобия треугольников
    x = (x1 * y2_abs + x2 * y1_abs) / (y1_abs + y2_abs)
    
    print(f"{x:.10f} {0.0:.10f}")

if __name__ == "__main__":
    solve()