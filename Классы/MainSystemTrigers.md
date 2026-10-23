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
[World_commands](Классы/World_commands.md) (`Triger`, `Errors`).

## Кто использует
[Move_class](Классы/Move_class.md) и [Mine_ore](Классы/Mine_ore.md) (фильтр `Update_Block`), [Created_block](Классы/Created_block.md) (сброс и перезапуск после постройки).

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
