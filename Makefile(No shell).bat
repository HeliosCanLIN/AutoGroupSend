rd /s /q .\build
rd /s /q .\__pycache__
del /s /q .\main.spec
pyinstaller -p "C:\Program Files\Python38\Lib\site-packages" -F main.py -w