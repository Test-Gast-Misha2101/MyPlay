# Created_block

**Файл:** `Player/Created_block.cs` · **Исходник:** `Assets\Scripts\Player\Created_block.cs` · **Тип:** `Errors` (RequireComponent → [Move_person](Move_person.md))

## Назначение
Постройка блоков игроком: призрак блока, подсветка, создание.

## Поля
- `layer` (LayerMask — куда рейкастить), `conf` (Config), `cam`.
- `Obj` (`DicVec.GamePlayerBuildBlock`: префаб-призрак + настройки + child), `SizeObj`, `quaternion1` (поворот), `_renderChild`, `_go_state`, `_hit_pos`, `smeschenie`, `TypeGenerated` (`PlayerBlock`), `Obj_coninue_create`.

## Методы/логика
- `Rotarions(Quaternion)` — задать поворот (с проверкой диапазона).
- `Create_block_Render(Prefab_Go)` — валидирует префаб (нужен BoxCollider), создаёт призрак.
- `CrBlRenderColor(...)` — подсветка Act/notAct из `conf.GetRenderStateCrBl()`, ленивое пересоздание рендера.
- `Update` — рейкаст из камеры, позиция по сетке (Floor + 0.5 + смещение), ЛКМ → `Set_bl_cr`.
- `Set_bl_cr` — создание блока: проверка лимита (`Config.Test_Cr_Bl`), слой «Collaider», `Config.Add_obg_scene`, `MainSystemTrigers.ResetClTr` + `RegistTrig(Update_Block)`.

## Зависимости
[Config](Config.md) · [World_commands](World_commands.md) · [Sattings_block_cr](Sattings_block_cr.md) (Prefab_Go, PlayerBlock) · [MainSystemTrigers](MainSystemTrigers.md) · [Move_person](Move_person.md).

## Кто использует
[ButtonCreateBlock](ButtonCreateBlock.md) · [Config](Config.md).created_pl.

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
