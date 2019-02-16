import ffmpy

ff = ffmpy.FFmpeg()
ff._cmd = "ffmpeg -i C:/Users/y500/Desktop/time.avi  C:/Users/y500/Desktop/new.mp4"
ff.run()
