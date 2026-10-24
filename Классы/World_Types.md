# World_Types

**Файл:** `Utils/World_Types.cs` · **Исходник:** `Assets\Scripts\World_Types.cs`

## Содержимое
`Dic_Rdic<TKey, TValue>` (namespace `World_Types`) — двунаправленный словарь: синхронные `Dictionary<TKey,TValue>` и `Dictionary<TValue,TKey>`.
- `Add/Set` — автоматически чистят обратную пару.
- `Remove` по ключу и по значению, `GetValue` с дефолтом, `TryGetKey/TryGetValue`.
- Индексаторы `this[TKey]` и `this[TValue]` (оба сеттера идут через `Set`).
- Копирующие конструкторы, в т.ч. `Dic_Rdic(Dic_Rdic<TValue,TKey>)` — «инверсия» типов.
- Реализует `IEnumerable` (перечисляет пары основного словаря).

## Зависимости
Нет (чистая generic-утилита).

## Кто использует
В текущем коде прямых использований не найдено — зарезервирована как переиспользуемая структура.

← [Обзор проекта](Obz.md)

---
↩️ [Содержание](Содержание.md)
