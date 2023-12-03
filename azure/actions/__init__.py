import time
from os import environ
from pprint import pprint

from kubiya import ActionStore, get_secret

actionstore = ActionStore("azure", "0.1.0")
