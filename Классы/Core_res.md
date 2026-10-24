# Core_res

**Файл:** `Machines/Core_res.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Core_res.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Conveir](Conveir.md))

## Назначение
«Ядро» — склад ресурсов и их источник для игрока.

## Поля
- `MainCam` (public set) — камера игрока, назначается из [Config](Config.md).created_pl.
- `dic` — Dictionary\<string, int\>: все руды из [BaseDate](BaseDate.md) со стартовым запасом 0.

## Логика
- `Awake` — заполняет словарь всеми известными рудами.
- `Up_Func_Ore` — принимает руду с соседей (через `World_class_move.get_ore`), увеличивает запас; новые руды дозаполняются.
- `move_ore()` — Null (ядро не отдаёт руду дальше).
- `get_ore_entity(entity, ore, len_ore)` — выдаёт ресурс, если тег `entity == "Player"` и запаса хватает.

## Зависимости
[World_commands](World_commands.md) · [BaseDate](BaseDate.md) · [ORE_BLOCK](ORE_BLOCK.md) · [Move_class](Move_class.md) · [Conveir](Conveir.md).

## Кто использует
[Core_Spawn](Core_Spawn.md) (RequireComponent, передача MainCam), [Config](Config.md).created_pl.
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Core_res" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Core_res" class="alice-style-header">
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
      <span>Core_res.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Conveir))]
public class Core_res : IF_move_functional
{
    public Camera MainCam { get; set; }

    private Dictionary&lt;string, int&gt; dic = new Dictionary&lt;string, int&gt;();

    void Awake()
    {
        foreach (string orel in BaseDate.BaseDateOre.GetListOresName())
        {
            if (orel != ORE_BLOCKS.Null)
                dic.Add(orel, 0);
        }
    }

    public override void Up_Func_Ore(List&lt;GameObject&gt; gam_inp, List&lt;GameObject&gt; gam_out)
    {
        List&lt;string&gt; ls = BaseDate.BaseDateOre.GetListOresName();
        foreach (var s in ls)
        {
            if (!dic.ContainsKey(s))
            {
                dic[s] = 0;
            }
        }

        if (gam_inp.Count &gt; 0)
        {
            foreach (var obj in gam_inp)
            {
                var comps = obj.GetComponents&lt;World_class_move&gt;();
                foreach (var c in comps)
                {
                    if (c != null)
                    {
                        var ore = c.get_ore(gameObject);
                        if (ore != ORE_BLOCKS.Null &amp;&amp; dic.ContainsKey(ore))
                        {
                            dic[ore] += 1;
                            return;
                        }
                    }
                }
            }
        }
    }

    public override string move_ore()
    {
        return ORE_BLOCKS.Null;
    }

    public override string get_ore_entity(GameObject entity, string ore, int len_ore = 1)
    {
        if (entity.tag == "Player" &amp;&amp; dic[ore] - len_ore &gt;= 0)
        {
            dic[ore] -= len_ore;
            return ore;
        }
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
