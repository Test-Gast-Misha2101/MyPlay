# Core_res

**Файл:** `Machines/Core_res.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Core_res.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Conveir](Conveir.md))

## Назначение
«Ядро» — склад ресурсов и их источник для игрока.

## Поля
- `MainCam` (public set) — камера игрока, назначается из [Config](Config.md).created_pl.
- `dic` — Dictionary\<string, int\>: все руды из [BaseDate](BaseDate.md) со стартовым запасом 0.

## Логика
- `Awake` — заполняет словарь всеми известными рудами.
- `Up_Func_Ore` — принимает руду с соседей (через `World_class_move.get_ore`), увеличивает запас; новые руды дозаполняются.
- `move_ore()` — Null (ядро не отдаёт руду дальше).
- `get_ore_entity(entity, ore, len_ore)` — выдаёт ресурс, если тег `entity == "Player"` и запаса хватает.

## Зависимости
[World_commands](World_commands.md) · [BaseDate](BaseDate.md) · [ORE_BLOCK](ORE_BLOCK.md) · [Move_class](Move_class.md) · [Conveir](Conveir.md).

## Кто использует
[Core_Spawn](Core_Spawn.md) (RequireComponent, передача MainCam), [Config](Config.md).created_pl.

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
