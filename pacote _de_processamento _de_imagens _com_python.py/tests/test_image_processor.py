import unittest
from image_processor import apply_filter, resize_image
from PIL import Image
import os

class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        # Configurações iniciais, como o caminho da imagem de teste
        self.test_image_path = 'test_images/test_image.jpg'
        self.output_image_path = 'test_images/output_image.jpg'

    def test_apply_filter_blur(self):
        result = apply_filter(self.test_image_path, 'BLUR')
        self.assertIsInstance(result, Image.Image)  # Verifica se o resultado é uma imagem
        result.save(self.output_image_path)  # Salva a imagem para verificação manual se necessário

    def test_resize_image(self):
        result = resize_image(self.test_image_path, 100, 100)
        self.assertEqual(result.size, (100, 100))  # Verifica se o tamanho da imagem está correto
        result.save(self.output_image_path)  # Salva a imagem para verificação manual

    def tearDown(self):
        # Limpa os arquivos de saída após os testes
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

if __name__ == '__main__':
    unittest.main()