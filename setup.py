from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecocuivre_th/__init__.py
from ecocuivre_th import __version__ as version

setup(
	name="ecocuivre_th",
	version=version,
	description="theme for Ecocuivre",
	author="Ecocuivre",
	author_email="mail@mail.mail",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
