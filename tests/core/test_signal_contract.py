import pytest
from text_curation.core.signals import Signal

def test_signal_is_immutable():
    sig = Signal("test.signal", True)

    with pytest.raises(TypeError):
        sig.name = "evil"

    with pytest.raises(TypeError):
        sig.value = False


def test_signal_repr_is_stable_and_informative():
    sig = Signal("example.signal", 123)
    rep = repr(sig)

    assert "example.signal" in rep
    assert "123" in rep

def test_signal_has_no_extra_attributes():
    sig = Signal("test.signal", True)

    with pytest.raises(AttributeError):
        sig.extra = "nope"