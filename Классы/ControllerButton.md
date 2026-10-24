# ControllerButton

**Файл:** `Input/ControllerButton.cs` · **Исходник:** `Assets\Scripts\ControllerButton.cs` · **Тип:** MonoBehaviour

## Назначение
Обработка ввода и состояния курсора (показ/скрытие GUI по Tab).

## Содержимое
- `visiable` — видно ли GUI.
- `KeyFunc` — Dictionary<bool, Dictionary<KeyCode, Action>>: раскладка действий для GUI видим/скрыт (в обоих Tab → `FTab`).
- `BlockKeys` (static HashSet) + `BlockKey(KeyCode)` / `UnBlockKey(KeyCode)` — блокировка нажатий; Escape заблокирован всегда.
- `Update` — выполнение действий по нажатой клавише текущего состояния.
- `LateUpdate` — «гашение» заблокированных клавиш (`Input.GetKeyDown` в цикле) и установка `Cursor.lockState` / `Cursor.visible`.

## Зависимости
UnityEngine.Input only.

## Кто использует
Вешается на объект сцене (управление курсором для [Created_block](Created_block.md) и UI).

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
