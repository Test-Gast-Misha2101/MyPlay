# Ore

**Файл:** `Ore/Ore.cs` · **Исходник:** `Assets\Scripts\Ore\Ore.cs`

## Содержимое
- `SattingsOre : DicVec.TypeGenerated` — метка рудного блока в индексе: `GetTypeGenerated()` → `Generated.Mine_blick`, хранит имя руды.
- `Ore : MonoBehaviour` — компонент рудного блока:
  - `_ore` (string, `[Delayed]`) — имя руды (дефолт `ORE_BLOCKS.Null`), свойство `ore`;
  - `_ore_mine_defect` — дефект добычи, свойство `ore_mine_defect`;
  - `Awake` → `Config.Add_obg_scene(gameObject, new SattingsOre(_ore))`;
  - `OnDestroy` → `Config.Destroy_obj_size_scene(...)`.

## Зависимости
[[World_commands]] (DicVec) · [[Config]] · [[ORE_BLOCK]] (`ORE_BLOCKS.Null`).

## Кто использует
[[Mine_ore]] (получает компонент `Ore` у добытых блоков) · [[ORE_BLOCK]].GetOreInMy.

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
