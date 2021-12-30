from pytube import YouTube

url = "https://www.youtube.com/watch?v=Fs7ZqaB98GA"

myVideo = YouTube(url)

print(myVideo.title)

print(myVideo.thumbnail_url)

print(myVideo.thumbnail_url)

print(myVideo.streams.all)

myVideo = myVideo.streams.get_highest_resolution()

myVideo.download()

print("downloaded")
