from datetime import datetime, timedelta
from core.base import PaymentMethod, PembayaranGagal
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("virtual_account")
class VirtualAccount(PaymentMethod):
    def __init__(self, nomor_va: str = "888801234567", bank: str = "BNI", durasi_jam: int = 24):
        super().__init__(f"Virtual Account {bank} ({nomor_va})")
        self.nomor_va = nomor_va
        self.bank = bank
        self.status = "menunggu"
        self.batas_waktu = datetime.now() + timedelta(hours=durasi_jam)

    def validasi(self, jumlah: float) -> bool:
        if datetime.now() > self.batas_waktu:
            self.status = "kadaluwarsa"
            return False
        return jumlah > 0

    def bayar(self, jumlah: float) -> str:
        if self.status == "kadaluwarsa":
            raise PembayaranGagal("Virtual Account sudah kadaluwarsa")
        self.status = "berhasil"
        return buat_id("VA")

    def biaya_admin(self, jumlah: float) -> float:
        # Contoh: biaya admin Virtual Account sebesar Rp4.000
        return 4_000.0