from Handler import Handler
from nickname import Name

#Add name_score to result
def score_result(result,person,name):
    best_score = float('inf')
    if 'aliases' in result:
        #Compare between aliases to find best match
        names = result['aliases']+[result['full_name']]
        for alias in names:
            alias = Name.parse(alias)
            score = name.compare(alias)
            if score < best_score:
                best_score = score
        result['name_score'] = best_score
    else:
        #Only one name
        result['name_score'] = name.compare(Name.parse(result['full_name']))

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Add metadata to familytree now data.')
    parser.add_argument("filename",type=str,help="Path to input json.")
    args = parser.parse_args()
    
    dataset = Handler(args.filename)
    dataset.addListener(score_result,'onResultBefore')
    dataset.startLoop(True)
    print("Done")
