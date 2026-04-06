# Pre-Launch Accessibility Checklist

Quick verification checklist grouped by POUR. Target: WCAG 2.2 Level AA.

## Perceivable

- [ ] All images have meaningful `alt` text (decorative images have `alt=""`)
- [ ] Video has accurate, synchronised captions
- [ ] Audio content has a text transcript
- [ ] Colour contrast meets minimums (4.5:1 normal text, 3:1 large text)
- [ ] Information is not conveyed by colour alone (icons, text, or patterns supplement colour)
- [ ] Content reflows at 320px width without horizontal scrolling
- [ ] UI component and graphical object contrast meets 3:1
- [ ] Text spacing can be overridden without content loss (no fixed-height text containers)
- [ ] Tooltips and hover content: dismissible, hoverable, persistent

## Operable

- [ ] All functionality available via keyboard alone
- [ ] No keyboard traps — user can Tab out of every component
- [ ] Skip navigation link present and functional
- [ ] Each page has a unique, descriptive `<title>`
- [ ] Tab order follows logical reading sequence
- [ ] Visible focus indicator on all interactive elements (>= 2px, 3:1 contrast)
- [ ] Interactive targets are >= 24x24 CSS pixels
- [ ] Drag operations have single-pointer alternatives
- [ ] No content flashes more than 3 times per second
- [ ] Time limits can be extended or turned off

## Understandable

- [ ] Page language declared with `<html lang="...">`
- [ ] Language changes marked with `lang` attribute on containing element
- [ ] Navigation is consistent across pages
- [ ] Same function uses the same label across the site
- [ ] Form errors identified in text with suggestions for correction
- [ ] Every form input has a visible, associated `<label>`
- [ ] Required fields identified before form submission
- [ ] Legal/financial submissions: reversible, checked, or confirmed
- [ ] No redundant data entry in multi-step processes

## Robust

- [ ] Valid HTML (no duplicate IDs, proper nesting)
- [ ] Custom widgets have appropriate ARIA roles, states, and properties
- [ ] Status messages announced to screen readers (`role="status"` or `aria-live`)
- [ ] Accessible authentication (no cognitive function test as sole method)

## Assistive Technology Spot-Check

- [ ] Screen reader: page landmarks announced correctly
- [ ] Screen reader: heading hierarchy forms a logical outline
- [ ] Screen reader: form labels announced on focus
- [ ] Keyboard: modals trap focus and return focus on close
- [ ] Zoom: content usable at 200% browser zoom
- [ ] Motion: `prefers-reduced-motion` respected
