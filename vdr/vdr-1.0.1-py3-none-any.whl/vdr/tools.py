import sentences


def update(filename):
    new_number = str(int(filename) + 1)
    while len(new_number) < 6:
        new_number = "0" + new_number
    return new_number


def safety(sentence, file):
    id_door = 0
    id_ballast = 0
    id_alarm = 0

    for i in sentence:

        if 'door' in i:
            file.write(sentence[0] + " " + sentences.SDS(id_door, sentence[sentence.index(i) + 1]))
            id_door += 1
        elif 'ballast' in i:
            file.write(sentence[0] + " " + sentences.SBS(id_ballast,
                                                         sentence[sentence.index(i) + 1],
                                                         sentence[sentence.index(i) + 2],
                                                         sentence[sentence.index(i) + 3]))
            id_ballast += 1
        elif 'alarm' in i:
            file.write(sentence[0] + " " + sentences.SAS(id_alarm, sentence[sentence.index(i) + 1]))
            id_alarm += 1

