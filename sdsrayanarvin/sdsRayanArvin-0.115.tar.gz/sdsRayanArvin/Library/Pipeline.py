from sdsRayanArvin.Dataset.AuxStationData import Aux
from sdsRayanArvin.RepositoryApi.DataApi import Data


class Pipeline:
    def GetLastData(self, Aux_data: Aux, deviceData: Data):
        if Aux_data is None:
            return 0

        type_aux = None

        if Aux_data.type == 1:
            type_aux = 'DO'
        if Aux_data.type == 2:
            type_aux = 'DI'
        if Aux_data.type == 3:
            return self.ReplaceTagWithValue(Aux_data, deviceData, 'AI')  # AI
        if Aux_data.type == 5:
            type_aux = 'VDO'
        if Aux_data.type == 6:
            return self.ReplaceTagWithValue(Aux_data, deviceData)  # AII
        if Aux_data.type == 8:
            return self.ReplaceTagWithValue(Aux_data, deviceData)

        if type_aux is None:
            return

        Last_data = deviceData.LastDataOnTopic(str(Aux_data.code),
                                               str(type_aux),
                                               str(Aux_data.pan),
                                               str(Aux_data.address))

        if Last_data is not None:
            if Aux_data.type == 1 or Aux_data.type == 2 or Aux_data.type == 5:
                try:
                    idxOutput = Aux_data.output - 1
                    binOutput = "{0:b}".format(int(Last_data.getData()))
                    binOutputArray = list(binOutput)
                    binOutputArray.reverse()
                    if len(binOutputArray) > idxOutput:
                        return binOutputArray[idxOutput]
                    else:
                        return 0
                except:
                    return 0

            return Last_data.getData()
        else:
            return 0

    def ReplaceTagWithValue(self, Aux_data: Aux, deviceData: Data, tag=None):
        arrayMath = Aux_data.Analog.math.split(' ')
        if tag is None:
            tag = arrayMath[0]
        Last_data = deviceData.LastDataOnTopic(str(Aux_data.code),
                                               str(tag),
                                               str(Aux_data.pan),
                                               str(Aux_data.address))

        data = '0' if Last_data is None else Last_data.getData()

        idxOutput = Aux_data.output - 1
        lastDataArray = data.split('/')

        if len(lastDataArray) > 1:
            data = lastDataArray[idxOutput]

        finalData = Aux_data.Analog.math.replace(arrayMath[0], data)

        return self.ReplaceMathWithValue(finalData)

    def ReplaceMathWithValue(self, value):
        arrayMath = value.split(' ')
        value = 0

        for idx, val in enumerate(arrayMath):
            if idx == 0 or idx == len(arrayMath) - 1 or idx % 2 == 0:
                continue

            nextVal = float(arrayMath[idx + 1])
            preVal = float(arrayMath[idx - 1])

            if val == '+':
                if value == 0:
                    value = preVal + nextVal
                else:
                    value += nextVal

            if val == '-':
                if value == 0:
                    value = preVal - nextVal
                else:
                    value -= nextVal

            if val == '/':
                if value == 0:
                    value = preVal / nextVal
                else:
                    value /= nextVal

            if val == '*':
                if value == 0:
                    value = preVal * nextVal
                else:
                    value *= nextVal

        return value
