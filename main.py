import pytube

url = input("enter video url: ")

path = ""

pytube.YouTube(url).streams.get_by_itag().download(url)
