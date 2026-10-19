from pathlib import Path
import re, zipfile
archive=Path("NOVERA-10-ROBOTS-IMAGES-NEW.zip")
names=["home","scout","field","access","buddy","cargo","med","agri","serve","guard"]
if not archive.is_file():
    raise SystemExit("Uploaded archive missing")
with zipfile.ZipFile(archive) as z:
    files=[n for n in z.namelist() if not n.endswith("/") and not n.startswith("__MACOSX/")]
    for name in names:
        options=[n for n in files if re.search(r"(?:^|[\\/])(?:novera[-_])?"+re.escape(name)+r"\.webp$",n,re.I)]
        if len(options)!=1:
            raise SystemExit(f"{name}: expected one .webp; found {options}. Archive entries: {files}")
        dest=Path("assets/robots")/f"novera-{name}.webp"
        dest.parent.mkdir(parents=True,exist_ok=True)
        content=z.read(options[0])
        if not content.startswith(b"RIFF") or content[8:12]!=b"WEBP":
            raise SystemExit(f"Invalid WebP data for {name}")
        dest.write_bytes(content)
        print(f"Added {dest} ({len(content)} bytes)")
