# BigStringLabel

**Файл:** `Editor/BigStringLabel.cs` · **Исходник:** `Assets\Scripts\Editor\BigStringLabel.cs` · **Тип:** Editor-only (UnityEditor)

## Содержимое
`BigStringDrawer : PropertyDrawer` для `BigStringAttribute` (объявлен в [World_commands](World_commands.md)):
- `OnGUI` — рисует `EditorGUI.TextArea` высотой `maxLines` строк.
- `GetPropertyHeight` — высота = singleLineHeight × maxLines.

## Зависимости
[World_commands](World_commands.md) (BigStringAttribute), UnityEditor.

## Кто использует
[Core_Spawn](Core_Spawn.md) — поле `stGuiJsonp` (`[BigString(3, 10)]`).

← [00 — Обзор проекта](../00 — Обзор проекта.md)

---
↩️ [Содержание](../Содержание.md)
