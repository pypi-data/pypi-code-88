"""
Runs a simple app for classification of text messages.

Will run on the web browser on a random port upon usage of the following
command-line entry:
    
    python -m spamdetection.app
    
Alternatively, running the following command will open an online version
hosted at https://nuveo-teste-ia.herokuapp.com/
    
    python -m spamdetection
"""

from pywebio import start_server
from pywebio.input import textarea, radio, actions
from pywebio.output import put_markdown, use_scope
import argparse
from spamdetection import SpamDetector
import spamdetection.params as params


@use_scope('scope1', clear=True)
def single_iteration():
    """Implements a single text classification iteration"""
        
    put_markdown('# Spam/Ham classification app')
    put_markdown('### This app demonstrates the use of a text message classification model')
    
    default = "These are not the droids you are looking for"
    user_input = textarea(label="Provide a message for classification",
                          placeholder='e.g.: ' + default,
                          help_text="PRO TIP: you can provide multiple messages separated by a semicolon")
    if user_input == "":
        user_input = default
    
    mode = radio("Choose the operating mode",
                  ["Aggressive", "Permissive"])
    
    input_list = user_input.split(';')
    input_list = [text.rstrip(' ').lstrip(' ') for text in input_list]
    probs = detector.prob_spam(input_list)
    
    if mode == "Aggressive":
        threshold = params.AGGRESSIVE_THRESHOLD
    elif mode == "Permissive":
        threshold = params.PERMISSIVE_THRESHOLD
    
    for msg, prob in zip(input_list, probs):
        if prob > threshold:
            label = 'spam'
        else:
            label = 'ham'
            prob = 1-prob
        output = '#### message ___"{}"___ classified as ___"{}"___ with probability ___"{}"___'.format(msg, label, prob)
        put_markdown(output)

    actions('Start over?', ['Confirm'])


def multiple_iterations(n_iterations = 100):
    """Implements multiple text classification iterations"""

    for _ in range(n_iterations):
        single_iteration()
 

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("-l", "--locale", type=str, default="local")
    args = parser.parse_args()
        
    detector = SpamDetector()
      
    if args.locale == "local":
        multiple_iterations()
    else:
        start_server(multiple_iterations, port=args.port)