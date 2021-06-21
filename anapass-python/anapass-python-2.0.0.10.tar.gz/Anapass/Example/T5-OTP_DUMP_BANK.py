from Anapass.TModule import *
import time

ModuleType = input('Enter Module Type : 6705, 6706, 6707, 6708 ')

filename = input('Save file name : ')


#@@@@@초기 구동 상태@@@@@@@@@@@@@
t5_dev = TDevice(TDevice.Type.T5)

isConnect = t5_dev.Connect()

if isConnect:
    print('Connection Success')
    t5_power = TPower()
else:
    print('Check Connections')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# OTP Bank Size Setting
if ModuleType == '6706':
    NumBytesBank = 1024*8 # 8192
    readAddr = 0xD0
    readOffset = 0x0D
    readCount = 4
    readValues = [0 for i in range(readCount)]
elif ModuleType == '6707':
    NumBytesBank = 1024*8 # 8192
    readAddr = 0xD0
    readOffset = 0x0D
    readCount = 4
    readValues = [0 for i in range(readCount)]
elif ModuleType == '6708':
    NumBytesBank = 1024*4 # 4096
    readAddr = 0xD0
    readOffset = 0x0D
    readCount = 4
    readValues = [0 for i in range(readCount)]
else:
    NumBytesBank = 1024*4 # 4096 @ ANA6705
    readAddr = 0xD3
    readOffset = 0x0C
    readCount = 4
    readValues = [0 for i in range(readCount)]
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    


i_NumBytesBank = int(NumBytesBank / 4)

bankx_addr_start = i_NumBytesBank * 0 #Bank # for 0~3

addr = 0

bank_data = ''

test_txt = ''

t5_dev.SendTxtCmd('WREG0		= 0x39, 0xF0, 0x5A, 0x5A')
t5_dev.SendTxtCmd('WREG0		= 0x39, 0xF1, 0x5A, 0x5A')
t5_dev.SendTxtCmd('WREG0		= 0x39, 0xFC, 0x5A, 0x5A')

start_t = time.time()
for addr_start in range(bankx_addr_start,bankx_addr_start + i_NumBytesBank + 1):
    addr_ms = '0x' + '%02X' % ((addr_start >> 8) & 0xFF) #addr upper address
    addr_ls = '0x' + '%02X' % (addr_start & 0xFF) #addr lower address
    
    if ModuleType == '6706' or ModuleType == '6707' or ModuleType == '6708':
        cmd = 'WREG0 = 0x39, 0xD0, 0x00, 0x77,'
        cmd += addr_ms + ','+ addr_ls + ','+ addr_ms + ','+ addr_ls + ',' + '0x00, 0x00, 0x00, 0x00, 0x00, 0x01'
    else:
        cmd = 'WREG0 = 0x39, 0xD3, 0x00, 0x77,'
        addr_ms = '0x' + '%02X' % (((addr_start) & 0xFF00)+ ((addr_start >> 8) & 0x00FF)) #for 6705
        cmd += addr_ms + ',' + addr_ls + ',' + addr_ls + ',' + '0x00, 0x00, 0x00, 0x00, 0x00, 0x01'

    t5_dev.SendTxtCmd(cmd)
    #time.sleep(0.2) # If you need any delay time
    t5_dev.ReadReg(readAddr, readOffset, readCount, readValues)
    #readValues = t5_dev.DD_DSIM_MipiReadReg(0, readAddr, readOffset, readCount)

    for i in range(readCount-1,-1,-1):
        bank_data = '0x' + '%02X'  %readValues[i] + '\n'
        test_txt += str(addr).zfill(4) + '\t' + bank_data
        addr += 1

end_t = time.time()
print(start_t - end_t)
    
fout = open(filename + '.txt', 'w')
fout.write(test_txt)
fout.close()
        
t5_dev.Reset()


print('Write Report Complete.')
