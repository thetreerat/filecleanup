class MailHelp:
    """Mail helper class"""
    def __init__(self, EmailAddress="",EmailHost="",Port=25):
        self.EmailAddress = EmailAddress
        self.EMailHost = EmailHost
        self.Port = Port
        self.Password = None
        
    def PrintValues(self):
        #print(self)
        print("""EmailAddress: %s
EmailHost: %s
Port: %s
Password: %s""" % (self.EmailAddress, self.EmailHost, self.Port, self.Password))

class MessageHelp:
    """Email Message Helper Class"""
    def __init__(self, Subject="", Body="", SendTo=""):
        self.Subject = Subject
        self.Body = Body
        self.SendTo=""

    def PrintValues(self):
        print("""SendTo: %s
Subject: %s
Body: %s""" % (self.SendTo, self.Subject, self.Body))
        
