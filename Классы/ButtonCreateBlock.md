# ButtonCreateBlock

**Файл:** `Player/ButtonCreateBlock.cs` · **Исходник:** `Assets\Scripts\Player\ButtonCreateBlock.cs` · **Тип:** MonoBehaviour

## Назначение
Мостик «UI-кнопка → постройка»: привязывается к кнопке инвентаря (OnClick).

## Поля/методы
- `Player` (Created_block), `sattings` (Prefab_Go).
- `SetParametr(pl, sattings)` — задать ссылки (null → `World_command.Error`).
- `CreateBlock()` — `Player.Create_block_Render(sattings)`.

## Зависимости
[Created_block](Классы/Created_block.md) · [Sattings_block_cr](Классы/Sattings_block_cr.md) (Prefab_Go) · [World_commands](Классы/World_commands.md) (Error).

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
