# Config

**Файл:** `Core/Config.cs` · **Исходник:** `Assets\Scripts\Config.cs` · **Тип:** MonoBehaviour (`Errors`)

## Содержимое
- `State_cr` (struct) — пара объектов-рендеров: `Act` (можно строить) / `notAct` (нельзя).
- `Config` — главный конфиг и владелец статического индекса сцены `obg_scene` (DicVec).

## API (статический)
| Метод | Назначение |
|---|---|
| `Add_obg_scene` | регистрация объекта в индексе (требует BoxCollider) |
| `Test_Cr_Bl` | можно ли построить блок в этой позиции |
| `Get_obg_scene` / `Get_obg_sceneGo` | объекты в ячейке |
| `Get_obg_size_scene` / `GetBlockRadScene` / `Get_Box_obg_scene` | объекты в области |
| `Destroy_obj_scene` / `Destroy_obj_size_scene` / `Destroy_obj_all_pos_scene` / `Destroy_rad_obj_scene` | удаление из индекса |

## Экземплярные поля/методы
`Ico_Defult`, `state_create_block`, `prefabs_sattings` (ScriptableObject-пресеты блоков), `player_prefab`, `created_pl` — создание игрока и пересоздание [ManagerGuiCr](ManagerGuiCr.md).

## Зависимости
[World_commands](World_commands.md) (DicVec, ProcessObjects, GetCellCenters, Error), [Sattings_block_cr](Sattings_block_cr.md) (Prefab_Go, Sattings_Block_Created_Level), [Move_person](Move_person.md), [Created_block](Created_block.md), [ManagerGuiCr](ManagerGuiCr.md).

## Кто использует
[Ore](Ore.md), [Created_block](Created_block.md), [Move_class](Move_class.md), [Core_Spawn](Core_Spawn.md), [ORE_BLOCK](ORE_BLOCK.md).
<<<<<<< HEAD

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Config" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Config" class="alice-style-header">
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
      <span>Config.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

[System.Serializable]
public struct State_cr
{
	public GameObject Act;
	public GameObject notAct;

	public State_cr(GameObject act, GameObject notAct)
	{
		Act = act;
		this.notAct = notAct;
	}
}

public class Config : Errors
{
	[SerializeField] private Sprite Ico_Defult;
	[SerializeField] private State_cr state_create_block;
	[SerializeField] private List&lt;DicVec.TypeGenerated&gt; prefabs_sattings = new List&lt;DicVec.TypeGenerated&gt;();
	private static DicVec obg_scene = new DicVec();

	public Sprite GetDefultIco()
	{
		return Ico_Defult;
	}

	public State_cr GetRenderStateCrBl()
	{
		return state_create_block;
	}

	public static bool Test_Cr_Bl(GameObject obj, DicVec.TypeGenerated sattings)
	{
		if (obj == null || sattings == null) return false;
		foreach (var pos in World_command.GetCellCenters(obj))
		{
			if (!obg_scene.TestCreateBlock(pos, sattings))
			{
				return true;
			}
		}
		return false;
	}

	public List&lt;DicVec.TypeGenerated&gt; get_prefabs()
	{
		return prefabs_sattings;
	}

	public static void Add_obg_scene(GameObject g, DicVec.TypeGenerated sattings_Block_Cr)
	{
		if (g.GetComponent&lt;BoxCollider&gt;() == null) World_command.Error(g.name, "not component BoxCollaider");
		List&lt;Vector3&gt; vec = World_command.GetCellCenters(g);
		foreach (Vector3 ve in vec)
		{
			if (obg_scene.GetAllInCellGo(ve, sattings_Block_Cr.GetTypeGenerated()).Contains(g)) return;
		}
		if (vec.Count == 0) return;
		foreach (Vector3 vect in vec)
		{
			obg_scene.Add(g, vect, sattings_Block_Cr);
		}
	}

	public static List&lt;GameObject&gt; GetBlockRadScene(Vector3 pos, Vector3 size, DicVec.Generated generated)
	{
		return World_command.ProcessObjects&lt;DicVec.GameInfo, GameObject&gt;(obg_scene.GetInBoxWithSize(pos, size, generated), selector: t);
	}

	public static bool If_Set_Block(GameObject g, DicVec.Generated generated)
	{
		return obg_scene.GetAllInCell(g.transform.position, generated) == null;
	}

	public static List&lt;DicVec.GameInfo&gt; Get_obg_size_scene(GameObject go, DicVec.Generated generated)
	{
		if (go == null || go.GetComponent&lt;BoxCollider&gt;() == null) World_command.Error(go.name, "not component BoxCollaider");
		return obg_scene.GetInBoxWithSize(go.transform.position, go.GetComponent&lt;BoxCollider&gt;().size, generated);
	}

	public static List&lt;DicVec.GameInfo&gt; Get_obg_scene(Vector3 vec, DicVec.Generated generated)
	{
		return obg_scene.GetAllInCell(vec, generated);
	}

	private static GameObject t(DicVec.GameInfo gi) { return gi.go; }
	public static List&lt;GameObject&gt; Get_obg_sceneGo(Vector3 vec, DicVec.Generated generated)
	{
		return World_command.ProcessObjects&lt;DicVec.GameInfo, GameObject&gt;(obg_scene.GetAllInCell(vec, generated), selector: t);
	}

	public static List&lt;GameObject&gt; Get_Box_obg_scene(Vector3 vec, DicVec.Generated generated, float rad = 0.1f)
	{
		return World_command.ProcessObjects&lt;DicVec.GameInfo, GameObject&gt;(obg_scene.GetInBox(vec, rad, generated), selector: t);
	}

	public static void Destroy_obj_scene(GameObject g, DicVec.Generated generated)
	{
		obg_scene.Remove(g, g.transform.position, generated);
	}

	public static void Destroy_obj_size_scene(GameObject g, DicVec.Generated generated)
	{
		foreach (Vector3 ve in World_command.GetCellCenters(g))
		{
			obg_scene.Remove(g, ve, generated);
		}
	}

	public static void Destroy_obj_all_pos_scene(Vector3 vec, DicVec.Generated generated)
	{
		List&lt;Vector3&gt; vecl;
		foreach (DicVec.GameInfo g in obg_scene.GetAllInCell(vec, generated))
		{
			vecl = World_command.GetCellCenters(g.go);
			foreach (Vector3 ve in vecl)
			{
				obg_scene.Remove(g.go, ve, generated);
			}
		}
	}

	public static void Destroy_rad_obj_scene(Vector3 vec, float rad, DicVec.Generated generated)
	{
		obg_scene.RemoveInBox(vec, rad, generated);
	}

	[SerializeField] private GameObject player_prefab;

	private Prefab_Go sbcinprg(Sattings_Block_Created_Level sbcl)
	{
		return sbcl.sbc.Obj[sbcl.lev];
	}

	public void created_pl(Vector3 pos, List&lt;Sattings_Block_Created_Level&gt; lprefab_Go, Core_res g, ref GameObject go, Config conf, ref ManagerGuiCr mgc)
	{
		if (go == null &amp;&amp; player_prefab != null)
		{
			go = Instantiate(player_prefab, new Vector3(pos.x, 2, pos.z), player_prefab.transform.rotation);
			var movp = go.GetComponent&lt;Move_person&gt;();
			if (go.GetComponent&lt;Created_block&gt;() == null || movp == null)
			{
				Destroy(go);
				World_command.Error(gameObject.name, "error get component");
				return;
			}
			g.MainCam = movp.MainCam;
			if (mgc == null) mgc = new ManagerGuiCr(go);
			mgc.ReGameObject(go);
		}
		else
		{
			World_command.Error(gameObject.name, "created act player");
		}
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
