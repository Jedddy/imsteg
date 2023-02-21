import pytest

from imsteg import StegCodec


steg = StegCodec()
tmp_file = "a.png"


def test_image(tmp_path):
    steg.encode("tests/images/image1.png", "wassup haaha").save(str(tmp_path / tmp_file))
    assert steg.decode(str(tmp_path / "a.png")) == "wassup haaha"


def test_image2(tmp_path):
    steg.encode("tests/images/image2.jpg", "wassup haaha").save(str(tmp_path / tmp_file))
    assert steg.decode(str(tmp_path / "a.png")) == "wassup haaha"


def test_image3(tmp_path):
    steg.encode("tests/images/image3.jpg", "wassup haaha").save(str(tmp_path / tmp_file))
    assert steg.decode(str(tmp_path / "a.png")) == "wassup haaha"


def test_image4(tmp_path):
    with pytest.raises(ValueError) as excinfo:
        steg.encode("tests/images/image3.jpg", "awh" * 100).save(str(tmp_path / tmp_file))
        assert "The image is too small for the text!" in excinfo
