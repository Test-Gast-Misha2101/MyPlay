# Sattings_block_cr

**Файл:** `Data/Sattings_block_cr.cs` · **Исходник:** `Assets\Scripts\Sattings_block_cr.cs`

## Содержимое
- `Sattings_Block_Created_Level` (class, Serializable) — пара: `sbc` (Sattings_block_cr) + `lev` (уровень/индекс).
- `Prefab_Go` (class, Serializable) — полное описание блока: `name`, `ico` (Sprite), `Prefab`, `vecPrSmetheniePaste` (смещение при вставке), `go` (превью-объект), `grup` / `sortGrup`, `resursesCrafts` (List\<ResursesCraft\> из [Create_block](Create_block.md)).
- `Sattings_block_cr` — **ScriptableObject**, меню создания: `Scripteble_obg/Block/Create/Sattings_create_block`; хранит `List<Prefab_Go> Obj`.
- `PlayerBlock : DicVec.TypeGenerated` — метка `Generated.Player_Block` для индекса [Config](Config.md).

## Зависимости
[Create_block](Create_block.md) (ResursesCraft) · [World_commands](World_commands.md) (DicVec.TypeGenerated).

## Кто использует
[Config](Config.md) (prefabs_sattings, created_pl) · [Core_Spawn](Core_Spawn.md) · [Created_block](Created_block.md) (Prefab_Go) · [ButtonCreateBlock](ButtonCreateBlock.md)

← [00 — Обзор проекта](../00 — Обзор проекта.md)

---
↩️ [Содержание](../Содержание.md)
