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
[World_commands](World_command.md) (`Triger`, `Errors`).

## Кто использует
[Move_class](Move_class.md) и [Mine_ore](Mine_ore.md) (фильтр `Update_Block`), [Created_block](Created.md) (сброс и перезапуск после постройки).

[Обзор проекта](../Obz.md) · [Архитектура](../README.md)

---
↩️ [Содержание](../Содержание.md)
