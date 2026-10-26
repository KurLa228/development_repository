import math
import time

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

ksc_x, ksc_y, ksc_z = 0.0, 0.0, 0.0
ship_x = 5000.0

print("Начинаем симуляцию полета...")

for i in range(5):
    last_x = ship_x
    ship_x -= 1000.0
    
    current_dist = calculate_distance(ksc_x, ksc_y, ksc_z, ship_x, 0, 0)
    last_dist = calculate_distance(ksc_x, ksc_y, ksc_z, last_x, 0, 0)
    
    print(f"Шаг {i+1}. Расстояние: {round(current_dist)} м.")
    
    if current_dist < last_dist:
        print(" -> Приближаемся!")
    else:
        print(" -> Отдаляемся!")
    
    time.sleep(1)
