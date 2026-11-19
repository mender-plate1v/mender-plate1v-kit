# mender-plate1v-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m mender_plate1v_kit.cli --help
```

```python
from mender_plate1v_kit.core import MenderPlate1vTool

tool = MenderPlate1vTool()
print(tool)
```

## Layout

```
mender_plate1v_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 mender-plate1v
