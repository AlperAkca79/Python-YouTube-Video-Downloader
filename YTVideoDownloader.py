# By AlperAkca79
from pytube import YouTube

# Download Function
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    # If Video doesn't completed succesfully print this:
    except:
        print("An Error has Occurred!")
    
    # If Video completed succesfully print this:
    print("Download is completed succesfully")

# YouTube Video Link
link = input("Enter the link(URL) of the video you want to download from youtube:  ")

# Downloading Video
Download(link)