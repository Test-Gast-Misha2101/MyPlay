# MainSystemTrigers

**Файл:** `Core/MainSystemTrigers.cs` · **Исходник:** `Assets\Scripts\MainSystemTrigers.cs` · **Тип:** MonoBehaviour

## Назначение
Центральная шина событий. Хранит список всех компонентов `Triger` и рассылает им триггеры.

## Содержимое
- `enum trig { Restart, Update_Block }` — типы событий.
- `ClTr` (static List\<Triger\>) — подписчики; `trigs` — очередь событий.
- `ResetClTr()` — пересобрать подписчиков (`FindObjectsOfType<Triger>`).
- `RegistTrig(trig)` — поставить событие в очередь.
- `TestTrig(trig, trig | HashSet<trig>)` — фильтр: `Restart` срабатывает всегда.
- В `FixedUpdate` события раздаются по одному (LIFO) всем подписчикам.

## Зависимости
[[World_commands]] (`Triger`, `Errors`).

## Кто использует
[[Move_class]] и [[Mine_ore]] (фильтр `Update_Block`), [[Created_block]] (сброс и перезапуск после постройки).

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
