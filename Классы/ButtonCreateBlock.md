# ButtonCreateBlock

**Файл:** `Player/ButtonCreateBlock.cs` · **Исходник:** `Assets\Scripts\Player\ButtonCreateBlock.cs` · **Тип:** MonoBehaviour

## Назначение
Мостик «UI-кнопка → постройка»: привязывается к кнопке инвентаря (OnClick).

## Поля/методы
- `Player` (Created_block), `sattings` (Prefab_Go).
- `SetParametr(pl, sattings)` — задать ссылки (null → `World_command.Error`).
- `CreateBlock()` — `Player.Create_block_Render(sattings)`.

## Зависимости
[Created_block](Created_block.md) · [Sattings_block_cr](Sattings_block_cr.md) (Prefab_Go) · [World_commands](World_command.md) (Error).

← [Обзор проекта](../obz.md) · [Архитектура](../README.md)

---
↩️ [[Содержание]]
