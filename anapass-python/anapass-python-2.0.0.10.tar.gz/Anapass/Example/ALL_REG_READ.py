from Anapass.TModule import *

t5_dev = TDevice(TDevice.Type.T5)

isConnect = t5_dev.Connect()

t5_dev.WriteReg(0x9F, 0x00, 0x02, [0x5A, 0x5A])
t5_dev.WriteReg(0xF0, 0x00, 0x02, [0x5A, 0x5A])
t5_dev.WriteReg(0xF1, 0x00, 0x02, [0x5A, 0x5A])
t5_dev.WriteReg(0xFC, 0x00, 0x02, [0x5A, 0x5A])

CMD_Dict = {}

fread = open('ANA6707_ADDRESS.txt', 'r')

IP_LIST = fread.readlines()

for i in IP_LIST:
    Addr = int(i.split('\t')[0], 16)
    IP = i.split('\t')[1]    
    Count = int(i.split('\t')[2])    
    CMD_Dict[IP] = [Addr, Count]

reg_txt = ''
wreg_txt = ''
for key in CMD_Dict.keys():
    readAddr = CMD_Dict[key][0]
    readCount = CMD_Dict[key][1]
    readValues = [0 for i in range(readCount)]
    t5_dev.ReadReg(readAddr, 0x00, readCount,readValues)
    addr = 0
    reg_txt += key +'\n'
    wreg_txt += ';;;;'+ key + ' ' + str(readCount) + ' ea\n'
    wreg_txt += 'wreg0 = 0x39, ' + '0x' '%02X' %readAddr + ', ' 

    for i in range(readCount):
        data = '0x' + '%02X'  %readValues[i]
        reg_txt += str(addr).zfill(4) + '\t' + data + '\n'
        if i == readCount - 1:
            wreg_txt += data
        else:
            wreg_txt += data + ', '
        addr += 1
    wreg_txt += '\n'
    
filename = input('output filename : ')
fout = open(filename + '.txt', 'w')
fout.write(reg_txt)
fout.close()

fout = open( filename + '_wreg.txt', 'w')
fout.write(wreg_txt)
fout.close()
