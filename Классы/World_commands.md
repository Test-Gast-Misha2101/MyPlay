# World_commands

**Файл:** `Core/World_commands.cs` · **Исходник:** `Assets\Scripts\World\World_commands.cs` · **Размер:** 32 КБ — фундамент всей архитектуры

> Файл лежал в папке `World`, но не содержит логики «мира»: это базовые классы, сетка, JSON и утилиты.

## Содержимое (по классам)

### BigStringAttribute
Атрибут `PropertyAttribute` — многострочное поле в инспекторе (отрисовывается в [[BigStringLabel]]).

### Vector3Int (struct)
Целочисленная координата сетки. Конструкторы флоорают и смещают на +1/-0.5; свойства `x/y/z` возвращают «флоат-центры» клеток. Поддерживает `+`, `Equals`, `GetHashCode` (hash-множители 73856093/19349663/83492791), `ToVector3`.

### DicVec
Пространственный индекс по клеткам `Dictionary<Generated, Dictionary<Vector3Int, List<GameInfo>>>`.
- `interface TypeGenerated` + `enum Generated { Player_Block, Mine_blick }`
- `struct GameInfo { GameObject go; TypeGenerated }`, `struct GamePlayerBuildBlock`
- `TestCreateBlock`, `Add`, `Remove`, `RemoveInBox`, `GetInBox`, `GetInBoxWithSize`, `GetAllInCell`, `GetAllInCellGo`

### Утилиты
- `TypeStConv` — Type ↔ AssemblyQualifiedName.
- `Str` — подсчёт символов, вырезка по скобкам/символам (`StDelBlock`, `StObrez`, `StObrezIndexOfMin/Max` и т.д.).
- `DicConv` — `KeyValuePairCl<T,T2>` (serializable пара), `DicToList` / `ListToDic`.

### JsonP
Собственный типизированный JSON-контейнер поверх словаря `KVP {type, value}`:
- конструкторы от string/Type/JsonP/словаря; ручной парсер `ToJson(string)` и сборщик `JsonToSt`.
- `Add/Reduct/Get/TryGet/TryGetValue` + версии `…Path` с путями через `/`.
- вложенные объекты — рекурсивный `JsonP`; события — интерфейсы `JsonPActionClass`, `JsonPActionTClass<T>`.
- `StToJson` / `JsonPToSt` — перенос через JsonUtility; `IsValidJson`, `GetCopyDicJsonP`.

### World_command
- `enum Date_move { INPUT, OUTPUT }`, `enum Napr { BACK, FRONT, TOP, BOTTOM, LEFT, RIGHT }`
- `Error(name, err)` — LogError + throw.
- `ListNotDoble`, `ProcessObjects<TSource,TResult>` (filter/selector-утилита).
- `GetSideFacing(Transform, Vector3)` — какая грань объекта смотрит на точку.
- `GetCellCenters(GameObject)` — центры клеток BoxCollider.
- `GetSurfaceCoordsBySide(obj, size)` — координаты ячеек всех 6 граней.

### Базовые классы
- `Error_duble_obg : MonoBehaviour` — защита от дублей компонентов одной группы.
- `Errors : Error_duble_obg` — проверки `AwTestError`/`StTestError`/`UpTestError`.
- `Triger : Errors` — подписчик событий ([[MainSystemTrigers]]).
- `World_class_block_world : Triger` — `Date_two_list`, `CoordKey`.
- `World_class_move : World_class_block_world` — абстракция машины-перевозчика.
- `IF_move_functional : Triger` — абстракция логики машины.

## Зависимости
Только UnityEngine/JsonUtility.

## Кто использует
Почти весь проект: [[Config]], [[Ore]], [[ORE_BLOCK]], [[Move_class]], [[Conveir]], [[Mine_ore]], [[Core_res]], [[Created_block]], [[Core_Spawn]], [[ManagerGuiCr]], [[WorldGoDisasamble]], [[ButtonCreateBlock]], [[Sattings_block_cr]] (косвенно).

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
