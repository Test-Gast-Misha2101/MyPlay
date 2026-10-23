# Config

**Файл:** `Core/Config.cs` · **Исходник:** `Assets\Scripts\Config.cs` · **Тип:** MonoBehaviour (`Errors`)

## Содержимое
- `State_cr` (struct) — пара объектов-рендеров: `Act` (можно строить) / `notAct` (нельзя).
- `Config` — главный конфиг и владелец статического индекса сцены `obg_scene` (DicVec).

## API (статический)
| Метод | Назначение |
|---|---|
| `Add_obg_scene` | регистрация объекта в индексе (требует BoxCollider) |
| `Test_Cr_Bl` | можно ли построить блок в этой позиции |
| `Get_obg_scene` / `Get_obg_sceneGo` | объекты в ячейке |
| `Get_obg_size_scene` / `GetBlockRadScene` / `Get_Box_obg_scene` | объекты в области |
| `Destroy_obj_scene` / `Destroy_obj_size_scene` / `Destroy_obj_all_pos_scene` / `Destroy_rad_obj_scene` | удаление из индекса |

## Экземплярные поля/методы
`Ico_Defult`, `state_create_block`, `prefabs_sattings` (ScriptableObject-пресеты блоков), `player_prefab`, `created_pl` — создание игрока и пересоздание [ManagerGuiCr](Классы/ManagerGuiCr.md).

## Зависимости
[World_commands](Классы/World_commands.md) (DicVec, ProcessObjects, GetCellCenters, Error), [Sattings_block_cr](Классы/Sattings_block_cr.md) (Prefab_Go, Sattings_Block_Created_Level), [Move_person](Классы/Move_person.md), [Created_block](Классы/Created_block.md), [ManagerGuiCr](Классы/ManagerGuiCr.md).

## Кто использует
[Ore](Классы/Ore.md), [Created_block](Классы/Created_block.md), [Move_class](Классы/Move_class.md), [Core_Spawn](Классы/Core_Spawn.md), [ORE_BLOCK](Классы/ORE_BLOCK.md).

← [00 — Обзор проекта](00 — Обзор проекта.md) · [Архитектура](Архитектура.md)

---
↩️ [Содержание](Содержание.md)
