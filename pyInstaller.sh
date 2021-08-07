wget https://github.com/pyinstaller/pyinstaller/releases/download/v3.1/PyInstaller-3.1.tar.gz
tar -zxf PyInstaller-3.1.tar.gz
cd PyInstaller-3.1
sudo ln -s $PWD/pyinstaller.py /usr/bin/
pyinstaller.py -h | less
