#!C:/Users/Kishor/AppData/Local/Programs/Python/Python38-32/python.exe
print("Content-Type: text/html\n\n")
print("""<html><head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"></link>
</head><body><br><br><br><div class='container'><div style="display: none;">""")
import cgi, os
import cgitb; cgitb.enable()

from moviepy.editor import *
from datetime import datetime

form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
allowed_extensions = ['mp4']
# Test if the file was uploaded
if fileitem.filename and fileitem.filename[-3:] in allowed_extensions:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('uploads/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   datentime = datetime.now()
   clipname = datentime.strftime("%d%m%H%M%S%f")


   print(fn)
   fn = str("uploads/"+fn)
   clip = VideoFileClip(fn)
   cuts = clip.duration/15
   cuts = int(cuts)
   #print(cuts)
   subclips = []
   def st(value):
       x=value*15
       return x
   def et(value):
       x=value+1
       x=x*15
       return x
   for i in range(0,cuts):
       subclips.append(clip.subclip(st(i),et(i)))
       subclips[i].write_videofile("downloads/" + clipname + str(i+1) + '.mp4')
       print(subclips[i].duration)

   subclips.append(clip.subclip(st(cuts),clip.duration))
   print(subclips[cuts].duration)
   subclips[cuts].write_videofile("downloads/" + clipname + str(cuts+1) + '.mp4')
   print("""</div><div class='row'>""")
   for i in range(0,cuts+1):
       print("""<div class="col-lg-12 text-center" style="padding-bottom: 10px;padding-top: 10px;"><button type="button" class="btn btn-dark"><a class="text-white" href='downloads/%s%s.mp4' download> download </a></button></div>""" % (clipname, i+1))

   print("""</div></div><body></html>""")

     
else:
   print("""</div><div class='row'><h1>Please upload a .mp4 video file</h1></div></div><body></html>""")
