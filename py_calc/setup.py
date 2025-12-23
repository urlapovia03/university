from setuptools import setup, find_packages

setup(
    name="pyCalc",                     # имя пакета (уникальное)
    version="1.0.0",                       # версия
    author="Ivan Urlapov",                     # автор
    author_email="urlapovivan03@gmail.com",
    description="Учебный пакет с математическими функциями",
    long_description=open("README.md", encoding="utf-8").read() if open else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/calculator",  # опционально
    packages=find_packages(),              # автоматически находит все пакеты
    python_requires=">=3.8",               # минимальная версия Python
    license="MIT",
    classifiers=[                          # метаданные для PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
