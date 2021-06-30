from queue import Queue
from queue import Empty
from threading import Thread
from threading import RLock
import os
import logging
import asyncio
import tornado.ioloop
import tornado.web
import socketio
import time
import datetime
import yaml
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

HTML_PATH = os.path.join( os.path.dirname(__file__) , "dist")

class IOForm:
    def __init__(self, port = 8000, config = {}, certfile = None, keyfile = None ):
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile
        self.isSecure = certfile and keyfile
        self.config = config
        self.q_input = Queue()
        self.q_output = Queue()
        self.sio = socketio.AsyncServer(async_mode='tornado',cors_allowed_origins='*')
        self.thread = None

    def run(self):
        self.thread = t1 = Thread(target=self.start_thread2 , name="TornadoThread")
        self.thread.daemon = True
        self.thread.start()

    def is_alive(self):
        return self.thread.is_alive()
    
    def get(self):
        if self.q_input.empty():
            time.sleep(0.1) #This is to cut down on idle cycling
            return None
        else:
            return self.q_input.get()

    def put(self,msg):
        self.q_output.put(msg)
    
    def start_thread2(self):
        asyncio.run( self.start_thread() )

    async def start_thread(self):
        self.sio = socketio.AsyncServer(async_mode='tornado',cors_allowed_origins='*')
        @self.sio.event
        async def connect(sid, environ):
            print('connect ', sid)
        @self.sio.event
        async def disconnect(sid):
            lastsid = sid
            print('disconnect ', lastsid)
        @self.sio.event
        async def data(sid, msg):
            logging.debug("Received Message %s from %s" %(msg, sid) )
            self.q_input.put(msg,True)
            return "Received Successfully"
        @self.sio.event
        async def config(sid, msg):
            logging.debug("Config requested from %s" %(sid) )
            # with open(r'dist/inputs.yaml') as file:
            #     json = yaml.load(file, Loader=yaml.FullLoader)
            #     return json
            return self.config

        if await self.start_tornado():
            await asyncio.create_task( self.send_outputs_from_queue() )

    async def start_tornado(self):
        try:

            app = tornado.web.Application([
                # (r"/submit", MainHandler),
                (r"/socket.io/", socketio.get_tornado_handler(self.sio)),
                (r"/(.*)", tornado.web.StaticFileHandler, {"path": HTML_PATH , "default_filename": "index.html" })
            ])

            if ( self.isSecure):
                if ( not os.path.isfile(self.certfile) or not os.path.isfile(self.keyfile) ):
                    print("Certificate files: %s and %s do not exist! Creating...")
                    self.creteSelfSignedCert()
                http_server = tornado.httpserver.HTTPServer(app, ssl_options={
                    "certfile": self.certfile,
                    "keyfile": self.keyfile,
                })
                http_server.listen(self.port)
                print("HTTPS server started on port:", self.port)

            else:
                app.listen(self.port)
                print("HTTP server started on port:", self.port)
            return True
        except OSError:
            logging.critical("Can't listen on port %s" %self.port)
            return False

    async def send_outputs_from_queue(self):     
        logging.debug("Send Sockets Loop Started!")
        while True:
            try:
                json = self.q_output.get(False)
                logging.info("Sending event")
                await self.sio.emit( "data", json )
            except Empty:
                await asyncio.sleep(0.1)

    def creteSelfSignedCert(self):
        # Generate our key
        key = rsa.generate_private_key( public_exponent=65537, key_size=2048, )
        # Write our key to disk for safe keeping
        with open( self.keyfile, "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
                # encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
            ))

        # Various details about who we are. For a self-signed certificate the
        # subject and issuer are always the same.
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Illinois"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"Naperville"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"ucipass"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"FrontEnd by ucipass"),
        ])
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
        # Our certificate will be valid for 10 days
            datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
        # Sign our certificate with our private key
        ).sign(key, hashes.SHA256())
        # Write our certificate out to disk.
        with open( self.certfile, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

