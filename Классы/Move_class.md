# Move_class

**Файл:** `Machines/Move_class.cs` · **Исходник:** `Assets\Scripts\IF_move_functionals\Move_class.cs` · **Тип:** `World_class_move` → [World_commands#World_class_move|базовый класс](World_commands.md)

## Назначение
Физический «корпус» машины: грани, точки входа/выхода, поиск соседей.

## Поля
- `myBox` (Vector3) — размер в клетках.
- `input_ore` / `output_ore` — List\<`Date_two_list`\> (x, y, грань `Napr`).
- `gam_inp` / `gam_out` — найденные соседние машины.
- `MyCoords` — координаты ячеек граней (пересчёт в `Trigers`).

## Логика
- `Awake` — требует компонент `IF_move_functional` (делегирует ему работу с рудой).
- `Trigers(Update_Block)` — `GetSurfaceCoordsBySide` → для каждой точки входа ищет в [Config](Config.md) объекты `Player_Block`, фильтрует по совпадению стороны (`test_napr_get` + `GetSideFacing`).
- `test_napr_get(g, dm)` — смотрит ли сторона объекта `g` на нас (INPUT/OUTPUT).
- `UpTestError` — уникальность точек входа/выхода и отсутствие пересечений (`CoordKey`).

## Зависимости
[World_commands](World_commands.md) · [Config](Config.md) · [MainSystemTrigers](MainSystemTrigers.md).

## Кто использует
[Conveir](Conveir.md), [Mine_ore](Mine_ore.md), [Core_res](Core_res.md) (через RequireComponent) — сам [Ore](Ore.md) находит руду через `World_class_move.get_ore`.

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Move_class" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Move_class" class="alice-style-header">
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
      <span>Move_class.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Move_class : World_class_move
{
    [SerializeField] private Vector3 myBox = Vector3.one;
    [SerializeField] private List&lt;Date_two_list&gt; input_ore = new List&lt;Date_two_list&gt;();
    [SerializeField] private List&lt;Date_two_list&gt; output_ore = new List&lt;Date_two_list&gt;();

    [SerializeField] private List&lt;GameObject&gt; gam_inp = new List&lt;GameObject&gt;();
    [SerializeField] private List&lt;GameObject&gt; gam_out = new List&lt;GameObject&gt;();
    private Dictionary&lt;World_command.Napr, List&lt;List&lt;Vector3&gt;&gt;&gt; MyCoords = new Dictionary&lt;World_command.Napr, List&lt;List&lt;Vector3&gt;&gt;&gt;();
    private IF_move_functional iF_Move_Functional;

    public override Vector3 GetSize()
    {
        return myBox;
    }

    void Awake()
    {
        iF_Move_Functional = gameObject.GetComponent&lt;IF_move_functional&gt;();
        if (iF_Move_Functional == null)
            World_command.Error(gameObject.name, "not exemplar class IF_move_functional on this obgect");
    }

    public override List&lt;Date_two_list&gt; get_napr(Vector3 vec)
    {
        return output_ore;
    }

    protected override bool AwTestError()
    {
        return myBox.x &gt; 0 &amp;&amp; myBox.y &gt; 0 &amp;&amp; myBox.z &gt; 0;
    }

    protected override bool UpTestError()
    {
        var inputSet = new HashSet&lt;CoordKey&gt;();
        foreach (var i in input_ore)
        {
            var key = new CoordKey(i.x, i.y, i.napr);
            if (!inputSet.Add(key))
                return false;
        }

        var outputSet = new HashSet&lt;CoordKey&gt;();
        foreach (var o in output_ore)
        {
            var key = new CoordKey(o.x, o.y, o.napr);
            if (!outputSet.Add(key))
                return false;

            if (inputSet.Contains(key))
                return false;
        }

        return true;
    }

    public override bool test_napr_get(GameObject g, World_command.Date_move dm)
    {
        var nap = World_command.GetSideFacing(gameObject.transform, g.transform.position);
        var dtl = dm == World_command.Date_move.INPUT ? input_ore : output_ore;

        foreach (var v in dtl)
        {
            if (v.napr == nap)
            {
                return true;
            }
        }

        return false;
    }

    private List&lt;GameObject&gt; GetObjectsAtCell(List&lt;GameObject&gt; g, World_command.Date_move dm)
    {
        List&lt;GameObject&gt; gm = new List&lt;GameObject&gt;();
        foreach (GameObject gmo in g)
        {
            if (gmo != null &amp;&amp; gmo != gameObject)
            {
                World_class_move wcm = gmo.GetComponent&lt;World_class_move&gt;();
                if (wcm != null &amp;&amp; wcm.test_napr_get(gameObject, dm))
                    gm.Add(gmo);
            }
        }
        return gm;
    }

    public override void Trigers(MainSystemTrigers.trig tr)
    {
        if (!MainSystemTrigers.TestTrig(tr, MainSystemTrigers.trig.Update_Block))
            return;

        MyCoords = World_command.GetSurfaceCoordsBySide(gameObject, myBox);

        gam_inp.Clear();
        gam_out.Clear();

        foreach (var dtl in input_ore)
        {
            if (!MyCoords.ContainsKey(dtl.napr)) continue;
            if (dtl.y &gt;= MyCoords[dtl.napr].Count || dtl.x &gt;= MyCoords[dtl.napr][dtl.y].Count) continue;

            Vector3 cellPos = MyCoords[dtl.napr][dtl.y][dtl.x];
            List&lt;GameObject&gt; nearby = Config.Get_obg_sceneGo(cellPos, DicVec.Generated.Player_Block);
            if (nearby == null || nearby.Count == 0) { continue; }
            nearby = GetObjectsAtCell(nearby, World_command.Date_move.OUTPUT);
            if (nearby == null || nearby.Count == 0) { continue; }
            gam_inp.AddRange(nearby);
        }

        foreach (var dtl in output_ore)
        {
            if (!MyCoords.ContainsKey(dtl.napr)) continue;
            if (dtl.y &gt;= MyCoords[dtl.napr].Count || dtl.x &gt;= MyCoords[dtl.napr][dtl.y].Count) continue;

            Vector3 cellPos = MyCoords[dtl.napr][dtl.y][dtl.x];
            List&lt;GameObject&gt; nearby = Config.Get_obg_sceneGo(cellPos, DicVec.Generated.Player_Block);
            if (nearby == null || nearby.Count == 0) { continue; }
            nearby = GetObjectsAtCell(nearby, World_command.Date_move.INPUT);
            if (nearby == null || nearby.Count == 0) { continue; }
            gam_out.AddRange(nearby);
        }
    }

    public override string get_ore(GameObject po)
    {
        if (po == null || output_ore.Count == 0)
            return ORE_BLOCKS.Null;

        foreach (var n in output_ore)
        {
            if (!MyCoords.ContainsKey(n.napr)) continue;
            if (n.y &gt;= MyCoords[n.napr].Count || n.x &gt;= MyCoords[n.napr][n.y].Count) continue;

            Vector3 cellPos = MyCoords[n.napr][n.y][n.x];
            if (Vector3.Distance(po.transform.position, cellPos) &lt;= 0.1f &amp;&amp; po.GetComponent&lt;World_class_move&gt;() != null &amp;&amp; gam_out.Contains(po))
            {
                return iF_Move_Functional.move_ore();
            }
        }

        return ORE_BLOCKS.Null;
    }

    void Update()
    {
        iF_Move_Functional.Up_Func_Ore(gam_inp, gam_out);
    }


    void OnDestroy()
    {
        Config.Destroy_obj_size_scene(gameObject, DicVec.Generated.Player_Block);
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
