from pytubefix import YouTube


def Download(link):
    try:
        youtubeObject = YouTube(link)  # Create YouTube object for the link
        stream = youtubeObject.streams.get_highest_resolution()  # Get the highest resolution stream
        stream.download()  # Download the video
        print("Download is completed successfully")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

link = input("Enter the YouTube video URL: ")
Download(link)
