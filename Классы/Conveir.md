# Conveir

**Файл:** `Machines/Conveir.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Conveir.cs` · **Тип:** `IF_move_functional` (RequireComponent → [[Move_class]])

## Назначение
Конвейер — транспорт руды. Очередь из трёх слотов.

## Поля
`res1`, `res2`, `res3` (string) — слоты; по умолчанию `ORE_BLOCKS.Null`.

## Логика
- `Up_Func_Ore(gam_inp, gam_out)` — проталкивает руду вниз по цепочке (res1→res2→res3); если res1 пуст, забирает руду у соседней машины через `World_class_move.get_ore(gameObject)`.
- `move_ore()` — отдаёт руду из res3 и очищает слот.
- `get_ore_entity(...)` — заглушка (Null).

## Зависимости
[[World_commands]] (`IF_move_functional`) · [[Move_class]] · [[ORE_BLOCK]].

## Кто использует
[[Mine_ore]] и [[Core_res]] требуют его через RequireComponent; цепочка: Mine_ore → Conveir → Core_res.

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
