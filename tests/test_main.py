import pytest
from weiver.utils.func import reverse_list_v0


def test_zero_dil():
    assert pytest.raises(func(5, 0))


def test_reverse_list_v0():
    assert reverse_list_v0(5) == [5, 4, 3, 2, 1, 0]
