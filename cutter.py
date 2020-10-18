#!C:/Users/Kishor/AppData/Local/Programs/Python/Python38-32/python.exe
print("Content-Type: text/html\n\n")
print("""<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="A minimalistic way to cut your long videos into 15 seconds segments for whatsapp and instagram in windows, instead of cutting it manually.">
<meta name="keywords" content="Whatsapp, instagram, cutter, video, status, stories, trim">
<meta name="author" content="Kishor. A">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"></link>
<title>Status Cutter</title>
</head><body><div class="container-fluid">
        <div class="row bg-dark">
            <div class="col-9 col-sm-9 col-lg-11 text-center font-weight-bold  p-3 bg-dark text-white align-self-center">
                <h1 style="font-size: 2.5rem;"> STATUS CUTTER</h1>
            </div>
            <div class="col-3 col-sm-3 col-lg-1 text-center font-weight-bold  p-3 bg-dark text-white align-self-center">
                <button type="button" class="btn btn-light text-center btn-outline-light"><a href="https://github.com/k1sh0r/StatusCutter"><img src="git1.png" alt="GitHub" style="width:2rem;" ></a></button>
            </div>
        </div>
    </div>
    </div><br><br><br><div class='container'>
    <div style="display: none;">""")
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
   fn = os.path.basename(fileitem.filename)
   open('uploads/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   datentime = datetime.now()
   clipname = datentime.strftime("%d%m%H%M%S%f")


   print(fn)
   fn = str("uploads/"+fn)
   clip = VideoFileClip(fn)
   cuts = clip.duration/30
   cuts = int(cuts)
   #print(cuts)
   subclips = []
   def st(value):
       x=value*30
       return x
   def et(value):
       x=value+1
       x=x*30
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
       print("""<div class="col-lg-12 text-center" style="padding-bottom: 10px;padding-top: 10px;"><button type="button" class="btn btn-dark"><a class="text-white" href='downloads/%s%s.mp4' download> Download - %s</a></button></div>""" % (clipname, i+1, i+1))

   print("""</div></div><body></html>""")

     
else:
   print("""</div><div class='row'><div class="col-lg-12 text-center"><h3>Please upload a .mp4 video file</h3></div><div class='mt-3 col-lg-12 col-sm-12'>                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js">
                </script>
                <lottie-player src="retry.json"  background="transparent"  speed="1"  style="width: 300px; height: 300px; margin-left: auto;margin-right: auto"  loop  autoplay>
                </lottie-player><div class='row'><div class='col-lg-12 col-sm-12'><div class="text-center"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button></div></div>
</div></div></div><body></html>""")
