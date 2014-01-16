#!/usr/bin/python
from PyQt4.QtCore import *
import math
import dbus
import dbus.service
from dbus.mainloop.qt import DBusQtMainLoop
import os
import subprocess
import signal

class KRecStream(dbus.service.Object):
    def __init__(self):
        busName = dbus.service.BusName('com.rishav.KRecStream', bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/KRecStream')
    
    def record(self,w,h):
        print "starting"
        os.system('rm output.flv')
        self.recordID = subprocess.Popen("ffmpeg -video_size " + str(w) + "x" + str(h) + " -framerate 25 -f x11grab -i :0 output.flv &",shell=True)
    def stream(self,w,h,url):
        print "streaming"
        string = 'ffmpeg -f x11grab -s ' +  str(w) + 'x' + str(h) + ' -r 15 -i :0.0 -preset fast -pix_fmt yuv420p -threads 0 -f flv "' + url + '"'
        print string
        self.streamID = subprocess.Popen(string + " & ", shell=True)
    
    @dbus.service.method('com.rishav.KRecStream', in_signature = 'iis', out_signature = '')
    def startStream(self,w,h,url):
        os.system("kdialog --passivepopup 'recording started' 3")
        self.stream(w,h,url)
        
    @dbus.service.method('com.rishav.KRecStream', in_signature = '', out_signature = '')
    def stopStream(self):
        print "killing"
        #self.recordID.kill()
        os.system("kill " + str(self.streamID.pid+1))
    
    @dbus.service.method('com.rishav.KRecStream', in_signature = 'ii', out_signature = '')
    def startRecord(self,w,h):
        os.system("kdialog --passivepopup 'recording started' 3")
        self.record(w,h)
        
    @dbus.service.method('com.rishav.KRecStream', in_signature = '', out_signature = '')
    def stopRecord(self):
        print "killing"
        #self.recordID.kill()
        os.system("kill " + str(self.recordID.pid+1))
        #print self.recordID.pid
    
DBusQtMainLoop(set_as_default = True)
app = QCoreApplication([])
krecstream = KRecStream()
app.exec_()