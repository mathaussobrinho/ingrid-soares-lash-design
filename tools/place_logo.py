"""Compoe o logo 'IS' sobre o peito da Ingrid, simulando estampa na camisa.
Uso: python tools/place_logo.py [cx] [cy] [size] [mode]
  cx, cy : centro do logo na imagem (px)
  size   : diametro do logo (px)
  mode   : 'color' (emblema circular colorido) ou 'white' (monocromatico branco)
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
PHOTO = ROOT / "assets" / "ingrid-cutout.png"
ICON = ROOT / "assets" / "icon.png"
OUT = ROOT / "assets" / "ingrid-logo.png"

cx = int(sys.argv[1]) if len(sys.argv) > 1 else 330
cy = int(sys.argv[2]) if len(sys.argv) > 2 else 540
size = int(sys.argv[3]) if len(sys.argv) > 3 else 95
mode = sys.argv[4] if len(sys.argv) > 4 else "color"
rot = -8  # leve inclinacao para acompanhar o corpo


def circular(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, s, s), fill=255)
    img.putalpha(mask)
    return img


def to_white(img: Image.Image) -> Image.Image:
    """Extrai as letras escuras do icone e pinta de branco (estampa tom-sobre-tom)."""
    gray = ImageOps.grayscale(img.convert("RGB"))
    # letras roxas sao mais escuras que o fundo lilas
    alpha = gray.point(lambda p: 255 if p < 120 else 0)
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    white = Image.new("RGBA", img.size, (255, 255, 255, 0))
    white.putalpha(alpha)
    rgb = Image.new("RGBA", img.size, (245, 240, 250, 0))
    rgb.putalpha(alpha)
    return rgb


def main() -> None:
    photo = Image.open(PHOTO).convert("RGBA")
    icon = Image.open(ICON)

    emblem = circular(icon) if mode == "color" else to_white(icon)
    emblem = emblem.resize((size, size), Image.LANCZOS)
    emblem = emblem.rotate(rot, expand=True, resample=Image.BICUBIC)

    # sombra suave para integrar ao tecido
    if mode == "color":
        shadow = Image.new("RGBA", emblem.size, (0, 0, 0, 0))
        sh_alpha = emblem.split()[3].point(lambda p: int(p * 0.55))
        shadow.putalpha(sh_alpha)
        shadow = shadow.filter(ImageFilter.GaussianBlur(4))
        sx = cx - emblem.width // 2 + 3
        sy = cy - emblem.height // 2 + 4
        photo.alpha_composite(shadow, (sx, sy))

    x = cx - emblem.width // 2
    y = cy - emblem.height // 2
    photo.alpha_composite(emblem, (x, y))
    photo.save(OUT)
    print(f"OK -> {OUT.name} centro=({cx},{cy}) size={size} mode={mode}")


if __name__ == "__main__":
    main()
