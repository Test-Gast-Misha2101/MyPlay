# Mine_ore

**Файл:** `Machines/Mine_ore.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Mine_ore.cs` · **Тип:** `IF_move_functional` (RequireComponent → [[Conveir]])

## Назначение
Добытчик руды: добывает рудные блоки рядом с собой в очередь `lore`, принимает топливо.

## Поля
- `toplivo_white_list` — какие руды годятся в топливо (проверка `FireToplivo` в [[BaseDate]]); `toplivo` — принятые.
- `mine_ore` (скорость), `ore_type` (какие руды добывать).
- `max_len_ore`, `max_len_interface` — лимиты очередей; `lore` — добытая руда.
- `gam` — список рудных блоков рядом.

## Логика
- `Trigers(Update_Block)` — обновляет `gam` через `ORE_BLOCKS.GetOreInMy`.
- `Up_Func_Ore` — принимает топливо со случайной соседней машины (`gam_inp`), с проверкой белого списка и `FireToplivo`.
- `corut_cr()` — корутина: с паузами `mine_ore / len_block * gam.Count` кладёт руду в `lore`.
- `move_ore()` — забирает последнюю добытую руду.
- `UpTestError` — все элементы `toplivo_white_list` должны быть валидным топливом.

## Зависимости
[[World_commands]] · [[ORE_BLOCK]] · [[BaseDate]] · [[Move_class]] · [[Conveir]] · [[MainSystemTrigers]].

← [[00 — Обзор проекта]] · [[Архитектура]]

---
↩️ [[Содержание]]
