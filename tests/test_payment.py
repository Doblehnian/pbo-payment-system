import pytest
from core.base import PaymentMethod
from core.registry import buat_metode, daftar_plugin
from plugins import muat_semua_plugin


def test_abc_instantiation_failure() -> None:
    """Memastikan ABC PaymentMethod tidak dapat diinstansiasi langsung."""
    with pytest.raises(TypeError):
        PaymentMethod("uji_abstrak")  # type: ignore[abstract]


def test_unknown_plugin_raises_key_error() -> None:
    """Memastikan pemanggilan plugin tak dikenal memunculkan KeyError."""
    muat_semua_plugin()
    with pytest.raises(KeyError):
        buat_metode("plugin_ngawur_xyz", jumlah=50_000)


def test_virtual_account_plugin() -> None:
    """Menguji fungsionalitas dan status awal plugin VirtualAccount."""
    muat_semua_plugin()
    if "virtual_account" in daftar_plugin():
        va = buat_metode("virtual_account", nomor_va="99998888", bank="Mandiri")
        assert va.status == "menunggu"
        
        # Proses pembayaran valid
        trx_id = va.proses(150_000)
        assert trx_id.startswith("VA-")
        assert va.status == "berhasil"