# Logo asset sources

These unmodified standalone SVG symbols were fetched at the pinned commits below. The example flows are authored proposals, not evidence of integration. Logos stay inside cards; accurate technology names stay below cards. Monochrome fallback variants are preserved as supplied, not recolored or redrawn.

| Asset | Source / pinned revision | License record | Variant / selection reason |
| --- | --- | --- | --- |
| React | [SVG](https://raw.githubusercontent.com/facebook/react/b618bbb4422693bbb8d387180687b3f510300f42/fixtures/dom/public/react-logo.svg) · `b618bbb4422693bbb8d387180687b3f510300f42` | [MIT](REACT-LICENSE.txt) | Official React repository; standalone atom mark. |
| GitHub | [SVG](https://raw.githubusercontent.com/primer/octicons/97825f832c98f817867f770d084c08e3edc6f78c/icons/mark-github-16.svg) · `97825f832c98f817867f770d084c08e3edc6f78c` | [MIT](OCTICONS-LICENSE.txt) | Official GitHub Primer Octicons; standalone mark. |
| Vite | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/vite.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Official current symbol uses unsupported SVG filters; unmodified monochrome Simple Icons variant selected for this restricted helper. |
| FastAPI | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/fastapi.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Official inspected standalone icon is white on white cards; unmodified monochrome Simple Icons variant selected. |
| Python | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/python.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Official inspected SVG includes metadata outside helper subset; unmodified monochrome Simple Icons variant selected. |
| Docker | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/docker.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Official media kit located; pinned standalone SVG not established in this pass. Unmodified Simple Icons variant selected. |
| SQLite | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/sqlite.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Usable official standalone SVG not established in this pass. Unmodified Simple Icons variant selected. |
| Qdrant | [SVG](https://raw.githubusercontent.com/simple-icons/simple-icons/98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d/icons/qdrant.svg) · `98820a4dc8c363ca72fa2c0d294ea4a0a9bba75d` | [CC0-1.0](SIMPLE-ICONS-LICENSE.txt) | Inspected official logo is a horizontal wordmark lockup; unmodified standalone Simple Icons variant selected. |

## Official-source checks before library fallback

- Vite: [current official symbol](https://github.com/vitejs/vite/blob/574d5e351905fe99891364d03c2440531378f7fd/docs/public/logo-without-border.svg); contains filters outside the helper subset.
- FastAPI: [official white symbol](https://github.com/fastapi/fastapi/blob/9269f17524e7990c39a9a1708db532810ceffc06/docs/en/docs/img/icon-white.svg); white artwork is unsuitable for these white cards.
- Python: [official inspected asset](https://github.com/python/pythondotorg/blob/e1ca31a8594668217e7d40bdd284ce890cc92cc0/static/community_logos/python-logo-generic.svg); contains metadata outside the restricted parser. [PSF trademark policy](https://www.python.org/psf/trademarks/).
- Docker: [official media resources](https://www.docker.com/company/newsroom/media-resources/); an official kit exists, but a pinned SVG suitable for this helper was not established in this pass.
- Qdrant: [official inspected lockup](https://github.com/qdrant/qdrant/blob/016542aa5deb6c66380bb137badf73d54f742bde/docs/logo.svg); wide logo-and-wordmark rather than standalone symbol.
- SQLite: usable official standalone SVG not established in this pass; this is a sourcing limitation, not a claim that no official symbol exists.

## Hashes and trademark boundary

The [input manifest](manifest.json) records the SHA-256 of every exact downloaded file. Each output manifest records the original hash and the embedded normalized hash. Normalization changes intrinsic dimensions and XML serialization, not geometry or colors.

React, GitHub, Vite, FastAPI, Python, Docker, SQLite, and Qdrant names and marks belong to their respective owners. Copyright licenses do not waive trademark conditions or imply sponsorship. MIT notices and the Simple Icons CC0 text are retained beside the source assets. This documentation illustrates the marks for identification; it does not grant additional brand-use rights.

For a production or commercial publication, consult the relevant brand policy and use the approved variant for that context. Exact output fonts may differ between renderers; inspect the final PNG or SVG before sharing.
