# 📁 Обзор проекта (Beta_Unity)

> Ваза Obsidian для кода из `Assets\Scripts`. Код не изменялся — это только документация.
> Структурированная копия самого кода: `Ai\Scripts` (байт-в-байт, проверено MD5).

## Дерево структуры Ai\Scripts

```
Ai\Scripts\
├── Core\        — ядро: конфиг, события, базовый код, спавн
│   ├── Config.cs
│   ├── MainSystemTrigers.cs
│   ├── World_commands.cs      ← фундамент всей архитектуры
│   └── Core_Spawn.cs
├── Data\        — данные и ScriptableObject
│   ├── Sattings_block_cr.cs
│   ├── Create_block.cs        (ResursesCraft)
│   └── BaseDate.cs            (реестр руд)
├── Machines\    — транспорт и добыча руды
│   ├── Move_class.cs
│   ├── Conveir.cs
│   ├── Mine_ore.cs
│   └── Core_res.cs
├── Ore\         — руда: компоненты и описания
│   ├── Ore.cs
│   └── ORE_BLOCK.cs
├── Player\      — игрок и постройка
│   ├── Move_person.cs
│   ├── Created_block.cs
│   └── ButtonCreateBlock.cs
├── Gui\         — динамический UI из JSON
│   ├── ManagerGuiCr.cs
│   └── PrefabGui.cs
├── Input\       — ввод и курсор
│   └── ControllerButton.cs
├── Utils\       — переиспользуемые утилиты
│   ├── World_Types.cs         (Dic_Rdic)
│   └── WorldGoDisasamble.cs   (де/сериализация GUI)
├── Editor\      — код редактора Unity
│   └── BigStringLabel.cs
└── Tools\       — не-C# инструменты
    └── t.py
```

## Все скрипты (ссылки на заметки)

| Скрипт | Назначение | Папка |
|---|---|---|
| [Config](Классы/Config.md) | Индекс сцены, API регистрации объектов | Core |
| [MainSystemTrigers](Классы/MainSystemTrigers.md) | Шина событий (триггеров) | Core |
| [World_commands](Классы/World_commands.md) | База: сетка, JsonP, ошибки, абстрактные классы | Core |
| [Core_Spawn](Классы/Core_Spawn.md) | Спавн ядра и игрока, инициализация GUI | Core |
| [Sattings_block_cr](Классы/Sattings_block_cr.md) | ScriptableObject блоков для постройки | Data |
| [Create_block](Классы/Create_block.md) | Структура ResursesCraft (рецепт крафта) | Data |
| [BaseDate](Классы/BaseDate.md) | Реестр руд (BaseDateOre) | Data |
| [Move_class](Классы/Move_class.md) | Корпус машины: точки входа/выхода | Machines |
| [Conveir](Классы/Conveir.md) | Конвейер (очередь из 3 слотов) | Machines |
| [Mine_ore](Классы/Mine_ore.md) | Добытчик руды + топливо | Machines |
| [Core_res](Классы/Core_res.md) | Ядро-склад ресурсов | Machines |
| [Ore](Классы/Ore.md) | Компонент рудного блока | Ore |
| [ORE_BLOCK](Классы/ORE_BLOCK.md) | Описания руд и поиск руд в сцене | Ore |
| [Move_person](Классы/Move_person.md) | Движение и камера игрока | Player |
| [Created_block](Классы/Created_block.md) | Постройка блоков (рейкаст + превью) | Player |
| [ButtonCreateBlock](Классы/ButtonCreateBlock.md) | Кнопка UI → постройка | Player |
| [ManagerGuiCr](Классы/ManagerGuiCr.md) | JSON-менеджер UI | Gui |
| [PrefabGui](Классы/PrefabGui.md) | Шаблоны GUI (заготовка) | Gui |
| [ControllerButton](Классы/ControllerButton.md) | Ввод, Tab, курсор, блокировка клавиш | Input |
| [World_Types](Классы/World_Types.md) | Dic_Rdic — двунаправленный словарь | Utils |
| [WorldGoDisasamble](Классы/WorldGoDisasamble.md) | Blueprint: сериализация GameObject | Utils |
| [BigStringLabel](Классы/BigStringLabel.md) | Drawer для BigStringAttribute | Editor |

См. также: [Архитектура (README)](README.md)

---
↩️ [Содержание](Содержание.md)
