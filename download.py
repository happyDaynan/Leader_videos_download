from pytube import YouTube
import re, os
with open ('urls.txt', 'r') as f:
    url_list = f.readlines()

mp4_t = len(url_list)
mp4_count = 0

for u in url_list:
    yt = YouTube('{}'.format(u))
    #　print("下載程式中請稍後")
    yt = yt.streams.filter()
    re_p = re.search(r'res=\"\d{4}\D{1}\"', str(yt))
    #print(re_p)
    
    if re_p != None:
        yt.filter(res='1080p').first().download()
        
        mp4_count += 1
        print("找到1080p", u)
    else:
        try:
            yt.filter(res='720p').first().download()
            print("找到720p", u)
            mp4_count += 1
        except AttributeError:
            print("沒找到720p", u)
print('下載:{}, 成功:{}'.format(mp4_t,mp4_count))
