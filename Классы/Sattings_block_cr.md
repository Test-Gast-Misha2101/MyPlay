# Sattings_block_cr

**Файл:** `Data/Sattings_block_cr.cs` · **Исходник:** `Assets\Scripts\Sattings_block_cr.cs`

## Содержимое
- `Sattings_Block_Created_Level` (class, Serializable) — пара: `sbc` (Sattings_block_cr) + `lev` (уровень/индекс).
- `Prefab_Go` (class, Serializable) — полное описание блока: `name`, `ico` (Sprite), `Prefab`, `vecPrSmetheniePaste` (смещение при вставке), `go` (превью-объект), `grup` / `sortGrup`, `resursesCrafts` (List\<ResursesCraft\> из [Create_block](Классы/Create_block.md)).
- `Sattings_block_cr` — **ScriptableObject**, меню создания: `Scripteble_obg/Block/Create/Sattings_create_block`; хранит `List<Prefab_Go> Obj`.
- `PlayerBlock : DicVec.TypeGenerated` — метка `Generated.Player_Block` для индекса [Config](Классы/Config.md).

## Зависимости
[Create_block](Классы/Create_block.md) (ResursesCraft) · [World_commands](Классы/World_commands.md) (DicVec.TypeGenerated).

## Кто использует
[Config](Классы/Config.md) (prefabs_sattings, created_pl) · [Core_Spawn](Классы/Core_Spawn.md) · [Created_block](Классы/Created_block.md) (Prefab_Go) · [ButtonCreateBlock](Классы/ButtonCreateBlock.md)

← [00 — Обзор проекта](00 — Обзор проекта.md)

---
↩️ [Содержание](Содержание.md)
