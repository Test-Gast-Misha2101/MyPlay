# WorldGoDisasamble

**Файл:** `Utils/WorldGoDisasamble.cs` · **Исходник:** `Assets\Scripts\World\WorldGoDisasamble.cs`

## Назначение
«Разбор и сборка» GameObject в чертёж (Blueprint) — используется [ManagerGuiCr](ManagerGuiCr.md) для сохранения/восстановления UI.

## Содержимое
- `VarDisasemble` (Attribute) — включать приватное поле в чертёж.
- `FieldEntry` — name / type (AssemblyQualifiedName) / json (значение).
- `ComponentEntry` — typeName + поля.
- `Blueprint` — name, layer, tag, active, флаг `isRectTransform`, позиция/поворот/масштаб, параметры RectTransform (anchors, offsets, pivot, sizeDelta), список компонентов.
- `Disassemble(GameObject)` — рефлексия: все поля (public, `[SerializeField]`, `[VarDisasemble]`), значения через `ToJson` (примитивы/строки — как есть, UnityEngine.Object → `"ref:имя"`, остальное — JsonUtility).
- `Assemble(Blueprint, parent)` — создаёт GameObject, восстанавливает трансформ, компоненты сортируются по приоритету (Canvas 100 → CanvasScaler 90 → GraphicRaycaster 80 → Graphic 70), поля заполняются через `FromJson`.
- `GetFields` — отфильтровывает `[NonSerialized]`.

## Зависимости
[World_commands](World_commands.md) (`ProcessObjects`), UnityEngine (JsonUtility, UI).

## Кто использует
[ManagerGuiCr](ManagerGuiCr.md) (`wd` — сохранённый чертёж, `ReGameObject`, `Add`, `Save`).
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-WorldGoDisasamble" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-WorldGoDisasamble" class="alice-style-header">
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
      <span>WorldGoDisasamble.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using UnityEngine;

public class WorldGoDisasamble
{
    [AttributeUsage(AttributeTargets.Field)]
    public class VarDisasemble : Attribute { }

    [Serializable]
    public class FieldEntry
    {
        public string name;
        public string type;
        public string json;
    }

    [Serializable]
    public class ComponentEntry
    {
        public string typeName;
        public List&lt;FieldEntry&gt; fields = new List&lt;FieldEntry&gt;();
    }

    [Serializable]
    public class Blueprint
    {
        public string name;
        public int layer;
        public string tag;
        public bool active;
        public bool isRectTransform;
        public Vector3 pos;
        public Quaternion rot;
        public Vector3 scale;
        public Vector2 anchorMin;
        public Vector2 anchorMax;
        public Vector2 offsetMin;
        public Vector2 offsetMax;
        public Vector2 pivot;
        public Vector2 sizeDelta;
        public List&lt;ComponentEntry&gt; components = new List&lt;ComponentEntry&gt;();
    }

    public static Blueprint Disassemble(GameObject go)
    {
        var bp = new Blueprint
        {
            name = go.name,
            layer = go.layer,
            tag = go.tag,
            active = go.activeSelf
        };

        var rt = go.transform as RectTransform;
        if (rt != null)
        {
            bp.isRectTransform = true;
            bp.pos = rt.localPosition;
            bp.rot = rt.localRotation;
            bp.scale = rt.localScale;
            bp.anchorMin = rt.anchorMin;
            bp.anchorMax = rt.anchorMax;
            bp.offsetMin = rt.offsetMin;
            bp.offsetMax = rt.offsetMax;
            bp.pivot = rt.pivot;
            bp.sizeDelta = rt.sizeDelta;
        }
        else
        {
            bp.isRectTransform = false;
            bp.pos = go.transform.localPosition;
            bp.rot = go.transform.localRotation;
            bp.scale = go.transform.localScale;
        }

        foreach (var comp in go.GetComponents&lt;Component&gt;())
        {
            if (comp is Transform) continue;
            if (comp is CanvasRenderer) continue;

            var t = comp.GetType();
            var entry = new ComponentEntry { typeName = t.AssemblyQualifiedName };

            foreach (var f in GetFields(t))
                entry.fields.Add(new FieldEntry
                {
                    name = f.Name,
                    type = f.FieldType.AssemblyQualifiedName,
                    json = ToJson(f.GetValue(comp), f.FieldType)
                });

            bp.components.Add(entry);
        }

        return bp;
    }

    public static GameObject Assemble(Blueprint bp, Transform parent = null)
    {
        var go = new GameObject(bp.name);
        go.layer = bp.layer;
        go.tag = bp.tag;
        go.SetActive(bp.active);

        if(parent != null)
		{
            go.transform.SetParent(parent, false);
		}

        if (bp.isRectTransform)
        {
            var rt = go.AddComponent&lt;RectTransform&gt;();
            rt.localPosition = bp.pos;
            rt.localRotation = bp.rot;
            rt.localScale = bp.scale;
            rt.anchorMin = bp.anchorMin;
            rt.anchorMax = bp.anchorMax;
            rt.offsetMin = bp.offsetMin;
            rt.offsetMax = bp.offsetMax;
            rt.pivot = bp.pivot;
            rt.sizeDelta = bp.sizeDelta;
        }
        else
        {
            go.transform.localPosition = bp.pos;
            go.transform.localRotation = bp.rot;
            go.transform.localScale = bp.scale;
        }

        var ordered = World_command.ProcessObjects&lt;ComponentEntry, ComponentEntry&gt;(
            bp.components,
            null,
            null
        );
        ordered.Sort((a, b) =&gt;
            ComponentPriority(Type.GetType(b.typeName))
            .CompareTo(ComponentPriority(Type.GetType(a.typeName))));

        foreach (var ce in ordered)
        {
            var t = Type.GetType(ce.typeName);
            if (t == null || t == typeof(CanvasRenderer)) continue;

            var comp = go.GetComponent(t);
            if (comp == null) comp = go.AddComponent(t);

            foreach (var fe in ce.fields)
            {
                var fields = GetFields(t);
                FieldInfo found = null;
                foreach (var f in fields)
                {
                    if (f.Name == fe.name) { found = f; break; }
                }
                if (found == null) continue;

                var ft = Type.GetType(fe.type);
                if (ft == null) continue;
                found.SetValue(comp, FromJson(fe.json, ft));
            }
        }

        return go;
    }

    private static int ComponentPriority(Type t)
    {
        if (t == null) return 0;
        if (t == typeof(Canvas)) return 100;
        if (t == typeof(UnityEngine.UI.CanvasScaler)) return 90;
        if (t == typeof(UnityEngine.UI.GraphicRaycaster)) return 80;
        if (typeof(UnityEngine.UI.Graphic).IsAssignableFrom(t)) return 70;
        return 0;
    }

    private static IEnumerable&lt;FieldInfo&gt; GetFields(Type t)
    {
        var pub = World_command.ProcessObjects&lt;FieldInfo, FieldInfo&gt;(
            new List&lt;FieldInfo&gt;(
                t.GetFields(BindingFlags.Public | BindingFlags.Instance)),
            f =&gt; !Attribute.IsDefined(f, typeof(NonSerializedAttribute)),
            null
        );

        var privSerialize = World_command.ProcessObjects&lt;FieldInfo, FieldInfo&gt;(
            new List&lt;FieldInfo&gt;(
                t.GetFields(BindingFlags.NonPublic | BindingFlags.Instance)),
            f =&gt; Attribute.IsDefined(f, typeof(SerializeField)),
            null
        );

        var privBlueprint = World_command.ProcessObjects&lt;FieldInfo, FieldInfo&gt;(
            new List&lt;FieldInfo&gt;(
                t.GetFields(BindingFlags.NonPublic | BindingFlags.Instance)),
            f =&gt; Attribute.IsDefined(f, typeof(VarDisasemble)),
            null
        );

        var result = new List&lt;FieldInfo&gt;(pub.Count + privSerialize.Count + privBlueprint.Count);
        result.AddRange(pub);
        result.AddRange(privSerialize);
        result.AddRange(privBlueprint);
        return result;
    }

    private static string ToJson(object val, Type t)
    {
        if (val == null) return "null";
        if (t == typeof(string)) return (string)val;
        if (t == typeof(int) || t == typeof(float) || t == typeof(bool)
            || t == typeof(double) || t == typeof(long))
            return val.ToString();
        if (t.IsEnum) return val.ToString();
        if (typeof(UnityEngine.Object).IsAssignableFrom(t))
        {
            var uo = (UnityEngine.Object)val;
            return "ref:" + (uo != null ? uo.name : "null");
        }
        try { return JsonUtility.ToJson(val); }
        catch { return "null"; }
    }

    private static object FromJson(string json, Type t)
    {
        if (json == "null") return null;
        if (t == typeof(string)) return json;
        if (t == typeof(int)) return int.Parse(json);
        if (t == typeof(float)) return float.Parse(json);
        if (t == typeof(bool)) return bool.Parse(json);
        if (t == typeof(double)) return double.Parse(json);
        if (t == typeof(long)) return long.Parse(json);
        if (t.IsEnum) return Enum.Parse(t, json);
        if (typeof(UnityEngine.Object).IsAssignableFrom(t)) return null;
        try { return JsonUtility.FromJson(json, t); }
        catch { return null; }
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
