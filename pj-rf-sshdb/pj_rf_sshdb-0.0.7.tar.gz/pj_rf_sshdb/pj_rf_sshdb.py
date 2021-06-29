from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class pj_rf_sshdb():
    
    def SSHDB(input_remote_server_IP, input_remote_server_port, input_ssh_username, 
        input_ssh_password, input_remote_bind_address, input_remote_bind_address_port, input_db_server, input_db_name, input_query):

        with SSHTunnelForwarder(
            (input_remote_server_IP, int(input_remote_server_port)), #Remote server IP and SSH port
            ssh_username = input_ssh_username,
            ssh_password = input_ssh_password,
            remote_bind_address=(input_remote_bind_address, int(input_remote_bind_address_port))) as server: 
                
            server.start() #start ssh sever
            print ('Server connected via SSH')
            
            #connect to PostgreSQL
            local_port = str(server.local_bind_port)
            engine = create_engine(input_db_server + local_port + input_db_name)

            Session = sessionmaker(bind=engine)
            session = Session()
            print ('Database session created')
            
            #test data retrieval
            print ('Executing Query')
            test = session.execute(input_query)
            for row in test:
                print(row['otp'])
                otp = row['otp']
                
            session.close()
            return otp

`