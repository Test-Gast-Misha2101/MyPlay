# BigStringLabel

**Файл:** `Editor/BigStringLabel.cs` · **Исходник:** `Assets\Scripts\Editor\BigStringLabel.cs` · **Тип:** Editor-only (UnityEditor)

## Содержимое
`BigStringDrawer : PropertyDrawer` для `BigStringAttribute` (объявлен в [[World_commands]]):
- `OnGUI` — рисует `EditorGUI.TextArea` высотой `maxLines` строк.
- `GetPropertyHeight` — высота = singleLineHeight × maxLines.

## Зависимости
[World_commands](../World_command.md) (BigStringAttribute), UnityEditor.

## Кто использует
[Core_Spawn](../Core_Spawn.md) — поле `stGuiJsonp` (`[BigString(3, 10)]`).

[Обзор проекта](../obz.md)

---
↩️ [Содержание](../Содержание.md)
