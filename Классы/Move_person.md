# Move_person

**Файл:** `Player/Move_person.cs` · **Исходник:** `Assets\Scripts\Player\Move_person.cs` · **Тип:** `Errors`

## Назначение
Движение и обзор игрока.

## Поля
- `speed` (5), `move_x` (6.0 — чувствительность мыши), `cam` (Camera, свойство `MainCam`), `Ui_Items_cr` (RectTransform).
- `coreSp` (свойство), `hor_m` — накопленный поворот.

## Логика
- `AwTestError` — камера не null.
- `Update` — при зафиксированном курсоре: поворот по Mouse X (`Quaternion.Euler(x, hor_m, z)`).
- `FixedUpdate` — то же условие: перемещение WASD (`Translate(vec * speed * 0.03f, Space.Self)`).

## Зависимости
[World_commands](Классы/World_commands.md) (`Errors`).

## Кто использует
[Created_block](Классы/Created_block.md) (RequireComponent, камера), [Config](Классы/Config.md).created_pl.

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
