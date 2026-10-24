# Core_Spawn

**Файл:** `Core/Core_Spawn.cs` · **Исходник:** `Assets\Scripts\Core\Core_Spawn.cs` · **Тип:** MonoBehaviour (`Errors`, RequireComponent → `Core_res`)

## Назначение
Точка входа игрового процесса: спавн ядра/игрока и инициализация динамического GUI.

## Поля
- `config` (Config), `lprefab_Go` (List\<Sattings_Block_Created_Level\>) — доступные блоки.
- `stGuiJsonp` — JSON-описание UI, отрисовывается через атрибут [World_commands#BigStringAttribute|BigString](World_commands.md).
- `player`, `core_Res`, `prg` (Prefab_Go), `items` (ManagerGuiCr).

## Логика
- `GuiCrMan(st)` — если строка не валидный JSON, прогоняет её через `items.JsonPManagerGuiCr`.
- `Awake` — собирает `prg` из lprefab_Go (ProcessObjects + selec), чистит пробелы/переносы JSON и инициализирует GUI.
- `Start` / `Update` — `config.created_pl(...)` создаёт игрока (и пересоздаёт, если тот умер).
- `StTestError` — config и core_Res не null.

## Зависимости
[Config](Config.md) · [World_commands](World_commands.md) · [Sattings_block_cr](Sattings_block_cr.md) · [ManagerGuiCr](ManagerGuiCr.md) · [Move_person](Move_person.md) · [Core_res](Core_res.md)

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
