# Mine_ore

**Файл:** `Machines/Mine_ore.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Mine_ore.cs` · **Тип:** `IF_move_functional` (RequireComponent → [Conveir](Conveir.md))

## Назначение
Добытчик руды: добывает рудные блоки рядом с собой в очередь `lore`, принимает топливо.

## Поля
- `toplivo_white_list` — какие руды годятся в топливо (проверка `FireToplivo` в [BaseDate](BaseDate.md)); `toplivo` — принятые.
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
[World_commands](World_commands.md) · [ORE_BLOCK](ORE_BLOCK.md) · [BaseDate](BaseDate.md) · [Move_class](Move_class.md) · [Conveir](Conveir.md) · [MainSystemTrigers](MainSystemTrigers.md).
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Mine_ore" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Mine_ore" class="alice-style-header">
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
      <span>Mine_ore.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

[RequireComponent(typeof(Conveir))]
public class Mine_ore : IF_move_functional
{
	[Header("Toplivo")]
	[SerializeField, Delayed] private List&lt;string&gt; toplivo_white_list = new List&lt;string&gt;();
	private List&lt;string&gt; toplivo = new List&lt;string&gt;();
	[Header("Mine_Ore")]
	[SerializeField, Delayed] private float mine_ore = 1;
	[SerializeField, Delayed] private List&lt;string&gt; ore_type;
	[Header("Ore")]
	private int len_block = 1;
	[SerializeField, Delayed] private int max_len_ore = 15;
	[SerializeField, Delayed] private int max_len_interface = 15;
	[SerializeField, Delayed] private List&lt;string&gt; lore = new List&lt;string&gt;();

	private Vector3 myBox = Vector3.one;
	[SerializeField] private List&lt;GameObject&gt; gam = new List&lt;GameObject&gt;();

	private bool Test_toplivo(string ore)
	{
		return !ORE_BLOCKS.IfNullOre(ore) &amp;&amp; BaseDate.BaseDateOre.GetObjOre(ore).FireToplivo();
	}

	protected override bool UpTestError()
	{
		return World_command.ProcessObjects&lt;string, string&gt;(toplivo_white_list, Test_toplivo).Count == toplivo_white_list.Count;
	}

	void Start()
	{
		len_block = Mathf.Max(1, Mathf.FloorToInt(myBox.x * myBox.y * myBox.z));
		StartCoroutine(corut_cr());
	}

	public override void Trigers(MainSystemTrigers.trig tr)
	{
		if (!MainSystemTrigers.TestTrig(tr, MainSystemTrigers.trig.Update_Block))
			return;
		if (ore_type.Count == 0)
			World_command.Error(gameObject.name, "error not var ore_type.Count == 0");
		gam.Clear();
		gam.AddRange(ORE_BLOCKS.GetOreInMy(gameObject, ore_type));
	}

	public override void Up_Func_Ore(List&lt;GameObject&gt; gam_inp, List&lt;GameObject&gt; gam_out)
	{
		if (ore_type.Count == 0)
			World_command.Error(gameObject.name, "error not var ore_type.Count == 0");
		if (gam.Count == 0)
			return;
		if (mine_ore == 0 || len_block == 0)
			World_command.Error(gameObject.name, "error not var mine_ore == 0 || len_block == 0");
		if (lore.Count &gt;= max_len_ore &amp;&amp; lore.Count != 0)
			return;
		if (gam_inp.Count != 0)
		{
			if (toplivo.Count &gt; max_len_interface &amp;&amp; toplivo.Count != 0)
				toplivo.Remove(lore[-1]);
			if (toplivo.Count &gt;= max_len_ore)
				return;
			int idx = UnityEngine.Random.Range(0, gam_inp.Count);
			World_class_move[] conv = gam_inp[idx].GetComponents&lt;World_class_move&gt;();

			if (conv.Length != 0)
			{
				string orbl = conv[UnityEngine.Random.Range(0, conv.Length)].get_ore(gameObject);
				if (!ORE_BLOCKS.IfNullOre(orbl) &amp;&amp; toplivo.Contains(orbl) &amp;&amp; BaseDate.BaseDateOre.GetObjOre(orbl).FireToplivo())
				{
					toplivo.Add(orbl);
				}
			}
		}
	}

	private IEnumerator corut_cr()
	{
		Ore ore;
		while (true)
		{
			yield return new WaitForSeconds(0.01f);
			if (gam.Count == 0 || mine_ore / len_block == 0 || (mine_ore / len_block) * gam.Count == 0) continue;
			for (float i = 1 / ((mine_ore / len_block) * gam.Count); i &gt; 0; i -= 0.01f)
			{
				yield return new WaitForSeconds(0.01f);
			}
			if (lore.Count &lt; max_len_ore)
			{
				if (gam.Count &gt; 0)
				{
					foreach (GameObject g in gam)
					{
						ore = g.GetComponent&lt;Ore&gt;();
						if (ore != null &amp;&amp; BaseDate.BaseDateOre.ConstantsOres(ore.ore))
						{
							lore.Add(ore.ore);
							break;
						}
					}
				}
			}
		}
	}

	public override string move_ore()
	{
		if (lore.Count &gt; 0)
		{
			string ort = lore[lore.Count - 1];
			lore.RemoveAt(lore.Count - 1);
			return ort;
		}
		return ORE_BLOCKS.Null;
	}

	public override string get_ore_entity(GameObject entity, string ore, int len_ore = 1)
	{
		return ORE_BLOCKS.Null;
	}
}</code></pre>
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
