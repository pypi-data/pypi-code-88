"""
This package implements the SpamDetector class, with methods for calculating
the probability and for binary classification of 'spam'/'ham' text messages.
    
The model has been trained externaly and provided as a pickled file 
containing a sklearn pipeline object.

Check the 
[package GitHub page](https://github.com/fabio-a-oliveira/nuveo-teste-ia/tree/main/02-SMSSpamDetection)
and the documentation for [spamdetection.SpamDetector](spamDetector.html) 
for details.
"""

from spamdetection.SpamDetector import SpamDetector        
import spamdetection.params as params