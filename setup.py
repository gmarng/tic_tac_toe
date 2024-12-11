from setuptools import setup, find_packages

setup(
    name="jogovelha",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Gabriel Henrique Marengoni",
    author_email="marengoni.gabriel@escola.pr.gov.br",
    description="Um pacote de jogo da velha",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)