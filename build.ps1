$ErrorActionPreference = "Stop"

$env:PATH="C:\Python39;$($env:PATH)"

if ($(python --version) -ne "Python 3.9.0") {
  throw "Python 3.9.0 is required to run this script. Please install it and try again."
}
if (Test-Path venv) {
  throw "Folder venv already exists. Please remove it and try again."
}

cd $PSScriptRoot
python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
pip install -r requirements-build.txt

pyinstaller --clean docker-compose.spec --onedir
