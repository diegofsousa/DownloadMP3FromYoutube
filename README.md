This is a simple code to download videos from youtube to mp3 from a search.
The project interface was produced with PyQt4 and business rules were produced with the beautifulsoup4 and youtube-dl libraries.

Step by Step to Install:

First of all, have pip and virtualenv installed.

1. Create a virtualenv for the project by prescribing Python 2:<br>
```virtualenv --python = python2 [environment name]```

2. Enter the virtualenv folder and activate it:<br>
```source bin/activate```

3. Make the clone or download the project into the part of the newly created virtualenv, 
create a folder called "app" and put the repository files in it.

4. In the virtualenv root create a "build" folder, download the SIP and PyQt4 modules. Once done, extract them into the folder:<br>
PyQt4: https://www.riverbankcomputing.com/software/pyqt/download<br>
SIP: https://pypi.python.org/pypi/SIP#downloads<br>

5. Install some prerequisites:<br>
```sudo apt-get install python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential```

6. Go to "build/SIP" directory:<br>
```python configure.py``` <br>
```make``` <br>
```sudo make install```

6. Go to "build/PyQt4" directory:<br>
```python configure.py``` <br>
```make``` <br>
```sudo make install```

8. Enter the "app" folder and install pip dependencies:<br>
```pip install requirements.txt -r.```

9. Still in the app folder run ```python gui.py```
