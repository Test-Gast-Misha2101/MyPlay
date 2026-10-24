# World_commands

**Файл:** `Core/World_commands.cs` · **Исходник:** `Assets\Scripts\World\World_commands.cs` · **Размер:** 32 КБ — фундамент всей архитектуры

> Файл лежал в папке `World`, но не содержит логики «мира»: это базовые классы, сетка, JSON и утилиты.

## Содержимое (по классам)

### BigStringAttribute
Атрибут `PropertyAttribute` — многострочное поле в инспекторе (отрисовывается в [BigStringLabel](BigStringLabel.md)).

### Vector3Int (struct)
Целочисленная координата сетки. Конструкторы флоорают и смещают на +1/-0.5; свойства `x/y/z` возвращают «флоат-центры» клеток. Поддерживает `+`, `Equals`, `GetHashCode` (hash-множители 73856093/19349663/83492791), `ToVector3`.

### DicVec
Пространственный индекс по клеткам `Dictionary<Generated, Dictionary<Vector3Int, List<GameInfo>>>`.
- `interface TypeGenerated` + `enum Generated { Player_Block, Mine_blick }`
- `struct GameInfo { GameObject go; TypeGenerated }`, `struct GamePlayerBuildBlock`
- `TestCreateBlock`, `Add`, `Remove`, `RemoveInBox`, `GetInBox`, `GetInBoxWithSize`, `GetAllInCell`, `GetAllInCellGo`

### Утилиты
- `TypeStConv` — Type ↔ AssemblyQualifiedName.
- `Str` — подсчёт символов, вырезка по скобкам/символам (`StDelBlock`, `StObrez`, `StObrezIndexOfMin/Max` и т.д.).
- `DicConv` — `KeyValuePairCl<T,T2>` (serializable пара), `DicToList` / `ListToDic`.

### JsonP
Собственный типизированный JSON-контейнер поверх словаря `KVP {type, value}`:
- конструкторы от string/Type/JsonP/словаря; ручной парсер `ToJson(string)` и сборщик `JsonToSt`.
- `Add/Reduct/Get/TryGet/TryGetValue` + версии `…Path` с путями через `/`.
- вложенные объекты — рекурсивный `JsonP`; события — интерфейсы `JsonPActionClass`, `JsonPActionTClass<T>`.
- `StToJson` / `JsonPToSt` — перенос через JsonUtility; `IsValidJson`, `GetCopyDicJsonP`.

### World_command
- `enum Date_move { INPUT, OUTPUT }`, `enum Napr { BACK, FRONT, TOP, BOTTOM, LEFT, RIGHT }`
- `Error(name, err)` — LogError + throw.
- `ListNotDoble`, `ProcessObjects<TSource,TResult>` (filter/selector-утилита).
- `GetSideFacing(Transform, Vector3)` — какая грань объекта смотрит на точку.
- `GetCellCenters(GameObject)` — центры клеток BoxCollider.
- `GetSurfaceCoordsBySide(obj, size)` — координаты ячеек всех 6 граней.

### Базовые классы
- `Error_duble_obg : MonoBehaviour` — защита от дублей компонентов одной группы.
- `Errors : Error_duble_obg` — проверки `AwTestError`/`StTestError`/`UpTestError`.
- `Triger : Errors` — подписчик событий ([MainSystemTrigers](MainSystemTrigers.md)).
- `World_class_block_world : Triger` — `Date_two_list`, `CoordKey`.
- `World_class_move : World_class_block_world` — абстракция машины-перевозчика.
- `IF_move_functional : Triger` — абстракция логики машины.

## Зависимости
Только UnityEngine/JsonUtility.

## Кто использует
Почти весь проект: [Config](Config.md), [Ore](Ore.md), [ORE_BLOCK](ORE_BLOCK.md), [Move_class](Move_class.md), [Conveir](Conveir.md), [Mine_ore](Mine_ore.md), [Core_res](Core_res.md), [Created_block](Created_block.md), [Core_Spawn](Core_Spawn.md), [ManagerGuiCr](ManagerGuiCr.md), [WorldGoDisasamble](WorldGoDisasamble.md), [ButtonCreateBlock](ButtonCreateBlock.md), [Sattings_block_cr](Sattings_block_cr.md) (косвенно).

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-World_commands" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-World_commands" class="alice-style-header">
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
      <span>World_commands.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections.Generic;
using System;
using UnityEngine;
using System.Collections;

public class BigStringAttribute : PropertyAttribute
{
	public int minLines;
	public int maxLines;

	public BigStringAttribute(int minLines = 3, int maxLines = 10)
	{
		this.minLines = minLines;
		this.maxLines = maxLines;
	}
}

public struct Vector3Int
{
	private int xi, yi, zi;
	public int xInt { get { return xi; } }
	public int yInt { get { return yi; } }
	public int zInt { get { return zi; } }
	public float x { get { return xi - 0.5f; } }
	public float y { get { return yi; } }
	public float z { get { return zi - 0.5f; } }

	public Vector3Int(float x, float y, float z) { this.xi = (int)(Mathf.Floor(x) + 1); this.yi = (int)(Mathf.Floor(y)); this.zi = (int)(Mathf.Floor(z) + 1); }
	public Vector3Int(Vector3 vec) { this.xi = (int)(Mathf.Floor(vec.x) + 1); this.yi = (int)(Mathf.Floor(vec.y)); this.zi = (int)(Mathf.Floor(vec.z) + 1); }

	public static Vector3Int operator +(Vector3Int a, Vector3Int b) { return new Vector3Int(a.xInt + b.xInt, a.yInt + b.yInt, a.zInt + b.zInt); }

	public override bool Equals(object obj)
	{
		if (obj == null)
			return false;

		if (!(obj is Vector3Int))
			return false;

		Vector3Int v = (Vector3Int)obj;
		return xi == v.xInt &amp;&amp; yi == v.yInt &amp;&amp; zi == v.zInt;
	}

	public override int GetHashCode()
	{
		unchecked
		{
			int hx = xi;
			int hy = yi;
			int hz = zi;
			return hx * 73856093 ^ hy * 19349663 ^ hz * 83492791;
		}
	}

	public override string ToString()
	{
		return "(" + x.ToString() + ", " + y.ToString() + ", " + z.ToString() + ")";
	}

	public Vector3 ToVector3()
	{
		return new Vector3(x, y, z);
	}
}

public class DicVec
{
	private readonly float cellSize;
	private readonly Vector3 gridOrigin = new Vector3(0.5f, 0.5f, 0.5f);

	public interface TypeGenerated { DicVec.Generated GetTypeGenerated(); }
	public enum Generated
	{
		Player_Block,
		Mine_blick
	}

	[System.Serializable]
	public struct GamePlayerBuildBlock
	{
		public GameObject go;
		public Prefab_Go sattings;
		public GameObject child;
		public GamePlayerBuildBlock(GameObject go, Prefab_Go sattings, GameObject child)
		{
			this.go = go;
			this.sattings = sattings;
			this.child = child;
		}
	}

	[System.Serializable]
	public struct GameInfo
	{
		public GameObject go;
		public TypeGenerated typeGenerated;
		public GameInfo(GameObject go, TypeGenerated typeGenerated)
		{
			this.go = go;
			this.typeGenerated = typeGenerated;
		}
	}

	private Dictionary&lt;Generated, Dictionary&lt;Vector3Int, List&lt;GameInfo&gt;&gt;&gt; cells = new Dictionary&lt;Generated, Dictionary&lt;Vector3Int, List&lt;GameInfo&gt;&gt;&gt;();

	private List&lt;GameInfo&gt; reuseList = new List&lt;GameInfo&gt;();

	public DicVec(float cellSize = 1f)
	{
		this.cellSize = cellSize;
	}

	private Vector3Int GetCell(Vector3 pos)
	{
		return new Vector3Int(
			(pos.x - gridOrigin.x) / cellSize,
			(pos.y - gridOrigin.y) / cellSize,
			(pos.z - gridOrigin.z) / cellSize
		);
	}

	private Dictionary&lt;Vector3Int, List&lt;GameInfo&gt;&gt; nu;

	private void gen_test(Generated generated)
	{
		if (!cells.TryGetValue(generated, out nu))
		{
			cells.Add(generated, new Dictionary&lt;Vector3Int, List&lt;GameInfo&gt;&gt;());
		}
	}

	public bool TestCreateBlock(Vector3 vec, TypeGenerated sattings)
	{
		var cell = GetCell(vec);
		List&lt;GameInfo&gt; list;

		if (vec == null || sattings == null)
		{
			World_command.Error("TestCrBl", "not date");
			return false;
		}
		Generated generated = sattings.GetTypeGenerated();
		gen_test(generated);
		if (cells[generated].TryGetValue(cell, out list))
		{
			if (list.Count == 0) return true;
		}
		else
		{
			return true;
		}
		return false;
	}

	public void Add(GameObject go, Vector3 vec, TypeGenerated sattings)
	{
		var cell = GetCell(vec);
		List&lt;GameInfo&gt; list;

		if (vec == null || sattings == null)
		{
			World_command.Error("TestCrBl", "not date");
			return;
		}
		Generated generated = sattings.GetTypeGenerated();
		gen_test(generated);

		if (!cells[generated].TryGetValue(cell, out list))
		{
			list = new List&lt;GameInfo&gt;();
			cells[generated][cell] = list;
		}
		cells[generated][cell].Add(new GameInfo(go, sattings));
	}

	private GameObject g(GameInfo gi)
	{
		return gi.go;
	}

	public void Remove(GameObject obj, Vector3 vec, Generated generated)
	{
		if (obj == null) return;
		var cell = GetCell(vec);
		gen_test(generated);
		if (cells[generated] == null || cells[generated].Count == 0 || !cells[generated].ContainsKey(cell)) return;

		for (int i = cells[generated][cell].Count - 1; i &gt;= 0; i--)
		{
			if (cells[generated][cell][i].go == obj)
			{
				cells[generated][cell].RemoveAt(i);
			}
		}
	}

	public void RemoveInBox(Vector3 center, float halfSize, Generated generated)
	{
		var centerCell = GetCell(center);
		float cellRadius = halfSize / cellSize + 1;
		List&lt;GameInfo&gt; list;

		gen_test(generated);

		for (float x = -cellRadius; x &lt;= cellRadius; ++x)
			for (float y = -cellRadius; y &lt;= cellRadius; ++y)
				for (float z = -cellRadius; z &lt;= cellRadius; ++z)
				{
					var cell = centerCell + new Vector3Int(x, y, z);

					if (!cells[generated].TryGetValue(cell, out list))
						continue;

					for (int i = list.Count - 1; i &gt;= 0; --i)
					{
						GameObject candidate = list[i].go;
						Vector3 p = candidate.transform.position;

						float dx = Mathf.Abs(p.x - center.x);
						float dy = Mathf.Abs(p.y - center.y);
						float dz = Mathf.Abs(p.z - center.z);

						if (dx &lt;= halfSize &amp;&amp; dy &lt;= halfSize &amp;&amp; dz &lt;= halfSize)
						{
							list.RemoveAt(i);
						}
					}

					if (list.Count == 0)
						cells[generated].Remove(cell);
				}
	}

	public List&lt;GameInfo&gt; GetInBoxWithSize(Vector3 center, Vector3 size, Generated generated)
	{
		gen_test(generated);
		reuseList.Clear();

		float halfX = size.x * 0.5f;
		float halfY = size.y * 0.5f;
		float halfZ = size.z * 0.5f;

		var centerCell = GetCell(center);

		int cellRadiusX = Mathf.CeilToInt(halfX / cellSize) + 1;
		int cellRadiusY = Mathf.CeilToInt(halfY / cellSize) + 1;
		int cellRadiusZ = Mathf.CeilToInt(halfZ / cellSize) + 1;

		List&lt;GameInfo&gt; list;

		for (int x = -cellRadiusX; x &lt;= cellRadiusX; ++x)
			for (int y = -cellRadiusY; y &lt;= cellRadiusY; ++y)
				for (int z = -cellRadiusZ; z &lt;= cellRadiusZ; ++z)
				{
					var cell = centerCell + new Vector3Int(x, y, z);

					if (!cells[generated].TryGetValue(cell, out list))
						continue;

					foreach (var obj in list)
					{
						Vector3 p = obj.go.transform.position;

						float dx = Mathf.Abs(p.x - center.x);
						float dy = Mathf.Abs(p.y - center.y);
						float dz = Mathf.Abs(p.z - center.z);

						if (dx &lt;= halfX &amp;&amp; dy &lt;= halfY &amp;&amp; dz &lt;= halfZ)
							reuseList.Add(obj);
					}
				}

		return reuseList;
	}

	public List&lt;GameInfo&gt; GetAllInCell(Vector3 vec, Generated generated)
	{
		gen_test(generated);
		var cell = GetCell(vec);
		List&lt;GameInfo&gt; list;
		if (cells[generated].TryGetValue(cell, out list))
		{
			return list;
		}
		return new List&lt;GameInfo&gt;();
	}

	private GameObject t(GameInfo gi) { return gi.go; }
	public List&lt;GameObject&gt; GetAllInCellGo(Vector3 vec, Generated generated)
	{
		gen_test(generated);
		var cell = GetCell(vec);
		List&lt;GameInfo&gt; list;
		if (cells[generated].TryGetValue(cell, out list))
		{
			return World_command.ProcessObjects&lt;GameInfo, GameObject&gt;(list, selector: t);
		}
		return new List&lt;GameObject&gt;();
	}

	public List&lt;GameInfo&gt; GetInBox(Vector3 center, float halfSize, Generated generated)
	{
		reuseList.Clear();

		var centerCell = GetCell(center);
		float cellRadius = halfSize / cellSize + 1;
		List&lt;GameInfo&gt; list;

		gen_test(generated);

		for (float x = -cellRadius; x &lt;= cellRadius; ++x)
			for (float y = -cellRadius; y &lt;= cellRadius; ++y)
				for (float z = -cellRadius; z &lt;= cellRadius; ++z)
				{
					var cell = centerCell + new Vector3Int(x, y, z);

					if (!cells[generated].TryGetValue(cell, out list))
						continue;

					foreach (var obj in list)
					{
						Vector3 p = obj.go.transform.position;

						float dx = Mathf.Abs(p.x - center.x);
						float dy = Mathf.Abs(p.y - center.y);
						float dz = Mathf.Abs(p.z - center.z);

						if (dx &lt;= halfSize &amp;&amp; dy &lt;= halfSize &amp;&amp; dz &lt;= halfSize)
							reuseList.Add(obj);
					}
				}

		return reuseList;
	}
}

class TypeStConv
{
	public static string TypeInSt(Type t)
	{
		return t.AssemblyQualifiedName;
	}

	public static Type StInType(string st)
	{
		if (string.IsNullOrEmpty(st)) return null;
		return Type.GetType(st, throwOnError: false, ignoreCase: false);
	}
}

public class Str
{
	public static int StrCount(string st, char simbul)
	{
		int i = 0;
		foreach (char j in st)
		{
			if (j == simbul)
			{
				i++;
			}
		}
		return i;
	}

	public static string StDelBlock(string st, char stc, char fc)
	{
		int start = st.IndexOf(stc);
		int end = st.LastIndexOf(fc);

		if (start &gt;= 0 &amp;&amp; end &gt; start)
		{
			st = st.Substring(start + 1, end - start - 1);
		}
		return st;
	}

	public static string StDelNotInLpRp(string input, char stc, char fc)
	{
		if (string.IsNullOrEmpty(input))
			return "";

		int start = input.IndexOf(stc);
		if (start &lt; 0)
			return "";

		int end = input.IndexOf(fc, start);
		if (end &lt;= start)
			return "";

		return input.Substring(start + 1, end - start - 1);
	}

	public static string StObrez(string st, int min, int max)
	{
		if (string.IsNullOrEmpty(st))
			return st;

		if (min &gt; max)
		{
			int temp = min;
			min = max;
			max = temp;
		}

		if (min &lt; 0) min = 0;
		if (max &gt; st.Length) max = st.Length;

		if (min &gt;= max)
			return st;

		int count = max - min;
		return st.Remove(min, count);
	}

	public static string StObrezIndexOfMin(string st, char ch)
	{
		if (string.IsNullOrEmpty(st))
			return st;

		int idx = st.IndexOf(ch);
		if (idx == -1)
			return st;

		return StObrez(st, 0, idx);
	}
	public static string StObrezIndexOfMinLast(string st, char ch)
	{
		if (string.IsNullOrEmpty(st))
			return st;

		int idx = st.LastIndexOf(ch);
		if (idx == -1)
			return st;

		return StObrez(st, 0, idx);
	}
	public static string StObrezIndexOfMax(string st, char ch)
	{
		if (string.IsNullOrEmpty(st))
			return st;

		int idx = st.IndexOf(ch);
		if (idx == -1)
			return st;

		return st.Remove(idx);
	}
	public static string StObrezIndexOfMaxLast(string st, char ch)
	{
		if (string.IsNullOrEmpty(st))
			return st;

		int idx = st.LastIndexOf(ch);
		if (idx == -1)
			return st;

		return st.Remove(idx);
	}

}

public class DicConv
{
	[Serializable]
	public class KeyValuePairCl&lt;T, T2&gt;
	{
		public T Key;
		public T2 Value;
		public KeyValuePairCl(T t, T2 t2)
		{
			Key = t;
			Value = t2;
		}
	}

	public static List&lt;KeyValuePairCl&lt;T, T2&gt;&gt; DicToList&lt;T, T2&gt;(Dictionary&lt;T, T2&gt; dic)
	{
		if (dic == null) return new List&lt;KeyValuePairCl&lt;T, T2&gt;&gt;();
		List&lt;KeyValuePairCl&lt;T, T2&gt;&gt; t = new List&lt;KeyValuePairCl&lt;T, T2&gt;&gt;();
		foreach(var i in dic)
		{
			t.Add(new KeyValuePairCl&lt;T, T2&gt;(i.Key, i.Value));
		}
		return t;
	}

	public static Dictionary&lt;T, T2&gt; ListToDic&lt;T, T2&gt;(List&lt;KeyValuePairCl&lt;T, T2&gt;&gt; l)
	{
		if (l == null) return null;
		Dictionary&lt;T, T2&gt; dic = new Dictionary&lt;T, T2&gt;();
		for(int i = 0; i &lt; l.Count; i++)
		{
			dic[l[i].Key] = l[i].Value;
		}
		return dic;
	}
}

[Serializable]
public class JsonP
{
	public Dictionary&lt;string, KVP&gt; json { get; private set; }
	public Dictionary&lt;string, KVP&gt;.KeyCollection Keys { get { return json.Keys; } }
	public readonly string t;
	public Type type() { Type ty = Type.GetType(this.t, throwOnError: false, ignoreCase: false); return ty; }

	[Serializable]
	public class KVP
	{
		public string type { get; private set; }
		public string value { get; private set; }

		public KVP(string type, string value)
		{
			if (type == null) World_command.Error("KVP", "type == null");
			this.type = type;
			this.value = value;
		}
	}

	public JsonP() { t = TypeStConv.TypeInSt(typeof(object)); json = new Dictionary&lt;string, KVP&gt;(); }
	public JsonP(Type t) { this.t = TypeStConv.TypeInSt(t); json = new Dictionary&lt;string, KVP&gt;(); }

	public JsonP(string jsons) { t = TypeStConv.TypeInSt(typeof(object)); json = ToJson(jsons); }
	public JsonP(string jsons, Type t) { this.t = TypeStConv.TypeInSt(t); json = ToJson(jsons); }

	public JsonP(JsonP jp) { t = TypeStConv.TypeInSt(typeof(object)); json = jp.json; }
	public JsonP(JsonP jp, Type t) { this.t = TypeStConv.TypeInSt(t); json = jp.json; }

	public JsonP(Dictionary&lt;string, KVP&gt; dic) { t = TypeStConv.TypeInSt(typeof(object)); json = new Dictionary&lt;string, KVP&gt;(dic); }
	public JsonP(Dictionary&lt;string, KVP&gt; dic, Type t) { this.t = TypeStConv.TypeInSt(t); json = new Dictionary&lt;string, KVP&gt;(dic); }

	public interface JsonPActionClass
	{
		void JsonPAction();
	}

	public interface JsonPActionTClass&lt;T&gt;
	{
		void JsonPAction(T val);
	}

	public static JsonP StToJson(string js)
	{
		if (!IsValidJson(js)) return null;
		var j = JsonUtility.FromJson&lt;DicConv.KeyValuePairCl&lt;string, List&lt;DicConv.KeyValuePairCl&lt;string, KVP&gt;&gt;&gt;&gt;(js);
		if (j == null) return null;
		Type ty = Type.GetType(j.Key, throwOnError: false, ignoreCase: false);
		if (ty == null) return null;
		return new JsonP(DicConv.ListToDic&lt;string, KVP&gt;(j.Value), ty);
	}

	public static string JsonPToSt(JsonP jp)
	{
		return JsonUtility.ToJson(new DicConv.KeyValuePairCl&lt;string, List&lt;DicConv.KeyValuePairCl&lt;string, KVP&gt;&gt;&gt;(jp.t, DicConv.DicToList&lt;string, KVP&gt;(jp.json)));
	}

	private T DeSer&lt;T&gt;(T d)
	{
		var ds = d as DicConv.KeyValuePairCl&lt;string, List&lt;DicConv.KeyValuePairCl&lt;string, KVP&gt;&gt;&gt;;

		if (ds != null)
		{
			Type h = Type.GetType(ds.Key, false, false);
			if (h == null) return default(T);

			var jsonP = new JsonP(DicConv.ListToDic&lt;string, KVP&gt;(ds.Value), h);
			return (T)(object)jsonP;
		}

		return d;
	}

	private object Ser(object obj)
	{
		JsonP j = obj as JsonP;
		if (j != null)
		{
			return DicConv.DicToList&lt;string, KVP&gt;(j.json);
		}

		Dictionary&lt;string, KVP&gt; dict = obj as Dictionary&lt;string, KVP&gt;;
		if (dict != null)
		{
			return new DicConv.KeyValuePairCl&lt;string, List&lt;DicConv.KeyValuePairCl&lt;string, KVP&gt;&gt;&gt;
			(
				TypeStConv.TypeInSt(typeof(JsonP)),
				DicConv.DicToList&lt;string, KVP&gt;(dict)
			);
		}

		return obj;
	}

	public void Add&lt;T&gt;(string key, T val) {
		if (json.ContainsKey(key)) World_command.Error("JsonP", "created (value != null) = new value");
		if (type() != typeof(object) &amp;&amp; !type().IsAssignableFrom(val.GetType())) World_command.Error("JsonP", "Add type != Init type");
		string t = val == null ? "" : val.GetType().FullName;
		json.Add(key, new KVP(t, JsonUtility.ToJson(Ser(val))));
	}

	public void AddPath&lt;T&gt;(string path, T value)
	{
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) return;
			jp.AddPath&lt;T&gt;(stp, value);
		}
		else
		{
			Add&lt;T&gt;(stp, value);
		}
	}

	public void Reduct&lt;T&gt;(string key, T val) {
		if (!json.ContainsKey(key)) World_command.Error("JsonP", "not key [\"" + key + "\"] in JsonP");
		if (type() != typeof(object) &amp;&amp; !type().IsAssignableFrom(val.GetType())) World_command.Error("JsonP", "Add type != Init type");
		string t = val == null ? "" : val.GetType().FullName;
		json[key] = new KVP(t, JsonUtility.ToJson(Ser(val)));
	}

	public void ReductPath&lt;T&gt;(string path, T value)
	{
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) return;
			jp.ReductPath&lt;T&gt;(stp, value);
		}
		else
		{
			Reduct&lt;T&gt;(stp, value);
		}
	}

	public T Get&lt;T&gt;(string key)
	{
		KVP st;
		if (!json.TryGetValue(key, out st) || string.IsNullOrEmpty(st.type) || string.IsNullOrEmpty(st.value))
		{
			if (!type().IsAssignableFrom(typeof(T)) &amp;&amp; type() != typeof(object)) World_command.Error("JsonP", "Add type != Init type");
			World_command.Error("JsonP", "not key in json");
			return default(T);
		}
		return DeSer&lt;T&gt;(JsonUtility.FromJson&lt;T&gt;(st.value));
	}

	public T GetPath&lt;T&gt;(string path)
	{
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) { World_command.Error("JsonP", "not key in json"); return default(T); }
			return jp.GetPath&lt;T&gt;(stp);
		}
		else
		{
			return Get&lt;T&gt;(stp);
		}
	}

	public T TryGet&lt;T&gt;(string key, T defult = default(T))
	{
		KVP st;
		if (!type().IsAssignableFrom(typeof(T)) &amp;&amp; type() != typeof(object)) World_command.Error("JsonP", "Add type != Init type");
		if (!json.TryGetValue(key, out st) || string.IsNullOrEmpty(st.type) || string.IsNullOrEmpty(st.value))
		{
			return defult;
		}
		return DeSer&lt;T&gt;(JsonUtility.FromJson&lt;T&gt;(st.value));
	}

	public T TryGetPath&lt;T&gt;(string path)
	{
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) return default(T);
			return jp.TryGetPath&lt;T&gt;(stp);
		}
		else
		{
			return Get&lt;T&gt;(stp);
		}
	}

	public bool TryGetValue&lt;T&gt;(string key)
	{
		KVP st;
		if (!type().IsAssignableFrom(typeof(T)) &amp;&amp; type() != typeof(object)) World_command.Error("JsonP", "Add type != Init type");
		if (!json.TryGetValue(key, out st) || string.IsNullOrEmpty(st.type) || string.IsNullOrEmpty(st.value))
		{
			return false;
		}
		return true;
	}

	public bool TryGetValue&lt;T&gt;(string key, out T val)
	{
		KVP st;
		if (!type().IsAssignableFrom(typeof(T)) &amp;&amp; type() != typeof(object)) World_command.Error("JsonP", "Add type != Init type");
		if (!json.TryGetValue(key, out st) || string.IsNullOrEmpty(st.type) || string.IsNullOrEmpty(st.value))
		{
			val = default(T);
			return false;
		}
		val = DeSer&lt;T&gt;(JsonUtility.FromJson&lt;T&gt;(st.value));
		return true;
	}

	public bool TryGetValuePath&lt;T&gt;(string path)
	{
		KVP res;
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) return false;
			return jp.TryGetValuePath&lt;T&gt;(stp);
		}
		else
		{
			return json.TryGetValue(st, out res) &amp;&amp; !string.IsNullOrEmpty(res.type) || !string.IsNullOrEmpty(res.value);
		}
	}

	public bool TryGetValuePath&lt;T&gt;(string path, out T val)
	{
		KVP res;
		string st = Str.StObrezIndexOfMin(path, '/');
		string stp = Str.StObrezIndexOfMax(path, '/');
		if (stp.Length != 0 &amp;&amp; path.Contains("/"))
		{
			JsonP jp = TryGet&lt;JsonP&gt;(st);
			if (jp == null) { val = default(T); return false; }
			T vp;
			bool b = jp.TryGetValuePath&lt;T&gt;(stp, out vp);
			val = vp;
			return b;
		}
		else
		{
			bool b = json.TryGetValue(st, out res) &amp;&amp; !string.IsNullOrEmpty(res.type) || !string.IsNullOrEmpty(res.value);
			val = Get&lt;T&gt;(st);
			return b;
		}
	}

	public Dictionary&lt;string, T&gt; GetCopyDicJsonP&lt;T&gt;()
	{
		Dictionary&lt;string, T&gt; dic = new Dictionary&lt;string, T&gt;();
		foreach(var i in Keys)
		{
			T ty = TryGet&lt;T&gt;(i);
			if ((object)ty == (object)default(T)) continue;
			dic.Add(i, ty);
		}
		return dic;
	}

	public override string ToString()
	{
		return JsonToSt(json);
	}

	public static bool IsValidJson(string json)
	{
		if (string.IsNullOrEmpty(json)) return false;

		var dummy = new JsonWrapper();
		try
		{
			JsonUtility.FromJsonOverwrite(json, dummy);
			return true;
		}
		catch
		{
			return false;
		}
	}

	private static string JsonToSt(Dictionary&lt;string, KVP&gt; st)
	{
		if (st == null || st.Count == 0) return "{}";

		var parts = new System.Text.StringBuilder();
		parts.Append("{");

		bool first = true;
		foreach (var kvp in st)
		{
			if (!first) parts.Append(',');
			first = false;

			string k = kvp.Key.Replace("\\", "\\\\").Replace("\"", "\\\"");
			string v = "(" + kvp.Value.type.Replace("\\", "\\\\").Replace("\"", "\\\"") + ")" + kvp.Value.value.Replace("\\", "\\\\").Replace("\"", "\\\"");

			parts.Append(string.Format("\"{0}\":\"{1}\"", k, v));
		}

		parts.Append("}");
		return parts.ToString();
	}

	private static Dictionary&lt;string, KVP&gt; ToJson(string st)
	{
		var res = new Dictionary&lt;string, KVP&gt;();
		if (string.IsNullOrEmpty(st) || st.Trim().Length == 0) return res;

		st = st.Trim();
		if (!st.StartsWith("{") || !st.EndsWith("}")) return res;
		st = st.Substring(1, st.Length - 2).Trim();
		if (st == "") return res;

		int i = 0, start = 0;
		while (i &lt;= st.Length)
		{
			if (i &lt; st.Length &amp;&amp; st[i] == '"')
			{
				i++;
				while (i &lt; st.Length)
				{
					if (st[i] == '\\' &amp;&amp; i + 1 &lt; st.Length) { i += 2; continue; }
					if (st[i] == '"') break;
					i++;
				}
			}
			if (i == st.Length || st[i] == ',')
			{
				string pair = st.Substring(start, i - start).Trim();
				start = i + 1;
				if (pair == "") { i++; continue; }

				int colon = pair.IndexOf(':');
				if (colon &lt;= 0) { i++; continue; }

				string key = pair.Substring(0, colon).Trim();
				if (key.StartsWith("\"") &amp;&amp; key.EndsWith("\""))
					key = key.Substring(1, key.Length - 2);

				string val = pair.Substring(colon + 1).Trim();
				if (val.StartsWith("\"") &amp;&amp; val.EndsWith("\""))
					val = val.Substring(1, val.Length - 2);

				key = key.Replace("\\\"", "\"").Replace("\\\\", "\\");
				val = val.Replace("\\\"", "\"").Replace("\\\\", "\\");
				if (Str.StrCount(val, '(') != 1 || Str.StrCount(val, ')') != 1) return new Dictionary&lt;string, KVP&gt;();
				res[key] = new KVP(Str.StDelNotInLpRp(val, '(', ')'), Str.StDelBlock(val, '(', ')'));
			}
			i++;
		}
		return res;
	}

	[System.Serializable]
	private class JsonWrapper
	{
		public Dictionary&lt;string, string&gt; Data;
	}
}

public class World_command
{
	public enum Date_move
	{
		INPUT,
		OUTPUT
	}

	public enum Napr
	{
		BACK,
		FRONT,
		TOP,
		BOTTOM,
		LEFT,
		RIGHT
	}

	public static List&lt;T&gt; ListNotDoble&lt;T&gt;(List&lt;T&gt; lst)
	{
		return new List&lt;T&gt;(new HashSet&lt;T&gt;(lst));
	}

	public static List&lt;TResult&gt; ProcessObjects&lt;TSource, TResult&gt;(
		List&lt;TSource&gt; source,
		Func&lt;TSource, bool&gt; filter = null,
		Func&lt;TSource, TResult&gt; selector = null
	)
	{

		if (source == null)
			throw new ArgumentNullException("source");

		if (filter == null &amp;&amp; selector == null)
			return new List&lt;TResult&gt;();

		var result = new List&lt;TResult&gt;(source.Count);

		foreach (var item in source)
		{
			if (filter != null &amp;&amp; !filter(item))
				continue;

			TResult value;

			if (selector != null)
			{
				value = selector(item);
			}
			else
			{
				if (item is TResult)
				{
					value = (TResult)(object)item;
				}
				else
				{
					throw new InvalidCastException(
						"Cannot convert " + typeof(TSource).Name + " to " + typeof(TResult).Name +
						" without selector.");
				}
			}

			result.Add(value);
		}

		return result;
	}

	public static World_command.Napr GetSideFacing(Transform source, Vector3 targetPos)
	{
		Vector3 dir = (targetPos - source.position).normalized;

		float f = Vector3.Dot(dir, source.forward);
		float b = Vector3.Dot(dir, -source.forward);
		float r = Vector3.Dot(dir, source.right);
		float l = Vector3.Dot(dir, -source.right);
		float u = Vector3.Dot(dir, source.up);
		float d = Vector3.Dot(dir, -source.up);

		float max = f;
		World_command.Napr result = World_command.Napr.FRONT;

		if (b &gt; max) { max = b; result = World_command.Napr.BACK; }
		if (r &gt; max) { max = r; result = World_command.Napr.RIGHT; }
		if (l &gt; max) { max = l; result = World_command.Napr.LEFT; }
		if (u &gt; max) { max = u; result = World_command.Napr.TOP; }
		if (d &gt; max) { max = d; result = World_command.Napr.BOTTOM; }

		return result;
	}

	public static void Error(string name, string err)
	{
		Debug.LogError("[Script(\"" + name + "\")] " + err);
		throw new Exception("[Script(\"" + name + "\")] " + err);
	}

	public static List&lt;Vector3&gt; GetCellCenters(GameObject g1)
	{
		const float cubeSize = 1f;
		var result = new List&lt;Vector3&gt;();

		var box = g1.GetComponent&lt;BoxCollider&gt;();
		if (box == null)
			return result;

		Vector3 center = box.center;
		Vector3 size = box.size;
		Vector3 min = center - size / 2f;

		int countX = Mathf.Max(1, Mathf.FloorToInt(size.x / cubeSize));
		int countY = Mathf.Max(1, Mathf.FloorToInt(size.y / cubeSize));
		int countZ = Mathf.Max(1, Mathf.FloorToInt(size.z / cubeSize));

		float stepX = size.x / countX;
		float stepY = size.y / countY;
		float stepZ = size.z / countZ;

		var t = g1.transform;

		Vector3Int vect;

		for (int ix = 0; ix &lt; countX; ix++)
			for (int iy = 0; iy &lt; countY; iy++)
				for (int iz = 0; iz &lt; countZ; iz++)
				{
					Vector3 localCenter = new Vector3(
						min.x + stepX * (ix + 0.5f),
						min.y + stepY * (iy + 0.5f),
						min.z + stepZ * (iz + 0.5f)
					);
					vect = new Vector3Int(t.TransformPoint(localCenter));
					result.Add(vect.ToVector3());
				}

		return result;
	}

	public static Dictionary&lt;Napr, List&lt;List&lt;Vector3&gt;&gt;&gt; GetSurfaceCoordsBySide(GameObject obj, Vector3 size)
	{
		int cellsX = Mathf.Max(Mathf.RoundToInt(size.x), 1);
		int cellsY = Mathf.Max(Mathf.RoundToInt(size.y), 1);
		int cellsZ = Mathf.Max(Mathf.RoundToInt(size.z), 1);

		const float cellSize = 1f;
		const float halfCell = 0.5f;

		Vector3 minLocal = Vector3.zero - (size * 0.5f);
		Vector3 maxLocal = Vector3.zero + (size * 0.5f);

		Transform t = obj.transform;

		var res = new Dictionary&lt;Napr, List&lt;List&lt;Vector3&gt;&gt;&gt;(6);

		// FRONT
		var frontRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsY);
		for (int y = 0; y &lt; cellsY; y++)
		{
			var row = new List&lt;Vector3&gt;(cellsX);
			float cy = minLocal.y + (y + halfCell) * cellSize;
			for (int x = 0; x &lt; cellsX; x++)
			{
				float cx = minLocal.x + (x + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(cx, cy, maxLocal.z + halfCell)));
			}
			frontRows.Add(row);
		}
		res[Napr.FRONT] = frontRows;

		// BACK
		var backRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsY);
		for (int y = 0; y &lt; cellsY; y++)
		{
			var row = new List&lt;Vector3&gt;(cellsX);
			float cy = minLocal.y + (y + halfCell) * cellSize;
			for (int x = 0; x &lt; cellsX; x++)
			{
				float cx = minLocal.x + (x + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(cx, cy, minLocal.z - halfCell)));
			}
			backRows.Add(row);
		}
		res[Napr.BACK] = backRows;

		// TOP
		var topRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsZ);
		for (int z = 0; z &lt; cellsZ; z++)
		{
			var row = new List&lt;Vector3&gt;(cellsX);
			float cz = minLocal.z + (z + halfCell) * cellSize;
			for (int x = 0; x &lt; cellsX; x++)
			{
				float cx = minLocal.x + (x + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(cx, maxLocal.y + halfCell, cz)));
			}
			topRows.Add(row);
		}
		res[Napr.TOP] = topRows;

		// BOTTOM
		var bottomRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsZ);
		for (int z = 0; z &lt; cellsZ; z++)
		{
			var row = new List&lt;Vector3&gt;(cellsX);
			float cz = minLocal.z + (z + halfCell) * cellSize;
			for (int x = 0; x &lt; cellsX; x++)
			{
				float cx = minLocal.x + (x + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(cx, minLocal.y - halfCell, cz)));
			}
			bottomRows.Add(row);
		}
		res[Napr.BOTTOM] = bottomRows;

		// RIGHT
		var rightRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsY);
		for (int y = 0; y &lt; cellsY; y++)
		{
			var row = new List&lt;Vector3&gt;(cellsZ);
			float cy = minLocal.y + (y + halfCell) * cellSize;
			for (int z = 0; z &lt; cellsZ; z++)
			{
				float cz = minLocal.z + (z + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(maxLocal.x + halfCell, cy, cz)));
			}
			rightRows.Add(row);
		}
		res[Napr.RIGHT] = rightRows;

		// LEFT
		var leftRows = new List&lt;List&lt;Vector3&gt;&gt;(cellsY);
		for (int y = 0; y &lt; cellsY; y++)
		{
			var row = new List&lt;Vector3&gt;(cellsZ);
			float cy = minLocal.y + (y + halfCell) * cellSize;
			for (int z = 0; z &lt; cellsZ; z++)
			{
				float cz = minLocal.z + (z + halfCell) * cellSize;
				row.Add(t.TransformPoint(new Vector3(minLocal.x - halfCell, cy, cz)));
			}
			leftRows.Add(row);
		}
		res[Napr.LEFT] = leftRows;

		return res;
	}

}

public abstract class Error_duble_obg : MonoBehaviour
{
	protected virtual System.Type GetGroupType()
	{
		return GetType();
	}

	private void OnValidate()
	{
		var myGroup = GetGroupType();
		var all = GetComponents&lt;Error_duble_obg&gt;();

		int count = 0;
		string existingNames = "";

		foreach (var comp in all)
		{
			if (comp.GetGroupType() == myGroup)
			{
				count++;

				if (!ReferenceEquals(comp, this))
				{
					existingNames += comp.GetType().Name + " (" + comp.gameObject.name + "), ";
				}
			}
		}

		if (count &gt; 1)
		{
			World_command.Error(gameObject.name, string.Format(
				"[G_Base Protection] Conflict on '{0}': multiple components in group '{1}'. " +
				"Found: {2}. This component ({3}) will be destroyed.",
				gameObject.name,
				myGroup.Name,
				existingNames.TrimEnd(',', ' '),
				GetType().Name));

			Destroy(this);
		}
	}

	protected virtual void OnV() { }
}

public abstract class Errors : Error_duble_obg
{
	private List&lt;Errors&gt; err = new List&lt;Errors&gt;();
	protected virtual bool UpTestError() { return true; }
	protected virtual bool AwTestError() { return true; }
	protected virtual bool StTestError() { return true; }

	private void Awake()
	{
		err = new List&lt;Errors&gt;(FindObjectsOfType&lt;Errors&gt;());
		foreach (var e in err)
		{
			if (e != null &amp;&amp; !e.AwTestError())
			{
				World_command.Error(gameObject.name, "Test_feiled");
				return;
			}
		}
		return;
	}

	private void Start()
	{
		foreach (var e in err)
		{
			if (e != null &amp;&amp; !e.StTestError())
			{
				World_command.Error(gameObject.name, "Test_feiled");
				return;
			}
		}
		return;
	}

	private void Update()
	{
		foreach (var e in err)
		{
			if (e != null &amp;&amp; !e.UpTestError())
			{
				World_command.Error(gameObject.name, "Test_feiled");
				return;
			}
		}
		return;
	}
}

public abstract class Triger : Errors
{
	public virtual void Trigers(MainSystemTrigers.trig tr) { }
}

public abstract class World_class_block_world : Triger
{
	protected sealed override System.Type GetGroupType() { return this.GetType().BaseType; }

	[System.Serializable]
	public sealed class Date_two_list
	{
		[Delayed] public int x = 0;
		[Delayed] public int y = 0;
		public World_command.Napr napr = World_command.Napr.FRONT;
	}

	public struct CoordKey
	{
		public readonly int x;
		public readonly int y;
		public readonly World_command.Napr n;

		public CoordKey(int x, int y, World_command.Napr n)
		{
			this.x = x;
			this.y = y;
			this.n = n;
		}

		public override bool Equals(object obj)
		{
			// Сначала проверяем тип, отдельно
			if (obj == null || obj.GetType() != typeof(CoordKey))
				return false;

			// Теперь безопасно приводим к структуре
			CoordKey other = (CoordKey)obj;
			return x == other.x &amp;&amp; y == other.y &amp;&amp; n == other.n;
		}

		public override int GetHashCode()
		{
			unchecked
			{
				int hash = 17;
				hash = hash * 31 + x.GetHashCode();
				hash = hash * 31 + y.GetHashCode();
				hash = hash * 31 + n.GetHashCode();
				return hash;
			}
		}
	}

}

public abstract class World_class_move : World_class_block_world
{
	public abstract Vector3 GetSize();
	public abstract bool test_napr_get(GameObject g, World_command.Date_move dm);
	public abstract string get_ore(GameObject po);
	public abstract List&lt;Date_two_list&gt; get_napr(Vector3 vec);
}

public abstract class IF_move_functional : Triger
{
	public abstract void Up_Func_Ore(List&lt;GameObject&gt; gam_inp, List&lt;GameObject&gt; gam_out);
	public abstract string move_ore();
	public abstract string get_ore_entity(GameObject entity, string ore, int len_ore = 1);
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
