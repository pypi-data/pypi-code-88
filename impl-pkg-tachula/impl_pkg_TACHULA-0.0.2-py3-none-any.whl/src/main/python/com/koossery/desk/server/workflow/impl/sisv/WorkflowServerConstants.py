from bs4 import BeautifulSoup


class WorkflowServerConstants:

     WORKFLOW_SERVER_GLOBAL_CONFIG_FILE = "koosserydesk-workflow-srv.properties"
     ECM_RESTWEBSVCE_HOST = "ecm.restwebsvce.host"
     ECM_RESTWEBSVCE_PORT = "ecm.restwebsvce.port"
     ECM_RESTWEBSVCE_ROOTNAME = "ecm.restwebsvce.rootname"
     BPM_RESTWEBSVCE_HOST = "bpm.restwebsvce.host"
     BPM_RESTWEBSVCE_PORT = "bpm.restwebsvce.port"
     BPM_RESTWEBSVCE_ROOTNAME = "bpm.restwebsvce.rootname"
     # retrieve message from a xml file using idmessage
     workflowServiceMessagePath='src/impl/src/main/ressources/service/messages/toolServiceMessage.xml'


     def getMessage(keyError, file):
          with open(file, 'r') as f:
               # Read each line in the file, readlines() returns a list of lines
               content = f.readlines()
               # Combine the lines in the list into a string
               content = "".join(content)
               bs_content =BeautifulSoup(content, "lxml")
               b_message= bs_content.find('messages')
               b_error=b_message.find('error',{'key': keyError})['value']
               return str(b_error)

