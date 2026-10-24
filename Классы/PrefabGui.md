# PrefabGui

**Файл:** `Gui/PrefabGui.cs` · **Исходник:** `Assets\Scripts\Gui\PrefabGui.cs`

## Содержимое
Заготовка шаблонов GUI. Статический класс `PrefabGui` с одним свойством:
- `Inventory` → `"{}"` — пустой JSON-шаблон инвентаря для [ManagerGuiCr](ManagerGuiCr.md).JsonPManagerGuiCr.

## Зависимости
Нет.

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-PrefabGui" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-PrefabGui" class="alice-style-header">
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
      <span>PrefabGui.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PrefabGui {
	public static string Inventory { get { return "{}"; } }
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
