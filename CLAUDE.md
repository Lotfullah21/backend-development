# CLAUDE.md

## Project

This is a **personal learning repository** for backend development with Django.
The user is a beginner. All documentation is written to be read and understood by someone learning these concepts for the first time.

## Document Structure

```
documents/
├── 01-intro-django/       Python packages, Django setup, project/app structure, settings
├── 02-framework-architecture/  MVT vs MVC
├── 03-view/               Views, URL routing, path/query/body params
├── 04-htttp/              HTTP protocol, HttpRequest, HttpResponse
├── model/                 Models, ORM, migrations, relationships
├── database/              Database setup and management
├── static-files/          Static file handling
├── tempalte/              Django templates
├── utils/                 Django commands and utilities
└── server/                Server setup
```

Each folder covers one topic. New docs go in the relevant folder.

## Writing Style

- **Audience is a beginner** — explain the concept first, then show the code.
- Be concise. One clear sentence beats a paragraph of filler.
- Every code example must be real and runnable, not pseudocode.
- Use `# urls.py` / `# views.py` comments at the top of code blocks to show which file the code belongs to.
- Use `>` blockquotes for important tips, warnings, or "why" explanations.
- End sections with a quick reference table where it adds value.

## SVG Guidelines

Only add an SVG when a diagram genuinely makes the concept clearer than text alone.

**Good cases for an SVG:**

- Flow diagrams (e.g., request through URL dispatcher to view)
- Object anatomy (e.g., what's inside HttpRequest)
- Side-by-side comparisons (e.g., path param vs query param)
- URL breakdown / labeled anatomy

**Skip SVGs for:**

- Simple lists of attributes or methods (a table is enough)
- Concepts that are self-evident from the code example
- Sections that are short and don't benefit from a visual

SVG files go in an `assets/` subfolder next to the markdown file that references them.
SVG style: dark background `#0d1117`, `ui-sans-serif` for labels, `Courier New` for code text.

## Accuracy

- Do not state things with more certainty than warranted.
- If the user demonstrates something that contradicts what was written, update the doc immediately.
- Prefer tested, concrete statements. If unsure, say so rather than guessing.

## What NOT to do

- Do not add unrelated content to a doc (e.g., gitignore info in a URL doc).
- Do not create SVGs for every doc by default — only where needed.
- Do not pad docs with filler sections.
- Do not over-engineer explanations. Keep examples minimal and focused.
