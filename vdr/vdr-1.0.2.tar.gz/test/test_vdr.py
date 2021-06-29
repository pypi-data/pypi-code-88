import vdr

VDR = vdr.Vdr()
VDR.add_connection("localhost", 12345, "ECDIS")
VDR.add_connection("localhost", 12346, "nmea")

ecdis = vdr.ReceivingFrame(VDR, "ECDIS")
nmea = vdr.ReceivingNmea(VDR, "nmea")

ecdis.start()
nmea.start()
