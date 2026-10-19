from pathlib import Path
import zipfile
archive=Path("NOVERA-SPECIALIZED-15-UNIQUE-IMAGES.zip")
names=["silent-guide","memory","quiet-care","micro-museum","reset","transit","calm-room","courtesy","window","field-note","reception-plus","kid-safe","studio-bot","aftercare","ethos"]
if not archive.is_file(): raise SystemExit("Required uploaded specialized image ZIP missing")
with zipfile.ZipFile(archive) as z:
    for name in names:
        p=f"assets/specialized/novera-{name}.webp"
        if p not in z.namelist(): raise SystemExit(f"Missing {p} in ZIP")
        data=z.read(p)
        if not data.startswith(b"RIFF") or data[8:12]!=b"WEBP": raise SystemExit(f"Invalid WebP file: {p}")
        dest=Path(p)
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(data)
        print(p,len(data))
