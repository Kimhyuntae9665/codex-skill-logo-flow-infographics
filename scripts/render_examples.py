#!/usr/bin/env python3
"""Rebuild the bundled gallery locally; never download assets or install tools."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path

from render_logo_flow import build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("output/gallery"))
    parser.add_argument("--png-renderer", choices=("inkscape", "cairosvg"))
    args = parser.parse_args()
    renderer = None
    if args.png_renderer == "inkscape":
        renderer = shutil.which("inkscape")
        if not renderer:
            parser.error("Inkscape is not on PATH; omit --png-renderer for SVG only.")
    elif args.png_renderer == "cairosvg":
        try:
            import cairosvg
        except (ImportError, OSError) as exc:
            parser.error(f"CairoSVG and its native Cairo runtime must already work: {exc}")

    root = Path(__file__).resolve().parents[1]
    graphs = sorted((root / "examples").glob("*/graph.json"))
    if not graphs:
        parser.error("No bundled example graphs found.")
    for graph in graphs:
        svg, manifest = build(graph)
        folder = args.output / graph.parent.name
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / "output.svg"
        target.write_text(svg, encoding="utf-8")
        (folder / "output.manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        if args.png_renderer == "cairosvg":
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(folder / "output.png"))
        elif renderer:
            subprocess.run(
                [renderer, str(target.resolve()), "--export-type=png",
                 "--export-filename=" + str((folder / "output.png").resolve())],
                check=True, capture_output=True, timeout=60,
            )
        if args.png_renderer:
            png = folder / "output.png"
            if not png.is_file() or png.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
                raise ValueError("PNG export failed: " + graph.parent.name)
        print(f"{graph.parent.name}: {manifest['nodes']} nodes, {manifest['edges']} edges")
    print("Inspect final pixels separately: logos, labels, proportions, and arrow routing.")


if __name__ == "__main__":
    main()
