# signals.py

from django.core.signals import request_finished
from django.db.models.signals import post_delete, post_save, pre_save
import signal
import sys

def signal_handler(signal, frame):
    print("\nHello, World!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
