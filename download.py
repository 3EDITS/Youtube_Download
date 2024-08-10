import yt_dlp

def download_video(url, output_format):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'./%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': output_format
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

asking = input("Enter youtube URL : ")

if not asking:
    print("Please enter a valid URL")
else:
    print("Please select format type.")

    list_format = ['mp4', 'mp3', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'webm', 'mpeg', '3gp', 'ogv']

    for v in list_format:
         print(v)

    asking_format = input("Choosing : ")

    if not asking_format in list_format:
         print("Please enter a valid Value")
    else:
         download_video(asking, asking_format)