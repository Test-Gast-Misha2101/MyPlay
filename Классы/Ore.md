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
[World_commands](World_commands.md) (DicVec) · [Config](Config.md) · [ORE_BLOCK](ORE_BLOCK.md) (`ORE_BLOCKS.Null`).

## Кто использует
[Mine_ore](Mine_ore.md) (получает компонент `Ore` у добытых блоков) · [ORE_BLOCK](ORE_BLOCK.md).GetOreInMy.
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Ore" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Ore" class="alice-style-header">
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
      <span>Ore.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SattingsOre : DicVec.TypeGenerated
{
	public SattingsOre(string ore)
	{
		this.ore = ore;
	}
	public DicVec.Generated GetTypeGenerated() { return DicVec.Generated.Mine_blick; }
	public string ore = ORE_BLOCKS.Null;
}

public class Ore : MonoBehaviour
{
	[SerializeField, Delayed] private string _ore = ORE_BLOCKS.Null;
	[SerializeField, Delayed] private int _ore_mine_defect = 0;
	public string ore { get { return _ore; } }
	public int ore_mine_defect { get { return _ore_mine_defect; } }

	void Awake()
	{
		Config.Add_obg_scene(gameObject, new SattingsOre(_ore));
	}

	void OnDestroy()
	{
		Config.Destroy_obj_size_scene(gameObject, DicVec.Generated.Mine_blick);
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
