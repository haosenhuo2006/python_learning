"""列出当前目录中每个 Jupyter Notebook 的章节与单元统计。"""

import json
from pathlib import Path


def headings(cell: dict) -> list[str]:
    """返回 Markdown 单元中的全部标题行。"""
    source = "".join(cell.get("source", []))
    return [
        line.strip()
        for line in source.splitlines()
        if line.lstrip().startswith("#")
    ]


def main() -> None:
    root = Path(__file__).resolve().parent
    for path in sorted(root.glob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        cells = notebook.get("cells", [])
        markdown = sum(c.get("cell_type") == "markdown" for c in cells)
        code = sum(c.get("cell_type") == "code" for c in cells)
        print(f"\n{path.name}: {markdown} markdown, {code} code")
        for cell in cells:
            if cell.get("cell_type") == "markdown":
                for heading in headings(cell):
                    print(" ", heading)


if __name__ == "__main__":
    main()
