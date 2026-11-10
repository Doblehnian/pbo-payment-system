
from core.notifiers import TelegramNotifier
from core.protocols import Notifier

from core.notifiers import TelegramNotifier
from core.protocols import Notifier
from core.processor import PaymentProcessor

telegram = TelegramNotifier()

print(isinstance(telegram, Notifier))

telegram.kirim(
    "mahasiswa@utr.ac.id",
    "Pembayaran berhasil!"
)

pemroses = PaymentProcessor(telegram)

print("TelegramNotifier berhasil digunakan!")


telegram = TelegramNotifier()

print(isinstance(telegram, Notifier))

telegram.kirim(
    "mahasiswa@utr.ac.id",
    "Pembayaran berhasil!"
)
