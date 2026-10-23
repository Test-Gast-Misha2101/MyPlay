# Core_res

**Файл:** `Machines/Core_res.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Core_res.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Conveir](Классы/Conveir.md))

## Назначение
«Ядро» — склад ресурсов и их источник для игрока.

## Поля
- `MainCam` (public set) — камера игрока, назначается из [Config](Классы/Config.md).created_pl.
- `dic` — Dictionary\<string, int\>: все руды из [BaseDate](Классы/BaseDate.md) со стартовым запасом 0.

## Логика
- `Awake` — заполняет словарь всеми известными рудами.
- `Up_Func_Ore` — принимает руду с соседей (через `World_class_move.get_ore`), увеличивает запас; новые руды дозаполняются.
- `move_ore()` — Null (ядро не отдаёт руду дальше).
- `get_ore_entity(entity, ore, len_ore)` — выдаёт ресурс, если тег `entity == "Player"` и запаса хватает.

## Зависимости
[World_commands](Классы/World_commands.md) · [BaseDate](Классы/BaseDate.md) · [ORE_BLOCK](Классы/ORE_BLOCK.md) · [Move_class](Классы/Move_class.md) · [Conveir](Классы/Conveir.md).

## Кто использует
[Core_Spawn](Классы/Core_Spawn.md) (RequireComponent, передача MainCam), [Config](Классы/Config.md).created_pl.

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
