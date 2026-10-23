# BaseDate

**Файл:** `Data/BaseDate.cs` · **Исходник:** `Assets\Scripts\Base\BaseDate.cs`

## Содержимое
`BaseDateOre` (namespace `BaseDate`) — статический реестр руд:
- `Ores` — Dictionary\<string, New_ore\>; на старте зарегистрирована одна: `{"Flammogidrid", new Flammogidrid()}`.
- `ConstantsOres(en)` — есть ли руда с таким ключом.
- `GetListOresName()` — все имена руд.
- `GetObjOre(store_Type)` — описание `New_ore`.
- `CreateNewObjOre(error, ore_Type, new_Ore)` — регистрация новой руды (ошибка при дубле или имени «Null»).

## Зависимости
[[ORE_BLOCK]] (`New_ore`, `Flammogidrid`, `ORE_BLOCKS.Null`).

## Кто использует
[[Core_res]] (заполнение запасов), [[Mine_ore]] (топливо `FireToplivo`).

← [[00 — Обзор проекта]]

---
↩️ [[Содержание]]
