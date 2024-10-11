# Image Processor

Um pacote simples para processamento de imagens em Python. Permite aplicar filtros, redimensionar e realizar outras manipulações de imagens de forma fácil e eficiente.

## Funcionalidades

- Aplicação de filtros básicos (blur, contorno, etc.)
- Redimensionamento de imagens
- Suporte para formatos de imagem comuns (JPEG, PNG, etc.)
- Filtros personalizados (em desenvolvimento)

## Instalação

Para instalar o pacote, utilize o `pip`:

```bash
pip install image_processor
Uso
Aplicando Filtros
python

from image_processor import apply_filter

# Aplicar um filtro de desfoque
filtered_image = apply_filter('caminho/para/imagem.jpg', 'BLUR')
filtered_image.save('caminho/para/imagem_filtrada.jpg')
Redimensionando Imagens
python

Copiar
from image_processor import resize_image

# Redimensionar a imagem para 200x200 pixels
resized_image = resize_image('caminho/para/imagem.jpg', 200, 200)
resized_image.save('caminho/para/imagem_redimensionada.jpg')
Testes
Para executar os testes unitários, use:

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

Contato
Para mais informações, entre em contato:

Nome: Antonio Araujo
Email: antonioaraujolb@gmail.com
GitHub: github.com/antonioaraujoseginfo