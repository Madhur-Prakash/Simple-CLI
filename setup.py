from setuptools import setup, find_packages

def load_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="BuildBuddy",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements(),
    entry_points={
        "console_scripts": [
            "build=cli_tool.cli:main",
        ],
    },
)
