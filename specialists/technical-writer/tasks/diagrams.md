## Visual Communication

**When diagrams are required:**

- System architecture (> 3 components)
- Data flow (> 2 transformation steps)
- Sequence diagrams (> 2 actors in an interaction)
- Decision trees (> 3 decision points)

**Diagram guidelines:**

- Use Mermaid syntax for version-controllable diagrams
- Label all arrows (what data/control flows)
- Include a legend if > 5 element types
- Keep diagrams to one screen width — split if wider
- Alt-text required for accessibility

**Diagram types and when to use each:**

| Type | Use When | Tool |
|---|---|---|
| Architecture | Showing system components and connections | Mermaid flowchart |
| Sequence | Showing request/response between services | Mermaid sequenceDiagram |
| Flowchart | Showing decision logic or process steps | Mermaid flowchart |
| ER diagram | Showing data model relationships | Mermaid erDiagram |
| State diagram | Showing lifecycle of an entity | Mermaid stateDiagram |

See `references/diagram-patterns.md` for Mermaid syntax quick reference and examples.
