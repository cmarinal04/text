from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    # Abre la imagen usando Pillow
    image = Image.open(image_path)

    # Utiliza Tesseract para extraer texto
    text = pytesseract.image_to_string(image)

    return text

def save_text_to_file(text, output_file):
    # Guarda el texto en un archivo plano
    with open(output_file, 'w') as file:
        file.write(text)

if __name__ == "__main__":
    # Ruta de la imagen que quieres procesar
    image_path = 'imagen2.png'

    # Extrae texto de la imagen
    extracted_text = extract_text_from_image(image_path)

    # Ruta del archivo en el que se guardará el texto
    output_file = 'texto_extraido.txt'

    # Guarda el texto en el archivo plano
    save_text_to_file(extracted_text, output_file)

    print(f"Texto extraído y guardado en '{output_file}'")
