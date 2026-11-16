from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
images_dir = root / "img" / "fotos"
output_path = images_dir / "photos.json"


def sort_key(path: Path):
    stem = path.stem
    if stem.isdigit():
        return (0, int(stem), path.name.lower())
    return (1, path.name.lower())


files = []
for item in sorted(images_dir.iterdir(), key=sort_key):
    if item.is_file() and item.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".jfif"}:
        files.append(item.name)

output_path.write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(files)} images to {output_path}")
