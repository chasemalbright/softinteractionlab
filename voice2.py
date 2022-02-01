import os

speak = "Hello world"

os.popen('espeak "' + speak + '" --stdout | aplay 2> /dev/null').read()