from ruleau import execute

from .rules import will_lend

if __name__ == "__main__":
    result = execute(will_lend, {"data": {"fico_score": 150, "ccjs": [], "kyc": "low"}})
