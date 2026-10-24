# ManagerGuiCr

**Файл:** `Gui/ManagerGuiCr.cs` · **Исходник:** `Assets\Scripts\Gui\ManagerGuiCr.cs` · **Размер:** 22 КБ · **Тип:** обычный класс (не MonoBehaviour)

## Назначение
Динамический менеджер UI: управление иерархией и свойствами компонентов через JSON.

## Структура
- `mgc` — Dictionary\<string, ManagerGuiCr\> (дерево элементов); `Go` — GameObject; `wd` — чертёж ([WorldGoDisasamble#Blueprint|Blueprint](WorldGoDisasamble.md)).
- `destroyType` — карта строк → типов компонентов (Image, Text, RawImage, Mask, RectMask2D, Button, InputField, Toggle, ToggleGroup, Slider, Scrollbar, Dropdown, ScrollRect) для секции `Destroy`.

## API
| Метод | Назначение |
|---|---|
| `JsonPManagerGuiCr(json)` | команды `add` / `del` / `comp` |
| `Add(go, name, path)` | добавить элемент (рекурсия по пути, инстанс + Disassemble) |
| `Get / TryGet(name, path)` | найти элемент |
| `Save(name, path)` | пересохранить чертёж |
| `Delete(name, path)` | удалить элемент |
| `ManagerComponent(name, path, jsonP, jsonPGoPathLinc)` | применить свойства + линковка объектов |
| `ReGameObject(go)` | пересобрать всё дерево под новым корнем |

## AssambleJsonUiObject — JSON-секции
`Rect` (RectTransform), `Img`, `Text`, `RawImage`, `Mask`, `RectMask2D`, `Button`, `InputField`, `Toggle`, `ToggleGroup`, `Slider`, `Scrollbar`, `Dropdown`, `ScrollRect`, `Destroy`. События — через `JsonP.JsonPActionClass` / `JsonPActionTClass<T>` (onClick, onValueChanged, onEndEdit).

## Зависимости
[World_commands](World_commands.md) (JsonP, DicConv, Error) · [WorldGoDisasamble](WorldGoDisasamble.md).

## Кто использует
[Core_Spawn](Core_Spawn.md) (GuiCrMan) · [Config](Config.md).created_pl (ReGameObject).

---
↩️ [Содержание](../Содержание.md)

## Исходный код

## Исходный код

## Исходный код

## Исходный код

<div class="alice-style">
  <!-- Скрытый чекбокс для управления сворачиванием через CSS -->
  <input type="checkbox" id="alice-toggle-ManagerGuiCr" class="alice-toggle-input" checked>
  
  <!-- Вся шапка теперь является тегом label, клик по любому месту переключает чекбокс -->
  <label for="alice-toggle-ManagerGuiCr" class="alice-style-header">
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
      <span>ManagerGuiCr.cs</span>
    </div>
    <div class="alice-style-right"></div>
  </label>

  <div class="alice-style-body">
<pre><code class="language-csharp">﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;
using System;

public class ManagerGuiCr
{
	private Dictionary&lt;string, ManagerGuiCr&gt; mgc = new Dictionary&lt;string, ManagerGuiCr&gt;();
	public GameObject Go { get; private set; }
	public WorldGoDisasamble.Blueprint wd { get; private set; }

	private Dictionary&lt;string, Type&gt; destroyType = new Dictionary&lt;string, Type&gt;() {
		{"Img", typeof(Image)},
		{"Text", typeof(Text)},
		{"RawImage", typeof(RawImage)},
		{"Mask", typeof(Mask)},
		{"RectMask2D", typeof(RectMask2D)},
		{"Button", typeof(Button)},
		{"InputField", typeof(InputField)},
		{"Toggle", typeof(Toggle)},
		{"ToggleGroup", typeof(ToggleGroup)},
		{"Slider", typeof(Slider)},
		{"Scrollbar", typeof(Scrollbar)},
		{"Dropdown", typeof(Dropdown)},
		{"ScrollRect", typeof(ScrollRect)},
	};

	private void AssambleJsonUiObject(GameObject go, string jsonc, Dictionary&lt;string, Dictionary&lt;string, GameObject&gt;&gt; dic)
	{
		JsonP json = new JsonP(jsonc);
		JsonP JP;
		List&lt;string&gt; ls;

		if(json.TryGetValue("Rect", out JP) &amp;&amp; JP != null) {
			RectTransform rt = go.GetComponent&lt;RectTransform&gt;();
			if (rt == null) { rt = go.AddComponent&lt;RectTransform&gt;(); if (rt == null) World_command.Error(go.name, "not component"); }

			rt.transform.position = JP.TryGet&lt;Vector3&gt;("pos", rt.transform.position);
			rt.sizeDelta = JP.TryGet&lt;Vector2&gt;("size", rt.sizeDelta);
			rt.anchorMin = JP.TryGet&lt;Vector2&gt;("ancMin", rt.anchorMin);
			rt.anchorMax = JP.TryGet&lt;Vector2&gt;("ancMax", rt.anchorMax);
			rt.pivot = JP.TryGet&lt;Vector2&gt;("pivot", rt.pivot);
			rt.anchoredPosition = JP.TryGet&lt;Vector2&gt;("anchPos", rt.anchoredPosition);
			rt.rotation = JP.TryGet&lt;Quaternion&gt;("rot", rt.rotation);
		}
		if(json.TryGetValue("Img", out JP) &amp;&amp; JP != null) {
			Image img = go.GetComponent&lt;Image&gt;();
			if (img == null) { img = go.AddComponent&lt;Image&gt;(); if (img == null) World_command.Error(go.name, "not component"); }

			img.sprite = JP.TryGet&lt;Sprite&gt;("sprite", img.sprite);
			img.color = JP.TryGet&lt;Color&gt;("color", img.color);
			img.type = JP.TryGet&lt;Image.Type&gt;("type", img.type);
			img.fillMethod = JP.TryGet&lt;Image.FillMethod&gt;("fm", img.fillMethod);
			img.fillOrigin = JP.TryGet&lt;int&gt;("fo", img.fillOrigin);
			img.fillAmount = JP.TryGet&lt;float&gt;("fa", img.fillAmount);
			img.preserveAspect = JP.TryGet&lt;bool&gt;("pa", img.preserveAspect);
			img.material = JP.TryGet&lt;Material&gt;("material", img.material);
			img.enabled = JP.TryGet&lt;bool&gt;("enabled", img.enabled);
		}
		if(json.TryGetValue("Text", out JP))
		{
			Text text = go.GetComponent&lt;Text&gt;();
			if (text == null) { text = go.AddComponent&lt;Text&gt;(); if (text == null) World_command.Error(go.name, "not component"); }

			text.text = JP.TryGet&lt;string&gt;("text", text.text);
			text.font = JP.TryGet&lt;Font&gt;("font", text.font);
			text.fontSize = JP.TryGet&lt;int&gt;("fontSize", text.fontSize);
			text.fontStyle = JP.TryGet&lt;FontStyle&gt;("fontStyle", text.fontStyle);
			text.color = JP.TryGet&lt;Color&gt;("color", text.color);
			text.alignment = JP.TryGet&lt;TextAnchor&gt;("aligment", text.alignment);
			text.horizontalOverflow = JP.TryGet&lt;HorizontalWrapMode&gt;("horOverflow", text.horizontalOverflow);
			text.verticalOverflow = JP.TryGet&lt;VerticalWrapMode&gt;("verOverflow", text.verticalOverflow);
			text.lineSpacing = JP.TryGet&lt;float&gt;("lineSpacing", text.lineSpacing);
			text.supportRichText = JP.TryGet&lt;bool&gt;("suppRichText", text.supportRichText);
			text.resizeTextForBestFit = JP.TryGet&lt;bool&gt;("resizeTextForBestFit", text.resizeTextForBestFit);
			text.resizeTextMaxSize = JP.TryGet&lt;int&gt;("resizeTextMaxSize", text.resizeTextMaxSize);
			text.resizeTextMinSize = JP.TryGet&lt;int&gt;("resizeTextMinSize", text.resizeTextMinSize);
			text.material = JP.TryGet&lt;Material&gt;("material", text.material);
			text.raycastTarget = JP.TryGet&lt;bool&gt;("raycTr", text.raycastTarget);
			text.enabled = JP.TryGet&lt;bool&gt;("enabled", text.enabled);
		}
		if(json.TryGetValue("RawImage", out JP))
		{
			RawImage rawi = go.GetComponent&lt;RawImage&gt;();
			if (rawi == null) { rawi = go.AddComponent&lt;RawImage&gt;(); if (rawi == null) World_command.Error(go.name, "not component"); }

			rawi.texture = JP.TryGet&lt;Texture&gt;("texture", rawi.texture);
			rawi.color = JP.TryGet&lt;Color&gt;("color", rawi.color);
			rawi.uvRect = JP.TryGet&lt;Rect&gt;("uvRect", rawi.uvRect);
			rawi.material = JP.TryGet&lt;Material&gt;("material", rawi.material);
			rawi.raycastTarget = JP.TryGet&lt;bool&gt;("raycT", rawi.raycastTarget);
			rawi.enabled = JP.TryGet&lt;bool&gt;("enabled", rawi.enabled);
		}
		if(json.TryGetValue("Mask", out JP))
		{
			Mask mask = go.GetComponent&lt;Mask&gt;();
			if (mask == null) { mask = go.AddComponent&lt;Mask&gt;(); if (mask == null) World_command.Error(go.name, "not component"); }

			mask.showMaskGraphic = JP.TryGet&lt;bool&gt;("showMaskGraphic", mask.showMaskGraphic);
			mask.enabled = JP.TryGet&lt;bool&gt;("enabled", mask.enabled);
		}
		if (json.TryGetValue("RectMask2D", out JP))
		{
			RectMask2D rectMask = go.GetComponent&lt;RectMask2D&gt;();
			if (rectMask == null) { rectMask = go.AddComponent&lt;RectMask2D&gt;(); if (rectMask == null) World_command.Error(go.name, "not component"); }

			rectMask.enabled = JP.TryGet&lt;bool&gt;("enabled", rectMask.enabled);
		}
		if (json.TryGetValue("Button", out JP))
		{
			Button button = go.GetComponent&lt;Button&gt;();
			if (button == null) { button = go.AddComponent&lt;Button&gt;(); if (button == null) World_command.Error(go.name, "not component"); }

			button.interactable = JP.TryGet&lt;bool&gt;("interactable", button.interactable);
			button.enabled = JP.TryGet&lt;bool&gt;("enabled", button.enabled);

			button.transition = JP.TryGet&lt;Button.Transition&gt;("transition", button.transition);
			button.colors = JP.TryGet&lt;ColorBlock&gt;("colors", button.colors);
			button.spriteState = JP.TryGet&lt;SpriteState&gt;("spriteState", button.spriteState);
			button.animationTriggers = JP.TryGet&lt;AnimationTriggers&gt;("animationTriggers", button.animationTriggers);
			button.navigation = JP.TryGet&lt;Navigation&gt;("navigation", button.navigation);
			button.targetGraphic = go.GetComponent&lt;Graphic&gt;();

			JsonP.JsonPActionClass onClickAction = JP.TryGet&lt;JsonP.JsonPActionClass&gt;("onClick", null);
			if (onClickAction != null) button.onClick.AddListener(onClickAction.JsonPAction);
		}
		if (json.TryGetValue("InputField", out JP))
		{
			InputField input = go.GetComponent&lt;InputField&gt;();
			if (input == null) { input = go.AddComponent&lt;InputField&gt;(); if (input == null) World_command.Error(go.name, "not component"); }

			input.interactable = JP.TryGet&lt;bool&gt;("interactable", input.interactable);
			input.enabled = JP.TryGet&lt;bool&gt;("enabled", input.enabled);

			input.text = JP.TryGet&lt;string&gt;("text", input.text);
			input.characterLimit = JP.TryGet&lt;int&gt;("characterLimit", input.characterLimit);
			input.readOnly = JP.TryGet&lt;bool&gt;("readOnly", input.readOnly);

			input.contentType = JP.TryGet&lt;InputField.ContentType&gt;("contentType", input.contentType);
			input.lineType = JP.TryGet&lt;InputField.LineType&gt;("lineType", input.lineType);
			input.inputType = JP.TryGet&lt;InputField.InputType&gt;("inputType", input.inputType);
			input.keyboardType = JP.TryGet&lt;TouchScreenKeyboardType&gt;("keyboardType", input.keyboardType);
			input.characterValidation = JP.TryGet&lt;InputField.CharacterValidation&gt;("characterValidation", input.characterValidation);

			input.caretBlinkRate = JP.TryGet&lt;float&gt;("caretBlinkRate", input.caretBlinkRate);
			input.caretColor = JP.TryGet&lt;Color&gt;("caretColor", input.caretColor);
			input.selectionColor = JP.TryGet&lt;Color&gt;("selectionColor", input.selectionColor);

			JsonP.JsonPActionTClass&lt;string&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;string&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null) input.onValueChanged.AddListener(val =&gt; onValueChangedAction.JsonPAction(val));

			JsonP.JsonPActionTClass&lt;string&gt; onEndEditAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;string&gt;&gt;("onEndEdit", null);
			if (onEndEditAction != null) input.onEndEdit.AddListener((val) =&gt; onEndEditAction.JsonPAction(val));
		}
		if (json.TryGetValue("Toggle", out JP))
		{
			Toggle toggle = go.GetComponent&lt;Toggle&gt;();
			if (toggle == null) { toggle = go.AddComponent&lt;Toggle&gt;(); if (toggle == null) World_command.Error(go.name, "not component"); }

			toggle.interactable = JP.TryGet&lt;bool&gt;("interactable", toggle.interactable);
			toggle.enabled = JP.TryGet&lt;bool&gt;("enabled", toggle.enabled);
			toggle.isOn = JP.TryGet&lt;bool&gt;("isOn", toggle.isOn);

			toggle.transition = JP.TryGet&lt;Selectable.Transition&gt;("transition", toggle.transition);
			toggle.colors = JP.TryGet&lt;ColorBlock&gt;("colors", toggle.colors);
			toggle.spriteState = JP.TryGet&lt;SpriteState&gt;("spriteState", toggle.spriteState);
			toggle.animationTriggers = JP.TryGet&lt;AnimationTriggers&gt;("animationTriggers", toggle.animationTriggers);
			toggle.navigation = JP.TryGet&lt;Navigation&gt;("navigation", toggle.navigation);
			toggle.targetGraphic = go.GetComponent&lt;Graphic&gt;();

			JsonP.JsonPActionTClass&lt;bool&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;bool&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null)
			{
				toggle.onValueChanged.RemoveAllListeners();
				toggle.onValueChanged.AddListener((val) =&gt; onValueChangedAction.JsonPAction(val));
			}
		}
		if (json.TryGetValue("ToggleGroup", out JP))
		{
			ToggleGroup tg = go.GetComponent&lt;ToggleGroup&gt;();
			if (tg == null) { tg = go.AddComponent&lt;ToggleGroup&gt;(); if (tg == null) World_command.Error(go.name, "not component"); }

			tg.allowSwitchOff = JP.TryGet&lt;bool&gt;("allowSwitchOff", tg.allowSwitchOff);

			Toggle target = null;
			Dictionary&lt;string, GameObject&gt; groupDic;
			GameObject objToggle;
			if (dic.TryGetValue("ToggleGroup", out groupDic) &amp;&amp; groupDic.TryGetValue("objToggle", out objToggle))
			{
				if (objToggle != null &amp;&amp; objToggle.activeInHierarchy)
				{
					target = objToggle.GetComponent&lt;Toggle&gt;();
				}
			}

			if (target != null)
			{
				target.isOn = true;
			}
			else
			{
				World_command.Error(go.name, "Toggle not found or destroyed");
			}
		}
		if (json.TryGetValue("Slider", out JP))
		{
			Slider slider = go.GetComponent&lt;Slider&gt;();
			if (slider == null) { slider = go.AddComponent&lt;Slider&gt;(); if (slider == null) World_command.Error(go.name, "not component"); }

			slider.interactable = JP.TryGet&lt;bool&gt;("interactable", slider.interactable);
			slider.enabled = JP.TryGet&lt;bool&gt;("enabled", slider.enabled);

			slider.minValue = JP.TryGet&lt;float&gt;("minValue", slider.minValue);
			slider.maxValue = JP.TryGet&lt;float&gt;("maxValue", slider.maxValue);
			slider.value = JP.TryGet&lt;float&gt;("value", slider.value);

			slider.wholeNumbers = JP.TryGet&lt;bool&gt;("wholeNumbers", slider.wholeNumbers);
			slider.direction = JP.TryGet&lt;Slider.Direction&gt;("direction", slider.direction);

			slider.transition = JP.TryGet&lt;Selectable.Transition&gt;("transition", slider.transition);
			slider.colors = JP.TryGet&lt;ColorBlock&gt;("colors", slider.colors);
			slider.spriteState = JP.TryGet&lt;SpriteState&gt;("spriteState", slider.spriteState);
			slider.animationTriggers = JP.TryGet&lt;AnimationTriggers&gt;("animationTriggers", slider.animationTriggers);
			slider.navigation = JP.TryGet&lt;Navigation&gt;("navigation", slider.navigation);
			slider.targetGraphic = go.GetComponent&lt;Graphic&gt;();

			JsonP.JsonPActionTClass&lt;float&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;float&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null)
			{
				slider.onValueChanged.RemoveAllListeners();
				slider.onValueChanged.AddListener((val) =&gt; onValueChangedAction.JsonPAction(val));
			}
		}
		if (json.TryGetValue("Scrollbar", out JP))
		{
			Scrollbar scrollbar = go.GetComponent&lt;Scrollbar&gt;();
			if (scrollbar == null) { scrollbar = go.AddComponent&lt;Scrollbar&gt;(); if (scrollbar == null) World_command.Error(go.name, "not component"); }

			scrollbar.interactable = JP.TryGet&lt;bool&gt;("interactable", scrollbar.interactable);
			scrollbar.enabled = JP.TryGet&lt;bool&gt;("enabled", scrollbar.enabled);

			scrollbar.size = JP.TryGet&lt;float&gt;("size", scrollbar.size);
			scrollbar.value = JP.TryGet&lt;float&gt;("value", scrollbar.value);
			scrollbar.direction = JP.TryGet&lt;Scrollbar.Direction&gt;("direction", scrollbar.direction);

			scrollbar.transition = JP.TryGet&lt;Selectable.Transition&gt;("transition", scrollbar.transition);
			scrollbar.colors = JP.TryGet&lt;ColorBlock&gt;("colors", scrollbar.colors);
			scrollbar.spriteState = JP.TryGet&lt;SpriteState&gt;("spriteState", scrollbar.spriteState);
			scrollbar.animationTriggers = JP.TryGet&lt;AnimationTriggers&gt;("animationTriggers", scrollbar.animationTriggers);
			scrollbar.navigation = JP.TryGet&lt;Navigation&gt;("navigation", scrollbar.navigation);
			scrollbar.targetGraphic = go.GetComponent&lt;Graphic&gt;();

			JsonP.JsonPActionTClass&lt;float&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;float&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null)
			{
				scrollbar.onValueChanged.RemoveAllListeners();
				scrollbar.onValueChanged.AddListener((val) =&gt; onValueChangedAction.JsonPAction(val));
			}
		}
		if (json.TryGetValue("Dropdown", out JP))
		{
			Dropdown dropdown = go.GetComponent&lt;Dropdown&gt;();
			if (dropdown == null) { dropdown = go.AddComponent&lt;Dropdown&gt;(); if (dropdown == null) World_command.Error(go.name, "not component"); }

			dropdown.interactable = JP.TryGet&lt;bool&gt;("interactable", dropdown.interactable);
			dropdown.enabled = JP.TryGet&lt;bool&gt;("enabled", dropdown.enabled);

			int selectedIndex = JP.TryGet&lt;int&gt;("selectedIndex", dropdown.value);
			if (selectedIndex &lt; 0) selectedIndex = 0;

			var options = JP.TryGet&lt;List&lt;string&gt;&gt;("options", null);
			if (options != null)
			{
				dropdown.ClearOptions();
				dropdown.AddOptions(options);

				if (selectedIndex &gt;= 0 &amp;&amp; selectedIndex &lt; dropdown.options.Count)
				{
					dropdown.value = selectedIndex;
				}
				else if (dropdown.options.Count &gt; 0)
				{
					dropdown.value = 0;
				}
			}
			else
			{
				if (selectedIndex &gt;= 0 &amp;&amp; selectedIndex &lt; dropdown.options.Count)
				{
					dropdown.value = selectedIndex;
				}
			}

			dropdown.transition = JP.TryGet&lt;Selectable.Transition&gt;("transition", dropdown.transition);
			dropdown.colors = JP.TryGet&lt;ColorBlock&gt;("colors", dropdown.colors);
			dropdown.spriteState = JP.TryGet&lt;SpriteState&gt;("spriteState", dropdown.spriteState);
			dropdown.animationTriggers = JP.TryGet&lt;AnimationTriggers&gt;("animationTriggers", dropdown.animationTriggers);
			dropdown.navigation = JP.TryGet&lt;Navigation&gt;("navigation", dropdown.navigation);
			dropdown.targetGraphic = go.GetComponent&lt;Graphic&gt;();

			JsonP.JsonPActionTClass&lt;int&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;int&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null)
			{
				dropdown.onValueChanged.RemoveAllListeners();
				dropdown.onValueChanged.AddListener((val) =&gt; onValueChangedAction.JsonPAction(val));
			}
		}
		if (json.TryGetValue("ScrollRect", out JP))
		{
			ScrollRect sr = go.GetComponent&lt;ScrollRect&gt;();
			if (sr == null) { sr = go.AddComponent&lt;ScrollRect&gt;(); if (sr == null) World_command.Error(go.name, "not component"); }

			sr.enabled = JP.TryGet&lt;bool&gt;("enabled", sr.enabled);
			sr.elasticity = JP.TryGet&lt;float&gt;("elasticity", sr.elasticity);
			sr.inertia = JP.TryGet&lt;bool&gt;("inertia", sr.inertia);
			sr.decelerationRate = JP.TryGet&lt;float&gt;("decelerationRate", sr.decelerationRate);

			sr.horizontal = JP.TryGet&lt;bool&gt;("horizontal", sr.horizontal);
			sr.vertical = JP.TryGet&lt;bool&gt;("vertical", sr.vertical);

			sr.content = JP.TryGet&lt;RectTransform&gt;("content", sr.content);

			Transform t = dic.ContainsKey("ScrollRect") &amp;&amp; dic["ScrollRect"].ContainsKey("contentName") ? dic["ScrollRect"]["contentName"].transform : null;
			if (t != null) sr.content = t as RectTransform;
			else World_command.Error(go.name, "Content not found");

			Transform t2 = dic.ContainsKey("ScrollRect") &amp;&amp; dic["ScrollRect"].ContainsKey("hScrollName") ? dic["ScrollRect"]["hScrollName"].transform : null;
			if (t2 != null) sr.horizontalScrollbar = t2.GetComponent&lt;Scrollbar&gt;();

			Transform t3 = dic.ContainsKey("ScrollRect") &amp;&amp; dic["ScrollRect"].ContainsKey("vScrollName") ? dic["ScrollRect"]["vScrollName"].transform : null;
			if (t3 != null) sr.verticalScrollbar = t3.GetComponent&lt;Scrollbar&gt;();

			sr.viewport = JP.TryGet&lt;RectTransform&gt;("viewport", sr.viewport);

			Transform t4 = dic.ContainsKey("ScrollRect") &amp;&amp; dic["ScrollRect"].ContainsKey("viewportName") ? dic["ScrollRect"]["viewportName"].transform : null;
			if (t4 != null) sr.viewport = t4 as RectTransform;

			JsonP.JsonPActionTClass&lt;Vector2&gt; onValueChangedAction = JP.TryGet&lt;JsonP.JsonPActionTClass&lt;Vector2&gt;&gt;("onValueChanged", null);
			if (onValueChangedAction != null)
			{
				sr.onValueChanged.RemoveAllListeners();
				sr.onValueChanged.AddListener((val) =&gt; onValueChangedAction.JsonPAction(val));
			}
		}
		if(json.TryGetValue("Destroy", out ls))
		{
			foreach(string st in ls)
			{
				if(st != null &amp;&amp; destroyType.ContainsKey(st))
				{
					var comp = go.GetComponents(destroyType[st]);
					foreach(var com in comp)
					{
						if(com != null)
						{
							UnityEngine.Object.Destroy(com);
						}
					}
				}
			}
		}
	}

	public ManagerGuiCr(GameObject go)
	{
		if (go.GetComponent&lt;RectTransform&gt;() == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		Go = go;
	}

	public void ReGameObject(GameObject go)
	{
		if (go.GetComponent&lt;RectTransform&gt;() == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		Go = go;
		foreach(ManagerGuiCr mc in mgc.Values)
		{
			mc.Go = WorldGoDisasamble.Assemble(mc.wd, Go.GetComponent&lt;RectTransform&gt;());
			mc.ReGameObject(mc.Go);
		}
	}

	public void JsonPManagerGuiCr(string jsonP)
	{
		if (!JsonP.IsValidJson(jsonP)) return;
		JsonP jp = new JsonP(jsonP);

		JsonP s;
		string sname;
		string[] slpath;
		if (jp.TryGetValue&lt;JsonP&gt;("add", out s)) {
			sname = s.TryGet&lt;string&gt;("name");
			slpath = s.TryGet&lt;string[]&gt;("path");

			GameObject go = new GameObject(sname); go.AddComponent&lt;RectTransform&gt;(); Add(go, sname, new List&lt;string&gt;(slpath));
		}
		if (jp.TryGetValue&lt;JsonP&gt;("del", out s)) {
			sname = s.TryGet&lt;string&gt;("name");
			slpath = s.TryGet&lt;string[]&gt;("path");

			Delete(sname, new List&lt;string&gt;(slpath));
		}
		if(jp.TryGetValue&lt;JsonP&gt;("comp", out s)) {
			sname = s.TryGet&lt;string&gt;("name");
			slpath = s.TryGet&lt;string[]&gt;("path");
			string jsp = s.TryGet&lt;string&gt;("jsonP");
			string jspGo = s.TryGet&lt;string&gt;("lincGo");

			ManagerComponent(sname, new List&lt;string&gt;(slpath), jsp, jspGo);
		}
	}

	public void Add(GameObject go, string name, List&lt;string&gt; lpathGui)
	{
		if (go == null || name == "" || lpathGui == null || go.GetComponent&lt;RectTransform&gt;() == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		List&lt;string&gt; lp = new List&lt;string&gt;(lpathGui);

		ManagerGuiCr mgcd;
		if (lp.Count != 0)
		{
			if (!mgc.TryGetValue(lp[lp.Count - 1], out mgcd)) World_command.Error(go.name, "Not path");
			lp.RemoveAt(lp.Count - 1);
			mgcd.Add(go, name, lp);
		}
		else
		{
			if (mgc.ContainsKey(name)) World_command.Error(go.name, "created Activity Obg");
			mgc.Add(name, new ManagerGuiCr(UnityEngine.Object.Instantiate(go, Go.GetComponent&lt;RectTransform&gt;())));
			mgc[name].wd = WorldGoDisasamble.Disassemble(mgc[name].Go);
		}
	}

	public GameObject Get(string name, List&lt;string&gt; lpathGui)
	{
		if (name == "" || lpathGui == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		List&lt;string&gt; lp = new List&lt;string&gt;(lpathGui);

		ManagerGuiCr mgcd;
		if (lp.Count != 0)
		{
			if (!mgc.TryGetValue(lp[lp.Count - 1], out mgcd)) World_command.Error(name, "Not path");
			lp.RemoveAt(lp.Count - 1);
			return mgcd.Get(name, lp);
		}
		else
		{
			if (!mgc.TryGetValue(name, out mgcd)) World_command.Error(name, "Not Obg on Gui Manager");
			return mgcd.Go;
		}
	}

	public GameObject TryGet(string name, List&lt;string&gt; lpathGui)
	{
		if (name == "" || lpathGui == null) return null;
		List&lt;string&gt; lp = new List&lt;string&gt;(lpathGui);

		ManagerGuiCr mgcd;
		if (lp.Count != 0)
		{
			if (!mgc.TryGetValue(lp[lp.Count - 1], out mgcd)) return null;
			lp.RemoveAt(lp.Count - 1);
			return mgcd.TryGet(name, lp);
		}
		else
		{
			if (!mgc.TryGetValue(name, out mgcd)) return null;
			return mgcd.Go;
		}
	}

	public void Save(string name, List&lt;string&gt; lpathGui)
	{
		if (name == "" || lpathGui == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		List&lt;string&gt; lp = new List&lt;string&gt;(lpathGui);

		ManagerGuiCr mgcd;
		if (lp.Count != 0)
		{
			if (!mgc.TryGetValue(lp[lp.Count - 1], out mgcd)) World_command.Error(name, "Not path");
			lp.RemoveAt(lp.Count - 1);
			mgcd.Save(name, lp);
		}
		else
		{
			if (!mgc.TryGetValue(name, out mgcd)) World_command.Error(name, "Not Obg on Gui Manager");
			mgcd.wd = WorldGoDisasamble.Disassemble(mgcd.Go);
		}
	}

	public void Delete(string name, List&lt;string&gt; lpathGui)
	{
		if (name == "" || lpathGui == null) World_command.Error("ManagerGuiCr", "parametrs == null");
		List&lt;string&gt; lp = new List&lt;string&gt;(lpathGui);

		ManagerGuiCr mgcd;
		if (lp.Count != 0)
		{
			if (!mgc.TryGetValue(lp[lp.Count - 1], out mgcd)) World_command.Error(name, "Not path");
			lp.RemoveAt(lp.Count - 1);
			mgcd.Delete(name, lp);
		}
		else
		{
			if (!mgc.Remove(name)) World_command.Error(name, "Not Obg on Gui Manager");
		}
	}

	public void ManagerComponent(string name, List&lt;string&gt; lpathGui, string jsonP, string jsonPGoPathLinc)
	{
		Dictionary&lt;string, Dictionary&lt;string, GameObject&gt;&gt; dic = new Dictionary&lt;string, Dictionary&lt;string, GameObject&gt;&gt;();
		if (JsonP.IsValidJson(jsonPGoPathLinc))
		{
			JsonP jp = new JsonP(jsonPGoPathLinc);
			foreach(var i in jp.GetCopyDicJsonP&lt;JsonP&gt;())
			{
				foreach(var j in i.Value.GetCopyDicJsonP&lt;DicConv.KeyValuePairCl&lt;string, List&lt;string&gt;&gt;&gt;())
				{
					if (!dic.ContainsKey(i.Key)) dic.Add(i.Key, new Dictionary&lt;string, GameObject&gt;());
					if (!dic[i.Key].ContainsKey(j.Key)) dic[i.Key].Add(j.Key, null);
					dic[i.Key][j.Key] = TryGet(j.Value.Key, j.Value.Value);
				}
			}
		}
		AssambleJsonUiObject(Get(name, lpathGui), jsonP, dic);
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
