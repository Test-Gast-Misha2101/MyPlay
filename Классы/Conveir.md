# Conveir

**Файл:** `Machines/Conveir.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Conveir.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Move_class](Move_class.md))

## Назначение
Конвейер — транспорт руды. Очередь из трёх слотов.

## Поля
`res1`, `res2`, `res3` (string) — слоты; по умолчанию `ORE_BLOCKS.Null`.

## Логика
- `Up_Func_Ore(gam_inp, gam_out)` — проталкивает руду вниз по цепочке (res1→res2→res3); если res1 пуст, забирает руду у соседней машины через `World_class_move.get_ore(gameObject)`.
- `move_ore()` — отдаёт руду из res3 и очищает слот.
- `get_ore_entity(...)` — заглушка (Null).

## Зависимости
[World_commands](World_commands.md) (`IF_move_functional`) · [Move_class](Move_class.md) · [ORE_BLOCK](ORE_BLOCK.md).

## Кто использует
[Mine_ore](Mine_ore.md) и [Core_res](Core_res.md) требуют его через RequireComponent; цепочка: Mine_ore → Conveir → Core_res.
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Conveir" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Conveir" class="alice-style-header">
    <div class="alice-style-left">
      <!-- Кнопка копирования с остановкой всплытия, чтобы не триггерить чекбокс -->
      <button class="alice-copy-btn" type="button" onclick="event.preventDefault(); aliceCopy(this)" title="Скопировать код">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://w3.org">
          <rect x="9" y="9" width="13" height="13" rx="2" stroke="currentColor" stroke-width="1.6"/>
          <path d="M5 15H4C2.89543 15 2 14.1046 2 13V4C2 2.89543 2.89543 2 4 2H13C14.1046 2 15 2.89543 15 4V5" stroke="currentColor" stroke-width="1.6"/>
        </svg>
      </button>
      <span class="alice-style-lang">C#</span>
    </div>
    <div class="alice-style-title">
      <span class="alice-style-dot"></span>
      <span>Conveir.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Move_class))]
public class Conveir : IF_move_functional
{
    [SerializeField, Delayed] private string res1 = ORE_BLOCKS.Null;
    [SerializeField, Delayed] private string res2 = ORE_BLOCKS.Null;
    [SerializeField, Delayed] private string res3 = ORE_BLOCKS.Null;

    public override void Up_Func_Ore(List&lt;GameObject&gt; gam_inp, List&lt;GameObject&gt; gam_out)
    {
        if (res1 != ORE_BLOCKS.Null)
        {
            if (res2 == ORE_BLOCKS.Null)
            {
                res2 = res1;
                res1 = ORE_BLOCKS.Null;
            }
        }

        if (res2 != ORE_BLOCKS.Null)
        {
            if (res3 == ORE_BLOCKS.Null)
            {
                res3 = res2;
                res2 = ORE_BLOCKS.Null;
            }
        }

        if (res1 == ORE_BLOCKS.Null &amp;&amp; gam_inp.Count &gt; 0)
        {
            foreach (var obj in gam_inp)
            {
                if (obj != null)
                {
                    var comps = obj.GetComponents&lt;World_class_move&gt;();
                    foreach (var c in comps)
                    {
                        if (c != null &amp;&amp; res1 == ORE_BLOCKS.Null)
                        {
                            var ore = c.get_ore(gameObject);
                            if (ore != ORE_BLOCKS.Null)
                            {
                                res1 = ore;
                                return;
                            }
                        }
                    }
                }
            }
        }
    }

    public override string move_ore()
    {
        var r = res3;
        res3 = ORE_BLOCKS.Null;
        return r;
    }

    public override string get_ore_entity(GameObject entity, string ore, int len_ore = 1)
    {
        return ORE_BLOCKS.Null;
    }
}
</code></pre>
  </div>
</div>

<style>
/* Скрываем чекбокс */
.alice-toggle-input {
  display: none;
}

.alice-style {
  border-radius: 12px;
  border: 1px solid #2f2f2f;
  background: #000000;
  overflow: hidden;
  margin: 16px 0;
  font-family: JetBrains Mono, Consolas, monospace;
}

.alice-style-header {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 7px 14px;
  background: linear-gradient(180deg, #2a2a2a 0%, #1f1f1f 100%);
  border-bottom: 1px solid #2f2f2f;
  cursor: pointer;
  user-select: none;
}

.alice-style-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.alice-copy-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: none;
  background: transparent;
  color: #ffffff;
  cursor: pointer;
  position: relative;
  z-index: 10;
}
.alice-copy-btn:hover { background: #2f2f2f; }
.alice-copy-btn.copied { color: #22c55e; }

.alice-style-lang {
  color: #ffffff;
  font-size: 13px;
  font-weight: 500;
}

.alice-style-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #ffffff;
  font-size: 13px;
}

.alice-style-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #7c3fff;
}

.alice-style-right { width: 28px; }

.alice-style-body {
  padding: 16px;
  background: #000000;
  display: none; /* По умолчанию скрыто, если чекбокс не активен */
}

.alice-style-body pre {
  margin: 0;
  overflow-x: auto;
}

/* СТИЛЬ ТЕКСТА КОДА: Строго белый цвет для тега code и всех его потомков (важно для обхода плагинов подсветки) */
.alice-style-body code,
.alice-style-body code * {
  display: block;
  line-height: 22px;
  font-size: 13px;
  color: #ffffff !important; 
}

/* Если чекбокс отмечен (checked), показываем тело с кодом */
.alice-toggle-input:checked ~ .alice-style-body {
  display: block;
}

/* Меняем рамку снизу у шапки, когда блок свернут */
.alice-toggle-input:not(:checked) ~ .alice-style-header {
  border-bottom: none;
}
</style>

<script>
function aliceCopy(btn) {
  const code = btn.closest('.alice-style').querySelector('code').innerText;
  navigator.clipboard.writeText(code).then(() => {
    btn.classList.add('copied');
    setTimeout(() => btn.classList.remove('copied'), 1000);
  });
}
</script>
=======

← [00 — Обзор проекта](../00 — Обзор проекта.md) · [Архитектура (README)](../README.md)

---
↩️ [Содержание](../Содержание.md)
>>>>>>> 58b679668214ac286933ee3ea99f70925b3e574d
