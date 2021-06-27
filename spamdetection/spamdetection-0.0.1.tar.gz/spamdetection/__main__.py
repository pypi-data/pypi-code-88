"""
Should be run from terminal using one of these options:
    
To open a web browser with the classification app:
    
    python -m spamdetection
    
To print the classification and probability for a given message:
    
    python -m spamdetection {message}
    
        OR
    
    python -m spamdetection {message} {mode}

If mode is not informed, defaults to "permissive"
"""

# imports

import spamdetection
import spamdetection.params as params
import sys
import webbrowser

# main() function
def main():
    """Provide simple command-line interface"""
    
    if len(sys.argv) == 1:
        # open browser with web app
        url = params.WEB_APP_URL
        print("Opening app with web browser... ", end='')
        
        try:
            webbrowser.open_new(url)
            print("ok")
        except:
            print("failed")
            raise RuntimeError("failed to open web app")
        
    elif len(sys.argv) == 2:
        # print classification results to console
        message = sys.argv[1]
        detector = spamdetection.SpamDetector()
        detector.print_classification(message)
        
    else:
        # print classification results to console
        message = sys.argv[1]
        mode = sys.argv[2]
        detector = spamdetection.SpamDetector()
        detector.print_classification(message, mode)
    
    
# call the main() function with proper args

if __name__ == '__main__':
    main()

    