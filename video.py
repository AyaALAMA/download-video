import pytube
print("Download video from web by bython")
url=input('enter video url:')
pytube.YouTube(url).streams.get_highest_resolution().download('Downloads')

#https://www.youtube.com/watch?v=mvZHDpCHphk&list=PLDoPjvoNmBAyE_gei5d18q