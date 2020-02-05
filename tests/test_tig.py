import os

from transparent_image_generator import tig, tig_data_url


def test_tig():
    with open(os.path.join(os.path.dirname(__file__), '1x1.png'), 'rb') as f:
        assert f.read() == tig(1, 1)


def test_tig_data_url():
    assert 'data:image/png;base64,' \
           'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEX' \
           '///+nxBvIAAAAAXRSTlMAQObYZgAAAApJREFUeNpjYAAAAAIAAeUn3vwAAAAASUVORK5CYII=' \
           == tig_data_url(1, 1)
