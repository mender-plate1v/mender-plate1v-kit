import tempfile
from pathlib import Path

from mender_plate1v_kit.core import MenderPlate1vTool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert MenderPlate1vTool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = MenderPlate1vTool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = MenderPlate1vTool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
