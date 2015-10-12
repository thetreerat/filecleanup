import sys,os, getopt
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

def emailstatus(message='', sysopemail='hal@parkavebike.com'):
    server = None
    try:
        mailhost='localhost'
        print(mailhost)
        server = smtplib.SMTP(mailhost)
        server.connect()
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

def loadcommandlinevars():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
        for option, value in opts:
            if option in ('-h', '-hostname'):
                mailhost = value
                print(mailhost)
            elif option in ('-e', '-email'):
                emailaddress=value
    except getopt.GetoptError as e:
        print(e)
        sys.exit(1)
    
def mainscreenmessage(c=0, usb=0):
 
    print("""     Main screen
     ---- ------

     %i files in C: dir
     %i files on USB dir""" % (c, usb))

if __name__ == '__main__':
    try:
        print("Hello, on to more importan things")
        loadcommandlinevars()
        
        filecountc = countbackups(path="""c:\\users\\Harold\\Documents\\""")
        filecountusb = countbackups(path="""c:\\users\\Harold\\""")
        mainscreenmessage(filecountc,filecountusb)
        emailstatus()
    finally:
        print("Thank you for playing")
