from pathlib import Path, PureWindowsPath

directory = Path('/home/mrrobot/Documents/PycharmProjects/PythonProject/Day6/test.txt')
print(directory.read_text())
print(directory.name)
print(directory.suffix)
print(directory.stem)

if not directory.exists():
    print('Directory does not exist')
else:
    print('Directory exists')

windows_path = PureWindowsPath(directory)
print(windows_path)
