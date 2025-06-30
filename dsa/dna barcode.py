import qrcode
import json
from PIL import Image
from pyzbar.pyzbar import decode

def generate_barcode(species, dna_sequence, sample_id, gene, filename='barcode.png'):
    metadata = {
        generate_barcode(
    species='Homo sapiens',
    dna_sequence='ATCGTACGATCGATCGATGCTAGCTAGCTAGC',
    sample_id='HS-001',
    gene='COI'
)

# To decode later:
# decode_barcode('barcode.png')
    }
    json_data = json.dumps(metadata)

    qr = qrcode.QRCode(version=2, box_size=10, border=4)
    qr.add_data(json_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code saved as {filename}")

def decode_barcode(filename='barcode.png'):
    img = Image.open(filename)
    decoded = decode(img)
    if decoded:
        data = decoded[0].data.decode('utf-8')
        metadata = json.loads(data)
        print("Decoded Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
        return metadata
    else:
        print("No QR code detected.")
        return None