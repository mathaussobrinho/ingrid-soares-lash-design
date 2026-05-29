"""Remove o fundo da foto da Ingrid e salva um PNG com transparência.
Uso: python tools/remove_bg.py
"""
from pathlib import Path
from rembg import remove
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "ingrid.png"
OUT = ROOT / "assets" / "ingrid-cutout.png"


def main() -> None:
    img = Image.open(SRC).convert("RGBA")
    cutout = remove(img)  # retorna RGBA com fundo transparente
    cutout.save(OUT)
    print(f"OK -> {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
