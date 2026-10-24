# Created_block

**Файл:** `Player/Created_block.cs` · **Исходник:** `Assets\Scripts\Player\Created_block.cs` · **Тип:** `Errors` (RequireComponent → [[Move_person]])

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
[[Config]] · [[World_commands]] · [[Sattings_block_cr]] (Prefab_Go, PlayerBlock) · [[MainSystemTrigers]] · [[Move_person]].

## Кто использует
[[ButtonCreateBlock]] · [[Config]].created_pl.

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
