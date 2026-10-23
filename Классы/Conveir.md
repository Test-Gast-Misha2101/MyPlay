# Conveir

**Файл:** `Machines/Conveir.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Conveir.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Move_class](Классы/Move_class.md))

## Назначение
Конвейер — транспорт руды. Очередь из трёх слотов.

## Поля
`res1`, `res2`, `res3` (string) — слоты; по умолчанию `ORE_BLOCKS.Null`.

## Логика
- `Up_Func_Ore(gam_inp, gam_out)` — проталкивает руду вниз по цепочке (res1→res2→res3); если res1 пуст, забирает руду у соседней машины через `World_class_move.get_ore(gameObject)`.
- `move_ore()` — отдаёт руду из res3 и очищает слот.
- `get_ore_entity(...)` — заглушка (Null).

## Зависимости
[World_commands](Классы/World_commands.md) (`IF_move_functional`) · [Move_class](Классы/Move_class.md) · [ORE_BLOCK](Классы/ORE_BLOCK.md).

## Кто использует
[Mine_ore](Классы/Mine_ore.md) и [Core_res](Классы/Core_res.md) требуют его через RequireComponent; цепочка: Mine_ore → Conveir → Core_res.

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
