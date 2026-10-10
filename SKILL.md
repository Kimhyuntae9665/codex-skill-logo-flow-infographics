---
name: logo-flow-infographics
description: Create or revise compact flow diagrams with real standalone logos inside rounded cards, technology names below, and short role labels for agents or repeated technologies. Use for logo-first architecture or workflow graphics on a dark dotted canvas with curved arrows, including editable SVG and PNG output.
---

# Logo Flow Infographics

## Visual contract
- Use a restrained dark dotted canvas, white rounded cards, clear spacing and thin gray curved directed connectors
- **Inside each card: the actual standalone logo symbol only. Below each card: the technology name in text; for agents, add a second short role line.** Keep these areas separate. Center the name immediately below its card, inside the exported diagram; a caption or a distant PDF paragraph is not a replacement for this label
- Use a verified symbol-only variant, not a full logo-and-wordmark banner. Do not put brand lettering, technology names, stage numbers or function descriptions inside the white card. Examples of external labels: Python, Qwen3, Qwen3 Embedding, Qdrant, SQLite; use accurate names and capitalization
- When the user says "네모 안에는 이미지 로고만", "이미지 칸 안의 글자를 빼줘" or similar, remove lettering **inside the card**, while retaining the name **below the card**. Do not interpret this as an instruction to erase every label in the diagram. Remove external names only when the user explicitly requests a completely unlabeled diagram
- Keep labels short: a technology/model name and, when needed, one role line; no function paragraphs, feature lists, decorative dashboards or oversized headings. Place detailed stage explanations, AI/code/human responsibilities and necessary prototype disclaimers outside the graph
- In agent/council diagrams, show every node's actual role directly below its technology/model name: for example Strategist / 전략 검토, Skeptic / 반례 검토, Creative / 독창적 제안, Operator / 실행 설계, Audience Advocate / 사용자 관점, Synthesizer / 종합, or Coordinator / 요청 배분. Use the user's language and the inspected workflow's actual roles; do not invent an optimist/pessimist merely to distinguish two copies of a logo. Repeated technologies in different jobs also need distinguishing role lines. A distant legend, hover tooltip, or README table alone does not satisfy this rule. Put role text outside the white logo card and retain it in SVG and PNG, unless the user explicitly asks for an unlabeled diagram
- Preserve logo proportions, artwork and brand colors. Fit rather than stretch. Label an Ollama mark Ollama, not Llama
- For each real technology, use its actual identifiable logo when one exists. Prefer official brand resources or the project's official repository; use a maintained logo library only when the official asset is unavailable and record its pinned source. Do not replace Python, Qwen or other established brands with invented geometric symbols or generic code/database icons
- Search for an official standalone mark before using a wordmark asset. If a family mark represents multiple models, retain the verified family symbol and distinguish the actual models in their external labels; record that reuse in the manifest. Do not invent an embedding logo, redraw a brand or remove lettering by painting over its artwork
- Preserve the user's existing topology and approved composition during label-only edits

## Build from a verified graph
1. Derive nodes, edges and branch meaning from the user's flow or inspected project sources. Logos alone are not integration evidence. Mark synthetic/proposed graphs explicitly; do not imply deployment
2. Use provided or approved logo assets. A user request to find and use actual logos authorizes downloading the necessary public brand assets; announce the sourcing, save them locally, and record source, revision/hash and license/trademark notes. Otherwise use approved local assets or ask only when missing authorization matters. Do not silently fetch assets, install software, authenticate or publish. Bundled example glyphs are fictional demonstration shapes, not substitutes for real brand marks. If no usable logo can be verified, state that limit and use a text-only name card; use a generic symbol only when the user approves that fallback
3. Keep editable source. For a compact left-to-right static graph, use the Python helper and [input contract](references/input-contract.md). For complex routing or an interactive canvas, use the selected editor/engine while preserving the style and semantics
4. Produce SVG, then PNG with an already available renderer. The helper uses installed Inkscape and performs no network access or installation. If PNG tooling is missing, report that specific limit and preserve SVG
5. Inspect actual pixels against the layout contract: every white card contains only a recognizable verified symbol; every card has its own correctly named label centered below it; agent nodes and repeated technologies have accurate role lines below their names; no wordmark remains inside a card and no external name or required role was accidentally deleted. Also check broken images, clipping, readability, label separation, arrowheads and edge routing. For portfolio edits, replace the graphic in the existing document and render the final pages; exporting a separate PNG alone does not finish the requested portfolio edit. File existence or renderer exit 0 is insufficient
6. Deliver the image with an accurate brief caption and retain SVG plus manifest for edits. Approval to edit a diagram does not authorize unrelated publication or account changes

## Local helper
Use Python 3.9+ (standard library). Run from the skill directory, writing artifacts outside the installed skill:
~~~bash
python3 scripts/render_logo_flow.py assets/example-graph.json --svg /absolute/output/flow.svg --png /absolute/output/flow.png
~~~
The example uses fictional names and original glyphs only. Replace its graph and manifest with requested content; its branches are not a real architecture.

For copyable requests and graph edits, read [the example guide](docs/EXAMPLES.md). The [README gallery](README.md#예시-갤러리) contains six proposed graphs using verified project symbols; their source JSON, SVG, PNG and manifests are under `examples/`. These are documentation proposals, not running integrations. Rebuild them with `python scripts/render_examples.py --output output/gallery`; PNG export requires explicitly choosing an already available renderer with `--png-renderer inkscape` or `--png-renderer cairosvg`.

Read [export checks](references/export-checks.md) for portable SVG or another renderer. External-image SVGs with 1em intrinsic dimensions can work in a browser yet fail in a rasterizer. The helper embeds local assets and sets explicit intrinsic dimensions while retaining viewBox ratio and geometry.

Retain a short SVG title and an adjacent text description of relationships for accessibility. Hover labels and brand recognition alone do not communicate branch meaning. Keep that description outside the minimal visual composition.
