# Caffeinate
Don't let your computer go to sleep while training your models

# Why would I need this?
Software engineering is more about thinking than typing. And it's very annoying when you're whiteboarding or just thinking and your work machine goes to sleep. Most of the times, we don't have admin access to change the settings so this helps prevent the computer from going to sleep.

# Installation
Using pip: 
```
pip install caffeinate
```

Using pip3:
```
pip3 install caffeinate
```

# Usage
| :memo:        | Tested on OSX and Windows       |
|---------------|:------------------------|

On windows, you might need to create a simple python file (code below) as path variable seems to be admin restricted. 

```
from caffeinate import caffeinate

caffeinate.run()
```

On Linux or Mac OSX, you can simply type ```awake``` in the terminal. 