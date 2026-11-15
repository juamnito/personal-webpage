from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
images_dir = root / "img" / "fotos"
output_path = images_dir / "photos.json"

files = []
for item in sorted(images_dir.iterdir(), key=lambda p: p.name.lower()):
    if item.is_file() and item.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".jfif"}:
        files.append(item.name)

output_path.write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(files)} images to {output_path}")
