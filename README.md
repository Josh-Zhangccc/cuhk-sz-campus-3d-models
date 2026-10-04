# CUHK-Shenzhen Campus 3D Scene Assets

3D scene assets of the **CUHK-Shenzhen campus** (Upper Garden / Middle Garden / Lower Garden, plus props), extracted from an abandoned Unity virtual-campus project and converted into portable formats.

Intended use: a campus traffic simulation study (bicycles / buses), or any other reuse of the campus models.

---

## Repository layout

| Location | Content |
|---|---|
| `previews/` | Rendered preview images (Blender workbench) of the three converted scenes |
| `unity_scenes/` | Original Unity scene files (`.unity`, YAML) — they record how every object is placed in the scene |
| `tools/` | Headless Blender scripts used for verification and preview rendering |
| `docs/export_summary.txt` | Log summary of the Unity → glTF export run |
| `CHECKSUMS.txt` | SHA-256 checksums of every release asset |
| **Release assets (v1.0)** | All large binary files — see table below |

All large files live in the [Releases](../../releases) section, not in the git tree, because several exceed GitHub's 100 MB repository file limit.

## Release assets (v1.0)

### Converted, ready-to-use formats (recommended starting point)

| File | Size | Description |
|---|---|---|
| `uppergarden.gltf` + `uppergarden.bin` | ~800 MB | Upper Garden scene as glTF 2.0 (geometry + placement + textures embedded in the bin) |
| `middlegarden.gltf` + `middlegarden.bin` | ~710 MB | Middle Garden scene as glTF 2.0 |
| `undergarden.gltf` + `undergarden.bin` | ~430 MB | Lower Garden scene as glTF 2.0 |
| `uppergarden.blend` | ~595 MB | Same scenes saved as native Blender files (open directly, no import needed) |
| `middlegarden.blend` | ~600 MB | 〃 |
| `undergarden.blend` | ~300 MB | 〃 |

### Original source assets (as they came from the old project)

| File | Size | Description |
|---|---|---|
| `uppergarden_Up.fbx` | 1.32 GB | Upper Garden source model |
| `middlegarden_music_school.fbx.part-aa` + `part-ab` | 3.84 GB total | Middle Garden source model, split into 2 parts (GitHub 2 GB per-file limit) — **must be rejoined before use** |
| `undergarden_down.fbx` | 1.33 GB | Lower Garden source model |
| `uppergarden_up.png` / `undergarden_down.png` / `middlegarden_music_school.png` | 318 / 348 / 36 MB | Large UI map images used by the in-game minimap (NOT 3D material textures) |
| `props_bus_stop.fbx`, `props_siting_lantern.fbx`, `props_siting_streetlight.fbx`, `props_siting_sign.fbx`, `props_siting_rabbit.fbx` | ~255 MB total | Props placed in the scenes (bus stop, Sih-Ting/Muse college lantern, street light, sign, rabbit statue) |

Prop file mapping: 思廷 = Sih-Ting (Muse College). Original Chinese filenames are preserved in the local backup; ASCII names are used here for download compatibility.

## How to use

### Open in Blender (easiest)
Download a `.blend` file and open it. Done.

Or download a `.gltf` **and** its `.bin` into the same folder, then *File → Import → glTF 2.0*.

### Use in engines / simulators
- **Web / three.js**: glTF files work as-is (keep `.gltf` and `.bin` together).
- **Unreal / CARLA**: open the `.blend` in Blender, export binary FBX or USD.
- **Unity**: you can use the glTF via an importer package, or the original `.fbx` files (Unity reads ASCII FBX natively).
- **Isaac Sim**: import glTF, or export USD from Blender.

### Rejoin the split file
`middlegarden_music_school.fbx` was split into 2 parts. After downloading all parts into one folder:

Windows (cmd):
```bat
copy /b middlegarden_music_school.fbx.part-aa + middlegarden_music_school.fbx.part-ab middlegarden_music_school.fbx
```
macOS / Linux:
```bash
cat middlegarden_music_school.fbx.part-* > middlegarden_music_school.fbx
```

### Verify downloads
Compare against `CHECKSUMS.txt` in the repository root:
```bash
sha256sum uppergarden.bin
```

## Scene statistics (converted glTF)

| Scene | Mesh instances | Vertices | Triangles | Textures |
|---|---|---|---|---|
| Upper Garden | 3,343 | 19.1 M | 11.6 M | 156 |
| Middle Garden | 2,924 | 26.7 M | 10.6 M | 321 |
| Lower Garden | 5,625 | 9.0 M | 5.2 M | 415 |

## Important notes

- **Source FBX files are ASCII FBX 7.3** (an old text-based variant). Unity and Unreal import them, but **Blender cannot open them directly** — use the glTF/blend conversions instead.
- **Coordinate system**: converted from Unity's left-handed Y-up to glTF's right-handed Y-up (Z axis mirrored). Units are meters. Scene extents are roughly 1–3 km per garden, matching the real campus scale.
- **Middle Garden has no vertex normals** in the conversion (vertex count exceeded the export threshold). In Blender: select all meshes → *Mesh → Normals → Shade Smooth* (or Average) if the flat shading bothers you.
- **Object names and hierarchy are preserved** — every building, street light, vending machine etc. is individually selectable in Blender, so roads/buildings/vegetation can be separated easily for simulation work (e.g. building drivable areas for bicycle/bus agents).
- The original per-face texture files referenced inside the FBX (`Documents\*.jpg` on the model author's machine) are lost; the textures embedded in these exports are the ones actually used by the old project, so this is the final visual state of the models.
- Known duplicate: `Assets/pictures/Up.fbx` in the old project is a byte-identical copy of `Assets/pictures/Scenes/Up.fbx`; only one copy is archived here.

## Provenance

- Extracted 2026-10-04 from Unity project `aicuhk` (Unity 6000.2.10f1), scenes `uppergarden.unity`, `middlegarden.unity`, `undergarden.unity`.
- Export pipeline: temporary Unity editor script (batch mode) → glTF 2.0 with embedded textures; verified headlessly in Blender 5.0 (all textures load, geometry counts match); previews rendered with Blender workbench engine.
- Model copyright belongs to the original student team of the virtual campus project. This repository is **private** and for internal research/educational use only.
