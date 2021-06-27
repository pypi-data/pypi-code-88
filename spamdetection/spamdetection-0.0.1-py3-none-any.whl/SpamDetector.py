"""
Implements the SpamDetector class
"""

## Imports

import pickle
import os
import os.path
import spamdetection.params as params

## Variables used by various methods

# Path to the model file
MODEL_FILENAME = params.MODEL_FILENAME
MODEL_DIRECTORY = params.MODEL_DIRECTORY
MODEL_PATH = params.MODEL_PATH
    
# With this threshold, there are no false positives in the validation set
PERMISSIVE_THRESHOLD = params.PERMISSIVE_THRESHOLD
    
# With this threshold, there are no false negatives in the validation set
AGGRESSIVE_THRESHOLD = params.AGGRESSIVE_THRESHOLD

#------------------------------------------------------------------------------

class SpamDetector:
    """
    Class implementing the prob_spam() and is_spam() public methods for
    classification of text messages.
    
    Args:
        
        mode : (optional) used to determine whether the is_spam() method
                behaves in an "aggressive" (few false negatives) or
                "permissive" (few false positives) manner. Can be set during
                initialization or with call to __set_mode__().
               
    Attributes:
        
        model : a sklearn.pipeline.Pipeline object containing preprocessing
                steps and a random forest model for the classification of
                text messages in either 'spam' or 'ham'
                
        mode : stores choice of mode. Can either be None, "aggressive" or 1, 
                "permissive" or 2.
               
        threshold : float between 0 and 1, automatically selected from preset
                    values when the mode attribute is set.
    """
 
#------------------------------------------------------------------------------
    
    def __init__(self, mode=None):
        """
        Constructor method
        """
        
        # Verify that there is a model file in the designated folder
        
        msg = ("No file named {} found in directory {}".
               format(MODEL_FILENAME, MODEL_DIRECTORY))
        
        assert MODEL_FILENAME in os.listdir(MODEL_DIRECTORY), msg
        
        # Load the pickled model into the .model attribute
        with open(MODEL_PATH, 'rb') as model:
            self.model = pickle.load(model)
        
        # Set .mode attribute (if provided)
            
        if mode == None:
            self.mode = None
            self.threshold = None
        else:
            self.__set_mode__(mode)
   
#------------------------------------------------------------------------------
        
    def __set_mode__(self, mode):
        """Set mode attribute"""
        
        # Assert that mode is valid
        
        msg = "invalid value for mode argument, check docstring"
        assert mode in [None, "aggressive", 1, "permissive", 2], msg
        
        # Set mode and threshold attributes
        
        if mode in ["aggressive", 1]:
            self.mode = "aggressive"
            self.threshold = AGGRESSIVE_THRESHOLD
            
        elif mode in ["permissive", 2]:
            self.mode = "permissive"
            self.threshold = PERMISSIVE_THRESHOLD

#------------------------------------------------------------------------------
        
    def prob_spam(self, X):        
        """
        Determines the probability (or list of probabilities) that message
        (or list of messages) is classified as 'spam'
        
        Args:
            
            X : either a string or list of strings for which classification
                is desired
            
        Returns:
            
            Either float or list of floats in the [0,1] interval,
            indicating the probability that each message in X is
            classified as 'spam'
        """
        
        # Simple assertion of args types

        msg = "X must be either a string or a list of strings"
        assert isinstance(X, (str, list)), msg
        
        msg = "All elements of X must be of type str"
        if isinstance(X, list):
            assert all([isinstance(element, str) for element in X]), msg
        
        
        # Make predictions
        
        # if X is type str, pass it inside a list,
        # otherwise, pass it directly
        
        if isinstance(X, str):
            prediction = self.model.predict_proba([X])
            return prediction[0][1]
        else:
            prediction = self.model.predict_proba(X)
            return [prob[1] for prob in prediction]
        

#------------------------------------------------------------------------------
    
    def is_spam(self, X, mode=None):
        """
        Determines whether message (or list of messages) is 
        classified as 'spam'
        
        Args:
            
            X : either a string or list of strings for which classification
                is desired
                
            mode : - determines mode of operation
                        - "aggressive" or 1 uses low threshold for spam label, 
                        with priority set to a very low False Negative rate,
                        possibly some ham will be misclassified as spam
                        - "permissive" or 2 uses high threshold for spam label,
                        with priority set to a very low False Positive rate,
                        possibly some spam will be misclassified as ham
                   - Valid values: None, "aggressive", 1, "permissive", 2
                   - if None, self.mode will be used (if available), or set
                   to "permissive" (if unavailable)
                   - if set to either "aggressive", 1, "permissive", 2, 
                   the method will operate in this mode but will not
                   alter the mode attribute value
            
        Returns:
            
            Either a boolean or list of booleans (according to shape of X)
            indicating spam (True) or ham (False)
        """
        
        # Check validity of mode argument
        # (X is evaluated by prob_spam() method)
        
        msg = "invalid value for mode argument, check docstring"
        assert mode in [None, "aggressive", 1, "permissive", 2], msg
        
        
        ## Get the operation mode and threshold
        ## used for this call to the is_spam() method
        
        # called with aggressive mode, will ignore attribute
        if mode in ["aggressive", 1]:
            use_mode = "aggressive"
            use_threshold = AGGRESSIVE_THRESHOLD
        
        # called with permissive mode, will ignore attribute
        elif mode in ["permissive", 2]:
            use_mode = "permissive"
            use_threshold = PERMISSIVE_THRESHOLD
        
        # called without explicit choice, will use attribute if available
        elif self.mode in ["aggressive", 1, "permissive", 2]:
            use_mode = self.mode
            use_threshold = self.threshold
        
        # called without explicit choice and attribute is not set,
        # will use permissive mode
        else:
            use_mode = "permissive"
            use_threshold = PERMISSIVE_THRESHOLD
        
        ## Get class probabilities
        
        probs = self.prob_spam(X)
        
        ## Compare probability with selected threshold and decide
        ## whether spam or ham
        
        # when X is a single string
        if isinstance(X, str):
            
            if probs > use_threshold:
                return True
            else:
                return False
        
        # when X is a list of strings
        # (detailed validation in prob_spam() method)
        else:
            return [True if prob > use_threshold else False for prob in probs]
        
#------------------------------------------------------------------------------        
        
    def print_classification(self, message, mode="permissive"):
        """
        Prints classification and probability for a single message.
        Used when running package from command-line.
        
        Args:
            
            message (str) : single message for classification
            
            mode : (optional) "permissive" or 2 (default) prioritizes low False
                   Positive rates. "aggressive" or 1 prioritizes low False
                   Negative rates.
        
        Returns:
            
            None
        """
        
        # Assert validity of args
        
        msg = "message must be a string when using module as script"
        assert isinstance(message, str), msg
        
        msg = "mode must be either 'aggressive', 1, 'permissive' or 2"
        assert mode in ["aggressive", 1, "permissive", 2], msg
        
        # Determine which cutoff threshold to use
        
        if mode in ["permissive", 2]:
            use_threshold = PERMISSIVE_THRESHOLD
            
        elif mode in ["aggressive", 1]:
            use_threshold = AGGRESSIVE_THRESHOLD    
        
        # Create object of class SpamDetector with designated mode,
        # get 'spam' probability and classify message
        
        detector = SpamDetector(mode)
        
        probability_spam = detector.prob_spam(message)
        
        if probability_spam > use_threshold:
            label = 'spam'
            probability = probability_spam
        else:
            label = 'ham'
            probability = 1 - probability_spam
            
        # print result
        
        print(f"Message is classified as '{label}' " +
              f"with probability {probability}" +
              "\n\n")