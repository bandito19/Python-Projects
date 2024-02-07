import qrcode

class QR:
    def __init__(self, size, padding) -> None:
        self.qr = qrcode.QRCode(box_size=size, border=padding)


    def create_qr(self, file_name, fg, bg):
        user_input = input("Text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f"Successfully created {file_name}")
        except Exception as e:
            print(f"Error {e}")

def main():
    qr = QR(size=30, padding=2)
    qr.create_qr(file_name="qr.png", fg='white', bg='black')

if __name__=="__main__":
    main()