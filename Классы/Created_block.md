# Created_block

**Файл:** `Player/Created_block.cs` · **Исходник:** `Assets\Scripts\Player\Created_block.cs` · **Тип:** `Errors` (RequireComponent → [Move_person](Move_person.md))

## Назначение
Постройка блоков игроком: призрак блока, подсветка, создание.

## Поля
- `layer` (LayerMask — куда рейкастить), `conf` (Config), `cam`.
- `Obj` (`DicVec.GamePlayerBuildBlock`: префаб-призрак + настройки + child), `SizeObj`, `quaternion1` (поворот), `_renderChild`, `_go_state`, `_hit_pos`, `smeschenie`, `TypeGenerated` (`PlayerBlock`), `Obj_coninue_create`.

## Методы/логика
- `Rotarions(Quaternion)` — задать поворот (с проверкой диапазона).
- `Create_block_Render(Prefab_Go)` — валидирует префаб (нужен BoxCollider), создаёт призрак.
- `CrBlRenderColor(...)` — подсветка Act/notAct из `conf.GetRenderStateCrBl()`, ленивое пересоздание рендера.
- `Update` — рейкаст из камеры, позиция по сетке (Floor + 0.5 + смещение), ЛКМ → `Set_bl_cr`.
- `Set_bl_cr` — создание блока: проверка лимита (`Config.Test_Cr_Bl`), слой «Collaider», `Config.Add_obg_scene`, `MainSystemTrigers.ResetClTr` + `RegistTrig(Update_Block)`.

## Зависимости
[Config](Config.md) · [World_commands](World_commands.md) · [Sattings_block_cr](Sattings_block_cr.md) (Prefab_Go, PlayerBlock) · [MainSystemTrigers](MainSystemTrigers.md) · [Move_person](Move_person.md).

## Кто использует
[ButtonCreateBlock](ButtonCreateBlock.md) · [Config](Config.md).created_pl.

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-Created_block" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-Created_block" class="alice-style-header">
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
      <span>Created_block.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Move_person))]
public class Created_block : Errors
{
	[SerializeField] private LayerMask layer;
	[SerializeField] private Config conf;
	private Camera cam;
	private DicVec.GamePlayerBuildBlock Obj = new DicVec.GamePlayerBuildBlock();
	private Vector3 SizeObj = Vector3.one;
	private Quaternion quaternion1 = Quaternion.identity;
	private GameObject _renderChild;
	private bool _go_state;
	private Vector3 _hit_pos = Vector3.zero;
	private Vector3 smeschenie = Vector3.zero;
	private DicVec.TypeGenerated TypeGenerated;
	private List&lt;DicVec.GamePlayerBuildBlock&gt; Obj_coninue_create = new List&lt;DicVec.GamePlayerBuildBlock&gt;();

	public void Rotarions(Quaternion quaternion)
	{
		if (quaternion.x &gt;= -360 || quaternion.x &lt;= 360 || quaternion.y &gt;= -360 || quaternion.y &lt;= 360 || quaternion.z &gt;= -360 || quaternion.z &lt;= 360)
		{
			quaternion1 = quaternion;
		}
		else
		{
			World_command.Error(gameObject.name, "In Rotarions set big float or miny float");
		}
	}

	void Awake()
	{
		var com = gameObject.GetComponent&lt;Move_person&gt;();
		cam = com.MainCam;
		if (com == null || cam == null) World_command.Error(gameObject.name, "not component Camera");
	}

	protected override bool StTestError()
	{
		return cam != null;
	}

	public void Create_block_Render(Prefab_Go sbc)
	{
		if (cam == null) return;
		if (sbc == null) World_command.Error(gameObject.name, "not prefab in Sattings_block_create");
		if (sbc.Prefab == null || sbc.go == null || sbc.Prefab.GetComponent&lt;BoxCollider&gt;() == null) World_command.Error(gameObject.name, "In Sattings_block_cr gameObgect not component BoxCollider");
		if (sbc == null) return;
		if (Obj.go != null) { Destroy(Obj.go); }
		Obj.go = Instantiate(sbc.Prefab);
		Obj.sattings = sbc;
		SizeObj = Obj.go.GetComponent&lt;BoxCollider&gt;().size;
		TypeGenerated = new PlayerBlock();
	}

	private void CrBlRenderColor(Vector3 vec, Quaternion quaternion, Vector3 size, bool act)
	{
		State_cr rgo = conf.GetRenderStateCrBl();
		if (rgo.Act == null || rgo.notAct == null)
		{
			World_command.Error(gameObject.name, "Not obj RenderObj");
			return;
		}

		GameObject go = act ? rgo.Act : rgo.notAct;
		if (go == null)
		{
			World_command.Error(gameObject.name, "Not obg in Renderer in " + (act ? "Act" : "notAct"));
			return;
		}

		if (_renderChild == null || act != _go_state)
		{
			if (_renderChild != null) Destroy(_renderChild);
			_renderChild = Instantiate(go, vec, quaternion, Obj.go.transform);
			_renderChild.transform.localScale = size + new Vector3(0.1f, 0.1f, 0.1f);
			_go_state = act;
		}
		else
		{
			_renderChild.transform.position = vec;
			_renderChild.transform.rotation = quaternion;
			_renderChild.transform.localScale = size + new Vector3(0.1f, 0.1f, 0.1f);
		}
	}


	private void Set_bl_cr(Vector3 vec, Quaternion quaternion)
	{
		if (cam == null) return;
		if (Obj.child != null) { Destroy(Obj.child); Obj.child = null; }
		if (Obj.go == null || Obj.sattings.go == null || Obj.sattings.Prefab == null) return;
		Destroy(Obj.go);
		GameObject go = Instantiate(Obj.sattings.go, vec, quaternion);
		if (Config.Test_Cr_Bl(go, TypeGenerated))
		{
			World_command.Error(gameObject.name, "block created &gt; max in block");
		}
		go.layer = LayerMask.NameToLayer("Collaider");
		Config.Add_obg_scene(go, TypeGenerated);
		MainSystemTrigers.ResetClTr();
		Obj.go = null;
		Obj.sattings = null;
		MainSystemTrigers.RegistTrig(MainSystemTrigers.trig.Update_Block);
	}

	void Update()
	{
		if (Obj.go != null &amp;&amp; Obj.sattings != null)
		{
			if (cam == null)
			{
				Destroy(Obj.go);
				Obj.sattings = null;
				Destroy(Obj.child);
			}
			Ray ray = cam.ScreenPointToRay(Input.mousePosition);
			RaycastHit hit;
			if (Physics.Raycast(ray, out hit, 100f, layer))
			{
				_hit_pos = (hit.point + new Vector3(0, SizeObj.y / 2, 0)) + hit.normal * 0.1f;
				smeschenie = Obj.sattings.vecPrSmetheniePaste;
				_hit_pos = new Vector3((Mathf.Floor(_hit_pos.x) + 0.5f) + smeschenie.x, Mathf.Floor(_hit_pos.y) + smeschenie.y, (Mathf.Floor(_hit_pos.z) + 0.5f) + smeschenie.z);
				Obj.go.transform.position = _hit_pos;
				if (!Config.Test_Cr_Bl(Obj.go, TypeGenerated))
				{
					CrBlRenderColor(Obj.go.transform.position, Quaternion.identity, SizeObj, true);
					if (Input.GetMouseButtonDown(0))
					{
						Set_bl_cr(_hit_pos, quaternion1);
					}
				}
				else
				{
					CrBlRenderColor(Obj.go.transform.position, Quaternion.identity, SizeObj, false);
				}
			}
			else
			{
				CrBlRenderColor(Obj.go.transform.position, Quaternion.identity, SizeObj, false);
			}
		}
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
