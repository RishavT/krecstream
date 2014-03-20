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
        busName = dbus.service.BusName('krecstream.KRecStream', bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/KRecStream')
        self.recording_ids = {}
        self.streaming_ids = {}
    
    def record(self,w,h,name):
        print "starting"
        os.system('rm ' + name + '.flv')
        self.recording_ids[name] = subprocess.Popen("ffmpeg -video_size " + str(w) + "x" + str(h) + " -framerate 25 -f x11grab -i :0 " + name + ".flv &",shell=True)
        
        
    def stream(self,w,h,url,name):
        print "streaming"
        #string = 'ffmpeg -f x11grab -s ' +  str(w) + 'x' + str(h) + ' -r 15 -i :0.0 -preset fast -pix_fmt yuv420p -threads 0 -f flv "' + url + '"'
        string = 'ffmpeg -f x11grab -s ' +  str(w) + 'x' + str(h) + ' -r 15 -i :0.0 -pix_fmt yuv420p -threads 0 -f flv "' + url + '"'
        print string
        self.streaming_ids[name] = subprocess.Popen(string + " & ", shell=True)
    
    @dbus.service.method('krecstream.KRecStream', in_signature = 'iiss', out_signature = '')
    def startStream(self,w,h,url,name):
        os.system("kdialog --passivepopup 'recording started' 3")
        self.stream(w,h,url,name)
        
    @dbus.service.method('krecstream.KRecStream', in_signature = 's', out_signature = '')
    def stopStream(self,name):
        print "killing " + name
        os.system("kill " + str(self.streaming_ids[name].pid+1))
        del self.streaming_ids[name]
    
    @dbus.service.method('krecstream.KRecStream', in_signature = 'iis', out_signature = '')
    def startRecord(self,w,h,name):
        os.system("kdialog --passivepopup 'recording started' 3")
        self.record(w,h,name)
        
    @dbus.service.method('krecstream.KRecStream', in_signature = 's', out_signature = '')
    def stopRecord(self,name):
        print "killing"
        #self.recordID.kill()
        os.system("kill " + str(self.recording_ids[name].pid+1))
        #print self.recordID.pid
    
DBusQtMainLoop(set_as_default = True)
app = QCoreApplication([])
krecstream = KRecStream()
app.exec_()