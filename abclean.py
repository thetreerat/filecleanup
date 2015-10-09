import sys,os

def mainscreenmessage(c=0, usb=0):
 
    print("""     Main screen
     ---- ------

     %i files in C: dir
     %i files on USB dir""" % (c, usb))
     

if __name__ == '__main__':
    try:
        print("Hello, on to more importan things")
        filelist = os.listdir()
        filecount = len(filelist)
        mainscreenmessage(filecount,1)
    finally:
        print("Thank you for playing")
