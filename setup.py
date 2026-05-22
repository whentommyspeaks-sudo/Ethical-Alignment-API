"""Setup.py for PyPI distribution"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ethical-alignment-api",
    version="2.0.0",
    author="whentommyspeaks-sudo",
    author_email="when.tommy.speaks@gmail.com",
    description="AI Red Letter Ethical Guardrail - Machine-readable ethics for AI systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
        "aws": [
            "boto3>=1.26.0",
        ],
        "langchain": [
            "langchain>=0.0.200",
        ],
    },
    keywords="AI ethics alignment safety guardrail ethical-ai responsible-ai",
    project_urls={
        "Bug Reports": "https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API/issues",
        "Source": "https://github.com/whentommyspeaks-sudo/Ethical-Alignment-API",
        "Documentation": "https://ethicalalignment.io/docs",
    },
)
