import tempfile

import qrcode

class CreateQrcode:

    def create(self, testo, file):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data(testo)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(tempfile.gettempdir() + '/' + file)
        return tempfile.gettempdir() + '/' + file
