from pytube import YouTube

def download_video(url: str, path: str = "."):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        
        # get the best progressive stream (video + audio)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        
        if not stream:
            print("No suitable stream found.")
            return

        print(f"Downloading: {stream.resolution}")
        stream.download(output_path=path)
        print("Download completed ✅")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter The URL of Video: ").strip()
    download_video(link)


