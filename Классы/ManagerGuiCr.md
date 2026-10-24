# ManagerGuiCr

**Файл:** `Gui/ManagerGuiCr.cs` · **Исходник:** `Assets\Scripts\Gui\ManagerGuiCr.cs` · **Размер:** 22 КБ · **Тип:** обычный класс (не MonoBehaviour)

## Назначение
Динамический менеджер UI: управление иерархией и свойствами компонентов через JSON.

## Структура
- `mgc` — Dictionary\<string, ManagerGuiCr\> (дерево элементов); `Go` — GameObject; `wd` — чертёж ([[WorldGoDisasamble#Blueprint|Blueprint]]).
- `destroyType` — карта строк → типов компонентов (Image, Text, RawImage, Mask, RectMask2D, Button, InputField, Toggle, ToggleGroup, Slider, Scrollbar, Dropdown, ScrollRect) для секции `Destroy`.

## API
| Метод | Назначение |
|---|---|
| `JsonPManagerGuiCr(json)` | команды `add` / `del` / `comp` |
| `Add(go, name, path)` | добавить элемент (рекурсия по пути, инстанс + Disassemble) |
| `Get / TryGet(name, path)` | найти элемент |
| `Save(name, path)` | пересохранить чертёж |
| `Delete(name, path)` | удалить элемент |
| `ManagerComponent(name, path, jsonP, jsonPGoPathLinc)` | применить свойства + линковка объектов |
| `ReGameObject(go)` | пересобрать всё дерево под новым корнем |

## AssambleJsonUiObject — JSON-секции
`Rect` (RectTransform), `Img`, `Text`, `RawImage`, `Mask`, `RectMask2D`, `Button`, `InputField`, `Toggle`, `ToggleGroup`, `Slider`, `Scrollbar`, `Dropdown`, `ScrollRect`, `Destroy`. События — через `JsonP.JsonPActionClass` / `JsonPActionTClass<T>` (onClick, onValueChanged, onEndEdit).

## Зависимости
[[World_commands]] (JsonP, DicConv, Error) · [[WorldGoDisasamble]].

## Кто использует
[[Core_Spawn]] (GuiCrMan) · [[Config]].created_pl (ReGameObject).

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
