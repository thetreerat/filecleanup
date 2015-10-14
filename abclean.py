import sys,os, getopt
import mailhelp
import smtplib

def countbackups(path=""):
    count = 0
    try:
        filelist = os.listdir(path)
        for f in filelist:
            if f[-3:] == '.py':
                count += 1
        return count
    except FileNotFoundError as e:
        print("""%s Path not found """ % (path))
        return None

def emailstatus(emailsettings, messagedata):
    server = None
    try:      
        if not emailsettings.EmailHost=="":
            print(emailsettings.EmailHost)
            server = smtplib.SMTP(emailsettings.EmailHost)
            server.connect()
        else:
            print('No mailhost defined')
    except ConnectionRefusedError as e:
        print("No email sent, server refused connection")
        return
    except OSError as e:
        
        print(type(e))
        print("OS error: {0}".format(e))
        sys.exit(1)
    finally:
        if server:
            server.quit

def loadcommandlinevars(commandline, emailsettings):
    try:
        
        print("here")
        opts, args = getopt.getopt(commandline, "h:e:p:", ["-hostname ",
                                                            "-email ",
                                                            "-port "])
    except getopt.GetoptError:
        print("Error")
        #print(e)
        sys.exit(1)
        
    for option, value in opts:
        if option in ('-h', '-hostname'):
            emailsettings.EmailHost = value
            #print(emailsettings.EmailHost)
        elif option in ('-e', '-email'):
            emailsettings.EmailAddress=value
        elif option in ('-p', '-port'):
            emailsettings.Port=value
        #emailsettings.PrintValues()
    return emailsettings
    
def mainscreenmessage(c=0, usb=0):
 
    print("""     Main screen
     ---- ------

     %i files in C: dir
     %i files on USB dir""" % (c, usb))

if __name__ == '__main__':
    try:
        m = "Hello, on to more importan things"
        emailsettings = mailhelp.MailHelp()
        print(m)
        emailsettings = loadcommandlinevars(sys.argv[1:], emailsettings)
        filecountc = countbackups(path="""c:\\users\\Harold\\Documents\\""")
        filecountusb = countbackups(path="""c:\\users\\Harold\\""")
        #mainscreenmessage(filecountc,filecountusb)
        messagedata = {'body':m,'subject':'test'}
        #emailstatus(emailsettings, messagedata)
        emailsettings.PrintValues()
        print(messagedata)
    finally:
        print("Thank you for playing")
