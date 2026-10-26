import math

R_kerbin = 600000.0
altitude = 100000.0
g = 9.81
v_fall = math.sqrt(2 * g * altitude)
time_to_fall = math.sqrt(2 * altitude / g)
burn_time = 30.0
distance_to_burn = v_fall * burn_time

print(f"Высота: {altitude / 1000:.1f} км")
print(f"Скорость падения: {v_fall:.1f} м/с")
print(f"Время падения: {time_to_fall:.1f} с")
print(f"Включить двигатели за: {burn_time} с до падения")
print(f"Дистанция до включения: {distance_to_burn / 1000:.1f} км")
print("Направление: SAS Retrograde")