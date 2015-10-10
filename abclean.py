import sys,os

def mainscreenmessage(c=0, usb=0):
 
    print("""     Main screen
     ---- ------

     %i files in C: dir
     %i files on USB dir""" % (c, usb))

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

if __name__ == '__main__':
    try:
        print("Hello, on to more importan things")
        
        
        filecountc = countbackups(path="""c:\\users\\Harold\\Documents\\""")
        filecountusb = countbackups(path="""c:\\users\\Harold\\""")
        mainscreenmessage(filecountc,filecountusb)
    finally:
        print("Thank you for playing")
