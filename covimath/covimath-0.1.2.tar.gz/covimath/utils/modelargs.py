import sys
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    nargs = len(sys.argv)
    if nargs == 1:
        logger.info('No arguments supplied.')
        return None
    
    args = sys.argv[1:]
    
    firstarg = args[0].strip().lower()
    if firstarg in ['-h', '--help']:
        logger.info('Command help requested.')
        return 'usage'
    
    argdict = {}
    ints = ['N', 'E0', 'I0', 'R0', 'D0', 'tau'] 
    reals = ['lambda', 'beta', 'gamma', 'sigma', 'mu']
    
    for a in args:
        tokens = a.split('=')
        if len(tokens) == 1:
            t = tokens[0].strip()
            argdict[t] = None
        elif len(tokens) == 2:
            t0 = tokens[0].strip()
            t1 = tokens[1].strip()
            
            if t0 in ints:
                try:
                    v = int(t1)
                    argdict[t0] = v
                except ValueError:
                    msg = 'Argument ' + t0 + ' must be an integer.'
                    raise ValueError(msg)
                else:
                    if v < 0:
                        raise ValueError('Value for argument: ' + t0 + 
                                         ' should be non-negative')        
            elif t0 in reals:
                try:
                    v = float(t1)
                    argdict[t0] = v
                except ValueError:
                    msg = 'Argument ' + t0 + ' must be a float.'
                    raise ValueError(msg)
                else:
                    if v <= 0:
                        raise ValueError('Value for argument: ' + t0 + 
                                         ' should be positive')
            else:
                argdict[t0] = t1 # Just in case there are non-int non-float args
        else:
            raise ValueError('Invalid input: ', a)
            
    logger.info('Arguments: ' + str(argdict))
    return argdict