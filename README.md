Docker Compose v1.29.2 rebuilt
==============
[Docker Compose v1.29.2](https://github.com/docker/compose/releases/tag/1.29.2) rebuilt from source codes without compiling Python code inside of self decompressing executable.

Solves challenge where anti-virus, etc breaks decompress process and makes `docker-compose` commands unreliable.

### Why Python 3.9.0 ?
With [PyInstaller Extractor](https://github.com/extremecoders-re/pyinstxtractor) it is possible to extract original `docker-compose-Windows-x86_64.exe` binary and see that `python39.dll` internal version number is `3.9.150.1013` which is same than is included to Python 3.9.0.
