class GameTopUpSystem:
    def __init__(self):
        self.games = {
            "Mobile Legend": {"1234567890ABCDEFGHIJ": "Username1", "MNOPQRSTUV12345WXYZ": "Username2"},
            "Game B": {"54321KLMNOPQRSTU": "Username3", "9876543210ZYXWVUTSRQ": "Username4"},
        }
        self.wallet_balance = 1000  
        self.transaction_history = []

    def top_up_game(self):
        print("Selamat datang di sistem top up game.")
        while True:
            game_choice = input("Pilih game yang ingin Anda top up: ")
            if game_choice in self.games:
                user_id = input("Masukkan ID game atau akun game Anda: ")
                if user_id in self.games[game_choice]:
                    print("Metode pembayaran yang tersedia:")
                    print("1. E-wallet")
                    payment_method = input("Pilih metode pembayaran: ")
                    if payment_method == "1":
                        success = self.e_wallet_payment()
                        if success:
                            print("Top up berhasil. Saldo telah ditambahkan.")
                            self.transaction_history.append(f"Top up game {game_choice} sebesar X")
                            break
                        else:
                            print("Pembayaran gagal. Silakan coba lagi atau hubungi customer service.")
                            retry = input("Coba lagi pembayaran (Y/N)? ")
                            if retry.lower() != "y":
                                break
                    else:
                        print("Metode pembayaran lain belum diimplementasikan.")
                else:
                    print("ID game atau akun tidak ditemukan. Silakan coba lagi.")
            else:
                print("Game tidak ditemukan. Silakan pilih game lain atau hubungi customer service.")

    def e_wallet_payment(self):
        amount = int(input("Masukkan nominal top up: "))
        if amount <= self.wallet_balance:
            self.wallet_balance -= amount
            return True
        else:
            print("Saldo E-wallet tidak mencukupi.")
            return False

    def display_transaction_history(self):
        print("Riwayat Transaksi:")
        for transaction in self.transaction_history:
            print(transaction)

top_up_system = GameTopUpSystem()

while True:
    top_up_system.top_up_game()
    view_history = input("Lihat riwayat transaksi (Y/N)? ")
    if view_history.lower() == "y":
        top_up_system.display_transaction_history()
    continue_shopping = input("Ingin melanjutkan berbelanja (Y/N)? ")
    if continue_shopping.lower() != "y":
        break

print("Terima kasih telah menggunakan sistem top up game.")