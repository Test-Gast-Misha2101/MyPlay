# WorldGoDisasamble

**Файл:** `Utils/WorldGoDisasamble.cs` · **Исходник:** `Assets\Scripts\World\WorldGoDisasamble.cs`

## Назначение
«Разбор и сборка» GameObject в чертёж (Blueprint) — используется [[ManagerGuiCr]] для сохранения/восстановления UI.

## Содержимое
- `VarDisasemble` (Attribute) — включать приватное поле в чертёж.
- `FieldEntry` — name / type (AssemblyQualifiedName) / json (значение).
- `ComponentEntry` — typeName + поля.
- `Blueprint` — name, layer, tag, active, флаг `isRectTransform`, позиция/поворот/масштаб, параметры RectTransform (anchors, offsets, pivot, sizeDelta), список компонентов.
- `Disassemble(GameObject)` — рефлексия: все поля (public, `[SerializeField]`, `[VarDisasemble]`), значения через `ToJson` (примитивы/строки — как есть, UnityEngine.Object → `"ref:имя"`, остальное — JsonUtility).
- `Assemble(Blueprint, parent)` — создаёт GameObject, восстанавливает трансформ, компоненты сортируются по приоритету (Canvas 100 → CanvasScaler 90 → GraphicRaycaster 80 → Graphic 70), поля заполняются через `FromJson`.
- `GetFields` — отфильтровывает `[NonSerialized]`.

## Зависимости
[[World_commands]] (`ProcessObjects`), UnityEngine (JsonUtility, UI).

## Кто использует
[[ManagerGuiCr]] (`wd` — сохранённый чертёж, `ReGameObject`, `Add`, `Save`).

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
