from setuptools import setup, find_packages

def load_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="Simple-CLI",               # Your package/distribution name
    version="1.0.0",
    packages=find_packages(),         # This will find cli_tool and sub-packages
    include_package_data=True,        # To include non-code files specified in MANIFEST.in if any
    install_requires=load_requirements(),
    entry_points={
        "console_scripts": [
            "simple=cli_tool.cli:main",  # 'simple' CLI command calls main() in cli_tool/cli.py
        ],
    },
    author="Madhur Prakash",               # Optional: put your name or leave blank
    author_email="madhur.prakash2005@gmail.com",  # Optional
    description="Simple-CLI tool",       # Optional
    license="MIT",                   # Or your license type
    url="https://github.com/Madhur-Prakash/My-CLI.git",  # Optional: project homepage
)
