from setuptools import find_packages, setup
import sys
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

version ="1.0.0"
if sys.version_info < (3, 7):
    raise RuntimeError("Plserver" + version +  "Requires Python 3.7+") 
setup(
    name="plserver",
    packages=find_packages(),
    version=version,
    author="Opeyemi Ogunsanya",
    author_email="ogunsanyaopeyemi4@gmail.com", 
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Python Live Server - For instant render on broswer while editing html, css, js.",
    long_description = long_description,
    license ='MIT',
    long_description_content_type = "text/markdown",
    install_requires=["aiohttp"],
    url = "https://github.com/o-opeyemi/plserver",
    project_urls = {
        "Homepage" : "https://github.com/o-opeyemi/plserver",
        "Tracker": "https://github.com/o-opeyemi/plserver/issues",
    },
    keywords=["plserver", "Python Live Server"],
    include_package_data=True,
    package_data={"":["websocket.js", "help.txt"]},
    package_dir={"plserver":"plserver"},
    zip_safe = False
    )