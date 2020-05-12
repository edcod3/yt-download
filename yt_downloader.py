from pytube import YouTube

print("---Welcome to my YT Music Downloader---")
#Ask for Link and make it a pytube object
link = input("Enter the video url: ")
yt = YouTube(link)


def video_downloader():
    stream = yt.streams.first()
    print(stream)
    stream.download()
    return

def audio_downloader():
    stream = yt.streams.filter(only_audio=True).first()
    print(stream)
    stream.download()
    return



dd = input("Do you want to download as a video or as audio? ")
if dd == "video":
    video_downloader()
    print( "Video has been successfully downloaded as video!")
elif dd == "audio":
    audio_downloader()
    print(" Audio has been successfully downloaded as audio!")
elif dd == "No":
    quit()


#Quit Programm
qt = input("Type q to quit: ")
if qt == "q":
    quit() 