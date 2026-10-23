# Core_Spawn

**Файл:** `Core/Core_Spawn.cs` · **Исходник:** `Assets\Scripts\Core\Core_Spawn.cs` · **Тип:** MonoBehaviour (`Errors`, RequireComponent → `Core_res`)

## Назначение
Точка входа игрового процесса: спавн ядра/игрока и инициализация динамического GUI.

## Поля
- `config` (Config), `lprefab_Go` (List\<Sattings_Block_Created_Level\>) — доступные блоки.
- `stGuiJsonp` — JSON-описание UI, отрисовывается через атрибут [[World_commands#BigStringAttribute|BigString]].
- `player`, `core_Res`, `prg` (Prefab_Go), `items` (ManagerGuiCr).

## Логика
- `GuiCrMan(st)` — если строка не валидный JSON, прогоняет её через `items.JsonPManagerGuiCr`.
- `Awake` — собирает `prg` из lprefab_Go (ProcessObjects + selec), чистит пробелы/переносы JSON и инициализирует GUI.
- `Start` / `Update` — `config.created_pl(...)` создаёт игрока (и пересоздаёт, если тот умер).
- `StTestError` — config и core_Res не null.

## Зависимости
[[Config]] · [[World_commands]] · [[Sattings_block_cr]] · [[ManagerGuiCr]] · [[Move_person]] · [[Core_res]]

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
