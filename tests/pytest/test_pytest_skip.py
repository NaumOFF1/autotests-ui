import pytest


# Указываем маркировку, которая пропустит данный автотест
@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    pass
