from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(name ="ucprotect3",
          description="Esta es una aplicacion para descargar level 3 de ucprotect",
          license="MIT",
          url="https://github.com/raulengineer/paquete.git",
          version="0.0.1",
          author="Raul Villano Obregon",
          author_email="raulengineer@gmail.com",
          long_description=open('README.md').read(),
          packages=find_packages(),
          zip_safe=False,
          install_requires=["pandas","Beautifulsoup4","selenium","lxml"],
        classifiers=[    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",]
          )