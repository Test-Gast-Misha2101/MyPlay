# ORE_BLOCK

**Файл:** `Ore/ORE_BLOCK.cs` · **Исходник:** `Assets\Scripts\Ore\ORE_BLOCK.cs`

## Содержимое
- `interface Ore_Name` — `Name()`.
- `struct Type_dobl<T,T2>` — generic-пара (`one`, `two`).
- `abstract class New_ore : Ore_Name` — описание руды: `name`, `fire_toplivo`, словарь свойств `DicDeffult` (`New_Svoystvo`), виртуальные `RandMineTimeSleep()` (0.01–0.15) и `FireToplivo()`.
- `class Flammogidrid : New_ore` — руда «Coal», горючая (`FireToplivo() == true`).
- `struct Len_List_Vec` — `len` + `List<Vector3>`.
- `class ORE_BLOCKS`:
  - `GetOreInMy(go, ore_type)` — руды нужного типа вокруг объекта (через индекс [Config](Config.md), тип `Mine_blick`);
  - `Null` — пустое имя руды `""`;
  - `IfNullOre(st)`.

## Зависимости
[World_commands](World_commands.md) · [Config](Config.md) · [Ore](Ore.md) (SattingsOre).

## Кто использует
[BaseDate](BaseDate.md) (реестр `New_ore`), [Mine_ore](Mine_ore.md), [Conveir](Conveir.md), [Core_res](Core_res.md) (константа `ORE_BLOCKS.Null`).

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
