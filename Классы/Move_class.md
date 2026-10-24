# Move_class

**Файл:** `Machines/Move_class.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Move_class.cs` · **Тип:** `World_class_move` → [[World_commands#World_class_move|базовый класс]]

## Назначение
Физический «корпус» машины: грани, точки входа/выхода, поиск соседей.

## Поля
- `myBox` (Vector3) — размер в клетках.
- `input_ore` / `output_ore` — List\<`Date_two_list`\> (x, y, грань `Napr`).
- `gam_inp` / `gam_out` — найденные соседние машины.
- `MyCoords` — координаты ячеек граней (пересчёт в `Trigers`).

## Логика
- `Awake` — требует компонент `IF_move_functional` (делегирует ему работу с рудой).
- `Trigers(Update_Block)` — `GetSurfaceCoordsBySide` → для каждой точки входа ищет в [[Config]] объекты `Player_Block`, фильтрует по совпадению стороны (`test_napr_get` + `GetSideFacing`).
- `test_napr_get(g, dm)` — смотрит ли сторона объекта `g` на нас (INPUT/OUTPUT).
- `UpTestError` — уникальность точек входа/выхода и отсутствие пересечений (`CoordKey`).

## Зависимости
[[World_commands]] · [[Config]] · [[MainSystemTrigers]].

## Кто использует
[[Conveir]], [[Mine_ore]], [[Core_res]] (через RequireComponent) — сам [[Ore]] находит руду через `World_class_move.get_ore`.

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
