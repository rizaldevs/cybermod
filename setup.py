from setuptools import setup, find_packages

setup(
    name="cybermod",
    version="5.5.1",
    description="A monkeypatcher add-on for cybergram that does conversation handling",
    author="rizaldevs",
    author_email="rizaldaitona@gmail.com",
    packages=find_packages(),
    install_requires=["cybergram>=1.0"],
    python_requires=">=3.8",
)

