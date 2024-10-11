from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy',
    ],
    description='A simple image processing package',
    author='Antonio Araújo',
    author_email='antonioaraujolb@gmail.com',
    url='https://github.com/antonioaraujoseginfo/projeto-pacote-processamento-imagens-python.py.git',
    
    python_requires='>=3.6',
)