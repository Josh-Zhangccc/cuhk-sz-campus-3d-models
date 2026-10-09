---
name: Bug report
about: Report a problem with a release asset, a 3D scene, or a Blender tool script
title: ''
labels: bug
assignees: ''
---

**Area**

- [ ] Release download / file corruption (checksum mismatch, split-file rejoin, 404)
- [ ] 3D scene content (missing/wrong geometry, placement, textures)
- [ ] Props (bus stop, lantern, streetlight, sign, rabbit)
- [ ] Blender tool scripts (`tools/`)
- [ ] Documentation / README

**Scene(s) affected**

- [ ] Upper Garden (`uppergarden`)
- [ ] Middle Garden (`middlegarden`)
- [ ] Lower Garden (`undergarden`)
- [ ] Props
- [ ] N/A

**Describe the bug**

A clear and concise description of what is wrong and what you expected instead.

**To reproduce**

Steps to reproduce the behavior, e.g.:

1. Downloaded `uppergarden.blend` (v1.0 release)
2. Opened in Blender 4.x
3. Saw ... near ...

**Environment**

- Format used: `.blend` / `.gltf` + `.bin` / source `.fbx`
- Viewer / engine + version (e.g. Blender 4.2, three.js r170, Unity 2022.3, CARLA, Isaac Sim)
- OS:

**Checksum (download issues only)**

Output of `sha256sum <file>` and the expected value from `CHECKSUMS.txt`:

```
```

**Screenshots / context**

If applicable, add screenshots or the exact error message.
