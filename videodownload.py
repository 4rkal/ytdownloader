import pytube

yt=pytube.YouTube("URL")

video=yt.streams.first()
video=yt.streams.get_highest_resolution()

video.download("PATH")
print("Succesfully downloaded : )")