from fuzzywuzzy import fuzz, process
import re
import statistics
import sys

def findRegex(pattern,currentLine):
    para=currentLine['LineText']
    bbox=currentLine["Words"][0]["bbox"]
    conf=currentLine["Words"][0]["confidence"]
    text=""
    regex = re.compile(pattern)
    match = regex.findall(para)
    if len(match)!=0:
        if len(match[0])>1:
            text="".join(match[0])
        else:
            text=match[0]
    return text,bbox,conf

# function to convert ocr json to required json
def convert_json(data):
    response = data
    confidence_dict = {}
    for i in range(len(response["responses"][0]["fullTextAnnotation"]["pages"][0]["blocks"])):
        response_2 = response["responses"][0]["fullTextAnnotation"]["pages"][0]["blocks"][i]["paragraphs"]
        for j in range(len(response_2)):
            response_3 = response["responses"][0]["fullTextAnnotation"]["pages"][0]["blocks"][i]["paragraphs"][j][
                "words"]
            for k in range(len(response_3)):
                response_4 = response_3[k]
                for l in range(len(response_4)):
                    # print(l)
                    # print(response_4.keys())
                    # word_text = ''.join([symbol.text for symbol in word.symbols])
                    word_text = ''.join([response_4["symbols"][m]["text"] for m in range(len(response_4["symbols"]))])
                    confidence_dict[word_text] = response_4["confidence"]

    texts = data["responses"]
    texts = texts[0]["textAnnotations"]
    dic = {"texts": []}
    tex = []
    for text in texts:
        vert = []
        for vertex in text["boundingPoly"]["vertices"]:
            try:
                vert.append(vertex["x"])
            except:
                vert.append(int(0))
            try:
                vert.append(vertex["y"])
            except:
                vert.append(int(0))

        if str(text["description"]) in confidence_dict.keys():
            tex.append({
                "text": text["description"],
                "bbox": vert,
                "confidence": confidence_dict[text["description"]]

            })
        else:
            tex.append({
                "text": text["description"],
                "bbox": vert,
                "confidence": 0

            })

    dic["texts"] = tex
    return dic

# left and right are list ["word","Wratio Value"]
def generic_finder(rule,data,left=None,right=None):
    regex = re.compile(rule)
    words_string = data["texts"][1:]
    answer = []
    for i in range(0,len(words_string),1):
        match = regex.findall(words_string[i]["text"])
        if(len(match)>0):
            x1,y1,x3,y3 =extractor_x_y(words_string[i]["bbox"])
            cord = [x1,y1,x3,y3]
            cords = [x1,y1,x3-x1,y3-y1]
            text = words_string[i]["text"]
            conf = words_string[i]["confidence"]
            
            # getting extremes of the page 
            # leftmost_x1 , right_most_x3 , top_most_y1 , bottom_most_y3
            left_extreme ,right_extreme , top_extreme , bottom_extreme  = finding_extremes(data)
            text_right,score_right,co_ordinates_right = vicinity_check(cord , 0, right_extreme-x3 , 0 , 0 , "RIGHT" , data)
            text_left,score_left,co_ordinates_left = vicinity_check(cord , x1-left_extreme , 0 , 0 , 0 , "LEFT" , data)
            
            ## it will throw all the regex matches
            if left==None and right==None:
                answer.append({"value":text,"bbox":cords,"score":conf,"text_left":text_left,"cord_left":co_ordinates_left,"text_right":text_right,"cord_right":co_ordinates_right})

            ## will throw all the regex matches with fuzzy match with the right side text that u passed    
            elif left==None and right!=None:
                word_exp = right[0] # getting word
                rat_exp = right[1] # getting ratio
                
                rat = fuzz.WRatio(word_exp,text_right)
                
                if rat>=rat_exp:
                    answer.append({"value":text,"bbox":cords,"score":conf,"text_left":text_left,"cord_left":co_ordinates_left,"text_right":text_right,"cord_right":co_ordinates_right})

            ## will throw all the regex matches with fuzzy match with the left side text that u passed          
            elif left!=None and right==None:
                word_exp = left[0] # getting word
                rat_exp = left[1] # getting ratio
                
                rat = fuzz.WRatio(word_exp,text_left)
                
                if rat>=rat_exp:
                    answer.append({"value":text,"bbox":cords,"score":conf,"text_left":text_left,"cord_left":co_ordinates_left,"text_right":text_right,"cord_right":co_ordinates_right})
                    
    return answer  

def GenerateRatios(data, xDiff, yDiff):
    x1_min, x3_max, y1_min, y3_max = finding_extremes(data)
    x_image = x3_max - x1_min
    y_image = y3_max - y1_min
    x_ratio = xDiff / x_image
    y_ratio = yDiff / y_image

    return x_ratio, y_ratio

##### cordinates as the reference , left shift , right shift , top shift , bottom shift
# allows to look near by entities
def vicinity_check(cords, flex_hor_left, flex_hor_right, flex_ver_top, flex_ver_bott, dirc, data):
    if len(cords) != 0:
        # getting x1,y1,x3,y3
        x1, y1, x3, y3 = cords[0], cords[1], cords[2], cords[3]
        # checking for left look
        if dirc == "LEFT":
            flex_hor_right = 0
            x1_check_left = x1 - flex_hor_left
            y1_check_left = y1 - flex_ver_top
            x3_check_left = x1
            y3_check_left = y3 + flex_ver_bott
            co_ordinates_check = [x1_check_left, y1_check_left, x3_check_left - x1_check_left,
                                  y3_check_left - y1_check_left]

            text, score = compare(co_ordinates_check, data)


        # checking for right look
        elif dirc == "RIGHT":
            flex_hor_left = 0
            x1_check_right = x3
            y1_check_right = y1 - flex_ver_top
            x3_check_right = x3 + flex_hor_right
            y3_check_right = y3 + flex_ver_bott
            co_ordinates_check = [x1_check_right, y1_check_right, x3_check_right - x1_check_right,
                                  y3_check_right - y1_check_right]
            text, score = compare(co_ordinates_check, data)


        # checking for top look
        elif dirc == "TOP":
            flex_ver_bott = 0
            x1_check_top = x1 - flex_hor_left
            y1_check_top = y1 - flex_ver_top
            x3_check_top = x3 + flex_hor_right
            y3_check_top = y1
            co_ordinates_check = [x1_check_top, y1_check_top, x3_check_top - x1_check_top, y3_check_top - y1_check_top]
            text, score = compare(co_ordinates_check, data)


        # checking for bottom look
        elif dirc == "BOTTOM":
            flex_ver_top = 0
            x1_check_bott = x1 - flex_hor_left
            y1_check_bott = y3
            x3_check_bott = x3 + flex_hor_right
            y3_check_bott = y3 + flex_ver_bott
            co_ordinates_check = [x1_check_bott, y1_check_bott, x3_check_bott - x1_check_bott,
                                  y3_check_bott - y1_check_bott]
            text, score = compare(co_ordinates_check, data)

        return text, score, co_ordinates_check  # returning text , score and cords for that box

### formatting the bbox
def cords_formatter(cords):
    x1 = cords[0]
    y1 = cords[1]
    w = cords[2]
    h = cords[3]

    x2 = x1 + w
    y2 = y1

    x4 = x2
    y4 = y2 + h

    x3 = x1
    y3 = y1 + h

    arr = [{"x": x1, "y": y1}, {"x": x2, "y": y2}, {"x": x4, "y": y4}, {"x": x3, "y": y3}]
    return arr

## returns the x1,y1,x3,y3 from the [x1,y1,x2,y2,x3,y3,x4,y4]
def extractor_x_y(coordinate_arr):
    if len(coordinate_arr) == 0:
        return "ZERO"
    x1 = coordinate_arr[0]
    y1 = coordinate_arr[1]
    # x2 = coordinate_arr[2]
    # y2 = coordinate_arr[3]
    x3 = coordinate_arr[4]
    y3 = coordinate_arr[5]
    # x4 = coordinate_arr[6]
    # y4 = coordinate_arr[7]
    return x1, y1, x3, y3


######################## finding co-ordinates based on the keyword #########################################
def parent_coordinate_finder(word, words_string):
    ay = []
    # looking into the list with words and co-ordinates
    for i in range(0, len(words_string), 1):
        ratio = fuzz.WRatio(word, words_string[i]["text"])
        len1 = len(word)
        len2 = len(words_string[i]["text"])
        # if the ratio is grater than 70 and length is same
        if words_string[i]["text"] == word or (ratio >= 70 and len1 == len2):
            ay.append(words_string[i]["bbox"])
    return ay


def extract_keys(key, inp, isList):
    ext = []
    if len(key.split()) == 1:
        ext = process.extractBests(key, [inp["texts"][i]["text"] for i in range(1, len(inp["texts"]))])
    elif len(key.split()) == 2:
        ext = process.extractBests(key,
                                   [inp["texts"][i]["text"] + " " + inp["texts"][i + 1]["text"] for i in
                                    range(1, len(inp["texts"]) - 1)])
    elif len(key.split()) == 3:
        ext = process.extractBests(key,
                                   [inp["texts"][i]["text"] + " " + inp["texts"][i + 1]["text"] + " " +
                                    inp["texts"][i + 2]["text"]
                                    for i in range(1, len(inp["texts"]) - 2)])

    words = [w[0] for w in ext]
    if isList:
        return words
    # match for extact word
    if key in words:
        return key
    else:
        if not words:
            return None
        score = [fuzz.ratio(key, k) for k in words]
        s = max(score)
        if s > 85:
            return words[score.index(s)]
        else:
            score = [fuzz.WRatio(key, k) for k in words]
            s = max(score)
            if s > 90:
                return words[score.index(s)]


# Concatenated words that are in the same line with a specified deviation
# row contains the words in a single line
# deviation is the maximum difference between 2 words
def ConcatRow(row, deviation):
    i = 0
    while (i <= len(row) - 2) & (len(row) != 1):
        row = SortWords(row, 0)
        firstDic = row[i]
        secondDic = row[i + 1]
        fBbox = firstDic['bbox']
        sBbox = secondDic['bbox']
        dif = sBbox[0] - fBbox[2]
        # if the diff between first and second word is less than the deviaton make it into one sentence
        if dif <= deviation:
            newWord = firstDic['text'] + " " + secondDic['text']
            newBbox = [fBbox[0], fBbox[1], sBbox[2], sBbox[3], sBbox[4], sBbox[5], fBbox[6], fBbox[7]]
            confidence = (firstDic['confidence'] + secondDic['confidence']) / 2
            row.pop(i)
            row.pop(i)
            row.append({
                'text': newWord,
                'bbox': newBbox,
                'confidence': confidence
            })
        else:
            i = i + 1
    return row


# Sorts the given words based on the specified axis
# 0 for X, 1 for Y
def SortWords(rowWords, axis):
    return sorted(rowWords, key=lambda i: i['bbox'][axis])


def LineOCR(data, deviation=22, lineDeviation=10):
    # Generates Line wise OCR data with the words and line sequence number
    wordAnnotations = data['texts'][1:]
    lineOCR = []
    lineNo = 1

    # gets all the unique Y coordinate values
    yCoords = []
    for i in wordAnnotations:
        if i['bbox'][1] not in yCoords:
            yCoords.append(i['bbox'][1])
    # sorting the Y coords
    yCoords.sort()

    words = []
    lineText = ""

    # Grouping all the words with same Y axis and less than the lineDeviation specified
    for k in range(0, len(yCoords)):
        for i in wordAnnotations:
            if i['bbox'][1] == yCoords[k]:
                words.append(i)

        if (k == len(yCoords) - 1) or (abs(yCoords[k] - yCoords[k + 1]) > lineDeviation):
            words = SortWords(words, 0)
            for j in words:
                lineText = lineText + " " + j['text']

            # LineOCR format
            lineOCR.append({
                'LineNumber': lineNo,
                'LineText': lineText,
                'Words': words,
                'ConcatWords': ConcatRow(words, deviation)
            })
            lineNo = lineNo + 1
            words = []
            lineText = ""

    return lineOCR


def GetText(keys, lineData, xDistance, yDistance, data):
    # Takes the reference bbox of the last key in keys
    textbbox = []
    bbox = []
    text = ""
    lineWords = lineData['Words']
    numberOfKeys = len(keys)
    for i in range(0, len(lineWords) - numberOfKeys + 1):
        keyList = []
        for k in range(0, numberOfKeys):
            keyList.append(lineWords[i + k]['text'])
        if keyList == keys:
            bbox = lineWords[i + numberOfKeys - 1]['bbox']
    #print(f"bbox: {bbox}")
    if not bbox:
        return "", [], 0.00

    texts = {
        'text': "",
        'bbox': [],
        'confidence': 0.00
    }

    if xDistance[0] == 0:
        x1 = bbox[2]
    else:
        x1 = xDistance[0]

    if xDistance[1] == 0:
        x2 = bbox[2] + 4000
    else:
        x2 = xDistance[1]

    if yDistance[0] == 0:
        y1 = bbox[1]
    else:
        y1 = yDistance[0]

    if yDistance[1] == 0:
        y2 = bbox[5]
    else:
        y2 = yDistance[1]
    #print(f"x1: {x1}, y1:{y1}, x2:{x2},y2:{y2}")
    # Compares for words inside the boundary
    if bbox:
        x = sys.maxsize
        y = sys.maxsize
        maxWidth = 0
        maxHeight = 0
        for i in data['texts'][1:]:
            bbox1 = i['bbox']
            midPoint = [(bbox1[0] + bbox1[2]) / 2, (bbox1[1] + bbox1[7]) / 2]
            if (x1 < midPoint[0] < x2) and (y1 < midPoint[1] < y2):
                if x > bbox1[0]:
                    x = bbox1[0]
                if y > bbox1[1]:
                    y = bbox1[1]
                if maxWidth < bbox1[2]:
                    maxWidth = bbox1[2]
                if maxHeight < bbox1[5]:
                    maxHeight = bbox1[5]
                if not texts['text'] and i['text'].strip() not in [':', ";", "."]:
                    texts['text'] = i["text"]
                    texts['bbox'] = bbox1
                    texts['confidence'] = i['confidence']
                elif i['text'].strip() not in [':', ";", "."]:
                    box = texts['bbox']
                    texts['text'] = texts['text'] + " " + i["text"]
                    texts['bbox'] = [box[0], box[1], bbox1[2], bbox1[3], bbox1[4], bbox1[5], box[6], box[7]]
                    texts['confidence'] = (texts['confidence'] + i['confidence']) / 2

        # Boundary box of the extracted text
        if texts['bbox']:
            textbbox = [x, y, maxWidth - x, maxHeight - y]

        # Removes the extra spaces between '-' and ','
        if texts['text']:
            text = texts['text'].replace(" ,", ",")
            text = text.replace(" - ", "-")
            text = text.replace("$ ", "$")
            text = text.replace("( ", "(")
            text = text.replace(" )", ")")

    return text, textbbox, texts['confidence']


# Get boundary box of the given key
def getBbox(key, linedata, data):
    if not key:
        return [0, 0, 0, 0, 0, 0, 0, 0]

    bbox = [0, 0, 0, 0, 0, 0, 0, 0]
    key1 = extract_keys(key, data, False)
    if key1:
        for i in linedata:
            if key1 in i['LineText']:
                keys = key1.split()
                lineWords = i['Words']
                numberOfKeys = len(keys)
                for i in range(0, len(lineWords) - numberOfKeys + 1):
                    keyList = []
                    for k in range(0, numberOfKeys):
                        keyList.append(lineWords[i + k]['text'])
                    if keyList == keys:
                        bbox = lineWords[i]['bbox']
    return bbox


# Primary key referencing, refkeys other referencing points, LineData of the line which has key, LineOCR, data, deviations to the refKeys
def GetUsingReferencing(key, refKeys, lineData, lineOCR, data, deviations=None):
    refBbox = []
    if not deviations:
        deviations = [0, 0, 0, 0]
    # top, left, bottom, right

    for k in range(0, 4):
        if isinstance(refKeys[k], int):
            refBbox.append(refKeys[k])
        else:
            bbox = getBbox(refKeys[k], lineOCR, data)
            #print(f"box: {bbox} key: {refKeys[k]}")
            # TOP X1
            if k == 0:
                refBbox.append(bbox[5] + deviations[0])
            # LEFT Y1
            if k == 1:
                refBbox.append(bbox[2] + deviations[1])
            # BOTTOM X2
            if k == 2 and isinstance(deviations[2],dict):
                refBbox.append(refBbox[0] + deviations[2]["Top"])
            elif k==2:
                refBbox.append(bbox[1] + deviations[2])
            # RIGHT Y2
            if k == 3:
                refBbox.append(bbox[0] + deviations[3])
    #print(f"box: {refBbox} key: {refKeys}")
    return GetText(key.split(), lineData, [refBbox[1], refBbox[3]], [refBbox[0], refBbox[2]], data)


# function to compare co-ordinates of ocr and prediction
def compare(templateBbox, data):
    # a,b,c,d
    resText = ""
    x = templateBbox[0]
    y = templateBbox[1]

    xx = x + templateBbox[2]
    yy = y + templateBbox[3]

    # Contains both the phrase and the confidence score
    text_and_score = []

    for text in data["texts"][1:]:
        wordSegmentation = text["bbox"]
        mid = [(wordSegmentation[0] + wordSegmentation[2]) / 2, (wordSegmentation[1] + wordSegmentation[7]) / 2]
        mid2 = [(mid[0] + wordSegmentation[2]) / 2, (mid[1] + wordSegmentation[7]) / 2]
        if x <= mid[0] <= xx and y <= mid[1] <= yy:
            if resText != "":
                resText += " " + text["text"]
            else:
                resText = text["text"]
        elif x <= mid2[0] <= xx and y <= mid2[1] <= yy:
            if resText != "":
                resText += " " + text["text"]
            else:
                resText = text["text"]

    list_resText = re.split(', |_|-|!|,| ', resText)

    confidence_list = []
    for word in list_resText:
        for j in range(len(data["texts"])):
            if data["texts"][j]["text"] == str(word):

                confidence_list.append(data["texts"][j]["confidence"])
            else:
                continue

    text_and_score.append(resText)
    try:
        text_and_score.append(statistics.mean(confidence_list))
    except:
        text_and_score.append(0)

    return text_and_score

## returns the bbox of the entire text of the doc
def finding_extremes(data):
    words_string = data["texts"][1:]
    x_extreme_left = []
    x_extreme_right = []
    y_extreme_top = []
    y_extreme_bottom = []

    for i in range(0, len(words_string), 1):
        x1 = words_string[i]["bbox"][0]  # getting all the x1
        y1 = words_string[i]["bbox"][1]  # getting all the y1
        x3 = words_string[i]["bbox"][4]  # getting all the x3
        y3 = words_string[i]["bbox"][5]  # getting all the y3
        x_extreme_left.append(x1)
        x_extreme_right.append(x3)
        y_extreme_top.append(y1)
        y_extreme_bottom.append(y3)

    x1_min = min(x_extreme_left)  # minimum of all x1's
    x3_max = max(x_extreme_right)  # maximum of all x3's
    y1_min = min(y_extreme_top)   # minimum of all y1's
    y3_max = max(y_extreme_bottom) # maximum of all y3's

    # left_extreme ,right_extreme , top_extreme , bottom_extreme
    return x1_min, x3_max, y1_min, y3_max


##### classification function #########################
######################## finding words based on the keyword #########################################
def keyword_finder(word, word_string):
    words = []
    for i in range(0, len(word_string), 1):
        ratio = fuzz.WRatio(word, word_string[i]["text"])
        len1 = len(word)
        len2 = len(word_string[i]["text"])
        if (word_string[i]["text"] == word or (ratio >= 80 and len1 == len2)):
            words.append(word_string[i]["text"])
    return words

## makes sure only one type is getting returned by the classification script
def validator(arr):
    count = 0
    for i in arr:
        if (i == 0):
            count += 1
    # checks if there is only one 1 bit flipped in the entire list
    if (count == len(arr) - 1):
        return True
    else:
        return False

# appends the values to the "result" dictionary
def append_result(result, name, value, isLineItem, LineItemSeq, bbox, index, score):
    result.append({
        "Name": name,
        "Value": value,
        "IsLineItem": isLineItem,
        "LineItemSequence": LineItemSeq,
        "bounding_box": [cords_formatter(bbox)],
        "offsets":[index] ,
        "ConfidenceScore": score})
    return result

# function to match the sentence and line ocr
def match_sent(line_data,sent):
    for i in line_data:
        #print(f"Sentence: {i['LineText']}, Sim: {fuzz.partial_ratio(i['LineText'],sentence)}")
        if fuzz.partial_ratio(i['LineText'],sent) > 90:
            return i

# function to match sent in the selected line i.e output of match_sent
def match_in_sent(line,word,part):
    try:
        # if no matching is given i.e None
        if not word:
            return 0
        
        if not line:
            return 0

        # split sentence into word
        words = word.split()
        #flag to check if sent matches
        flag = True
        for no,i in enumerate(line["Words"]):
            # find the first word in sent to match
            if fuzz.partial_ratio(i["text"],words[0]) >90:
                # if first word matches then extract the word info
                x = i["text"]
                flag = False
                # match the next consecutive word till the given sentence len
                for j in range(no,len(words)):
                    x = x + " " + line["Words"][j]["text"]
                break
        # if match not found
        if flag:
            raise Exception(f"Word not found:{words[0]}, part: {part}")
        # if match is found
        if fuzz.partial_ratio(x,word)> 90:
            # if the matched part is left then find the min x2
            if part == "Left":
                return min([line["Words"][i]["bbox"][2] for i in range(no,no+len(words))])
            # if the matched part is right then find the max x1
            elif part =="Right":
                return max([line["Words"][i]["bbox"][0] for i in range(no,no+len(words))])
            # if the matched part is Top then find the min y2
            elif part =="Top":
                return min([line["Words"][i]["bbox"][7] for i in range(no,no+len(words))])
            # if the matched part is Bottom then find the max y1
            elif part =="Bottom":
                return max([line["Words"][i]["bbox"][1] for i in range(no,no+len(words))])
        else:
            raise Exception(f"x din't match in {part}")
    except:
        return 0


# create the box from the given reference words
def create_box(data,line_data, sent,top,top_is_same,right,right_is_same,left,left_is_same,bottom):
    # match prime reference word
    matched = match_sent(line_data=line_data,sent=sent)
    # find extremes co_ordinates
    z = finding_extremes(data)
    # rearrange co_ord
    z = [z[0],z[2],z[1],z[3]]
    bbox = [z[0],z[2],z[1],z[3]]
    # if prime matches
    if matched:
        # check if top is present in prime ref
        if top_is_same:
            # find the ref in the selected line
            bbox[1] =  match_in_sent(line=matched,word=top,part="Top")
        else:
            # find the top ref in line ocr
            matched_top = match_sent(line_data=line_data,sent=top)
            # find the ref in the selected line
            bbox[1] =  match_in_sent(line=matched_top,word=top,part="Top")
        # check if right is present in prime ref
        if right_is_same:
            # find the ref in the selected line
            bbox[2] = match_in_sent(line=matched,word=right,part="Right")   
        else:
            # find the right ref in line ocr
            matched_right = match_sent(line_data=line_data,sent=right)
            # find the ref in the selected line
            bbox[2] = match_in_sent(line=matched_right,word=right,part="Right")
        # check if left is present in prime ref
        if left_is_same:
            # find the ref in the selected line
            bbox[0] = match_in_sent(line=matched,word=left,part="Left")
            
        else:
            # find the left ref in line ocr
            matched_left = match_sent(line_data=line_data,sent=left)
            # find the ref in the selected line
            bbox[0] = match_in_sent(line=matched_left,word=left,part="Left")
        # find the bottom ref in line ocr
        matched_bottom = match_sent(line_data=line_data,sent=bottom)
        # find the ref in the selected line
        bbox[3] = match_in_sent(line=matched_bottom,word=bottom,part="Bottom")
        bbox = [bbox[i] if bbox[i]!=0 else z[i] for i in range(0,4)]
        return bbox
    else:
        return None

# function to filter out the ocr based on given co_ordinates    
def filter_ocr(data,bbox:list,flex:list):
    try:
        new_data = {"texts": [data["texts"][0]]}
        for i in data["texts"][1:]:
            # check the mid point of the word lies in the given box
            if ((i["bbox"][0]+i["bbox"][2])/2 >= int(bbox[0] or 0) + flex[0]) & ((i["bbox"][1]+i["bbox"][5])/2 >= int(bbox[1] or 0) +flex[1]) & ((i["bbox"][0]+i["bbox"][2])/2 <= int(bbox[2] or 0) + flex[2]) & ((i["bbox"][1]+i["bbox"][5])/2 <= int(bbox[3] or 0) +flex[3]):
                new_data["texts"].append(i)    
        return new_data
    except:
        return None


###### for property nested #######################
def property_result_formatter(result):
    new_result = []
    prop_result = []
    for i in range(len(result)):
        if "Property" in result[i]["Name"] and result[i]["Name"]!="PropertyAddress":
            prop_result.append(result[i])        
        else:
            new_result.append(result[i])

    if len(prop_result)!=0:
        for i in range(len(new_result)):
            if new_result[i]["Name"]=="PropertyAddress":
                new_result[i]["Details"]= prop_result

    elif len(prop_result)==0:
        for i in range(len(new_result)):
            if new_result[i]["Name"]=="PropertyAddress":
                new_result[i]["Details"]= []

    return new_result