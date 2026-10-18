import krpc

# Подключение к серверу kRPC
conn = krpc.connect(name='Set ISS Docking Target')
space_center = conn.space_center

# 1. Проверяем, что мы управляем шаттлом
vessel = space_center.active_vessel
if vessel.name != 'SHUTTLE':
    print(f"Внимание: активный аппарат '{vessel.name}', а не 'SHUTTLE'")
else:
    print("Управляем аппаратом SHUTTLE")

# 2. Ищем станцию ISS среди всех аппаратов
iss_vessel = None
for v in space_center.vessels:
    if v.name == 'Центральный модуль космической станции':
        iss_vessel = v
        break

if iss_vessel is None:
    print("Ошибка: станция ISS не найдена!")
    exit()

print("Станция ISS найдена")

# 3. Ищем стыковочный узел DockingPort2 на станции ISS
target_port = None
for port in iss_vessel.parts.docking_ports:
    # Сравниваем имя детали (part.name) с искомым
    if port.part.name == 'dockingPort2':
        target_port = port
        break

# 4. Устанавливаем цель
if target_port is not None:
    space_center.target_docking_port = target_port
    print("Цель успешно установлена: DockingPort2 на станции ISS")
else:
    print("Стыковочный узел 'DockingPort2' не найден на станции ISS")
    # Для отладки можно вывести все доступные узлы
    print("Доступные узлы на ISS:")
    for port in iss_vessel.parts.docking_ports:
        print(f" - {port.part.name}")
