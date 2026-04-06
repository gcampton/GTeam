# Common ARIA Patterns

Reference for implementing accessible custom widgets. Always prefer native HTML elements first. [TESTED]

---

## Dialog (Modal)

**When to use:** Overlay content that requires user interaction before continuing.

**Required roles/attributes:**
- Container: `role="dialog"`, `aria-modal="true"`, `aria-labelledby="[heading-id]"`
- Close button with accessible name

**Keyboard interaction:**
- `Tab` / `Shift+Tab` — cycle focus within the dialog (focus trap)
- `Escape` — close the dialog
- On open: focus moves to first focusable element (or the dialog itself)
- On close: focus returns to the element that triggered the dialog

```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Delete item?</h2>
  <p>This action cannot be undone.</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

---

## Tabs

**When to use:** Switching between panels of related content without page navigation.

**Required roles/attributes:**
- Tab list: `role="tablist"`
- Each tab: `role="tab"`, `aria-selected="true|false"`, `aria-controls="[panel-id]"`
- Each panel: `role="tabpanel"`, `aria-labelledby="[tab-id]"`

**Keyboard interaction:**
- `Arrow Left/Right` — move between tabs (horizontal tablist)
- `Arrow Up/Down` — move between tabs (vertical tablist)
- `Tab` — move focus from active tab into the tab panel
- `Home/End` — first/last tab

```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1">Profile</button>
  <button role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">Security</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">Profile content...</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>Security content...</div>
```

---

## Accordion

**When to use:** Expandable/collapsible sections of content.

**Required roles/attributes:**
- Trigger: `<button>` with `aria-expanded="true|false"`, `aria-controls="[section-id]"`
- Panel: linked via `id` matching `aria-controls`

**Keyboard interaction:**
- `Enter` / `Space` — toggle section open/closed
- `Arrow Up/Down` — move between accordion headers (optional)
- `Home/End` — first/last header (optional)

```html
<h3>
  <button aria-expanded="false" aria-controls="section-1">Shipping information</button>
</h3>
<div id="section-1" role="region" aria-labelledby="..." hidden>
  <p>We ship worldwide within 5-7 business days...</p>
</div>
```

---

## Menu (Navigation/Action)

**When to use:** Dropdown menus for actions (not navigation links — use `<nav>` with `<ul>` for navigation).

**Required roles/attributes:**
- Container: `role="menu"`
- Items: `role="menuitem"` (or `role="menuitemcheckbox"` / `role="menuitemradio"`)
- Trigger: `aria-haspopup="true"`, `aria-expanded="true|false"`

**Keyboard interaction:**
- `Enter` / `Space` — open menu; activate menu item
- `Arrow Down` — next menu item (or open menu from trigger)
- `Arrow Up` — previous menu item
- `Escape` — close menu, return focus to trigger
- `Home/End` — first/last item
- Type-ahead: typing a letter moves to the next item starting with that letter

```html
<button aria-haspopup="true" aria-expanded="false" aria-controls="actions-menu">Actions</button>
<ul role="menu" id="actions-menu" hidden>
  <li role="menuitem">Edit</li>
  <li role="menuitem">Duplicate</li>
  <li role="menuitem">Delete</li>
</ul>
```

---

## Combobox (Autocomplete)

**When to use:** Text input with a dropdown list of suggestions.

**Required roles/attributes:**
- Input: `role="combobox"`, `aria-expanded="true|false"`, `aria-autocomplete="list|both"`, `aria-controls="[listbox-id]"`, `aria-activedescendant="[option-id]"`
- Listbox: `role="listbox"`
- Options: `role="option"`, `aria-selected="true|false"`

**Keyboard interaction:**
- `Arrow Down` — open list / next option
- `Arrow Up` — previous option
- `Enter` — select highlighted option
- `Escape` — close list, clear selection
- Typing filters the list

```html
<label for="city">City</label>
<input id="city" role="combobox" aria-expanded="true" aria-autocomplete="list"
       aria-controls="city-listbox" aria-activedescendant="city-2">
<ul role="listbox" id="city-listbox">
  <li role="option" id="city-1">Brisbane</li>
  <li role="option" id="city-2" aria-selected="true">Sydney</li>
  <li role="option" id="city-3">Melbourne</li>
</ul>
```

---

## Live Region

**When to use:** Dynamic content updates that should be announced to screen readers without moving focus.

**Attributes:**
- `aria-live="polite"` — announces at next pause (use for most updates: "Item added to cart")
- `aria-live="assertive"` — interrupts current announcement (use for urgent alerts: "Session expiring in 30 seconds")
- `role="status"` — implicit `aria-live="polite"` (use for status messages)
- `role="alert"` — implicit `aria-live="assertive"` (use for errors/warnings)
- `aria-atomic="true"` — announces the entire region content, not just changes

```html
<!-- Status message (polite) -->
<div role="status" aria-live="polite">
  <!-- Updated dynamically via JS -->
  3 items in your cart
</div>

<!-- Error alert (assertive) -->
<div role="alert" aria-live="assertive">
  <!-- Injected when error occurs -->
  Payment failed. Please check your card details.
</div>

<!-- Search results count -->
<div aria-live="polite" aria-atomic="true">
  Showing 24 of 156 results
</div>
```

**Important:** The live region container must exist in the DOM *before* content is injected. Adding a container with `aria-live` and content simultaneously won't be announced.
