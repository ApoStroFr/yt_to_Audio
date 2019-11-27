import sys
from pytube import YouTube

#SHOW A PROGRESS BAR
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))
 
def url_dwl(url):
	global file_size
	yt = YouTube(url, on_progress_callback=progress_Check)
	audio = yt.streams.filter(only_audio=True).first()
	file_size = audio.filesize
	print('----- '+yt.title+' -----')
	audio.download()
	print('	==> download completed')


file_size = 0
if str(sys.argv[1]) == '-u':	
	url = sys.argv[2]
	url_dwl(url)

else :
	print("Below the command line possible :")
	print("	-u [YOUTUBE URL] : Télécharge la vidéo youtube si celle-ci dure moins de 20 minutes ")
	print("	-h : Command guideline")