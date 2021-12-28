# Template

## How to create / install the virtual enviroment
In order to have the same enviroment ...a shell script which will install the necessary tools on a debian based enviroment
```bash 
installEnv.sh
```
## How to activate the virtual enviroment
For running the script without docker...ensure to activate the enviroment prior starting the script.
```bash 
source venv/bin/activate
./start.py
```

## How to deactivate the virtual enviroment
in the active terminal where the venv enviroment is active...
```bash 
deactivate 
```

## How to install packages using pip
In order to install additional packages with pip...please make sure that the venv is active and 
install for exampel flask this way....do not forget to save the new model with the pip freeze command...
```bash 
source venv/bin/activate
pip install flask
```
## How to check which packages are installed 
in order to show what is currently installed use the pip list command..if the new package is not visible there...then check the file permissions and if the venv is active...
```bash 
pip list
Package       Version
------------- -------
paho-mqtt     1.5.1  
pip           18.1   
pkg-resources 0.0.0  
setuptools    40.8.0 
```

## How to save the current installed packages to a requirement file
```bash 
pip freeze > requirements.txt
```


