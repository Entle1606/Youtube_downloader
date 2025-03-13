YouTube Video Downloader
This Python script allows you to download YouTube videos using the pytubefix library. The program supports downloading videos in various resolutions and formats, and it also allows batch downloads from multiple YouTube links. You can specify a download folder where the videos will be saved.

Features
Download YouTube videos in various formats (mp4, webm).
Download videos in different resolutions (e.g., 1080p, 720p).
Save videos to a specified folder on your local machine.
Option for batch downloading multiple videos at once.
Gracefully exit the program by typing exit.

Requirements
Before running the script, make sure you have Python installed and the required dependencies. You will also need the pytubefix library.

Dependencies
pytubefix: A Python library for downloading YouTube videos.
python youtube_downloader.py to run the programme

How to Use
1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project folder.

3. Run the Python script:

4. When prompted, enter the YouTube URLs you wish to download (separated by commas for batch downloads). You can type 'exit' to stop the program.

5. Specify the folder where you want the videos to be saved.

6. Select the resolution (e.g., 1080p, 720p) and the file format (e.g., mp4, webm) for your download.

7. The downloader will start downloading the videos one by one. After completion, the program will either exit automatically or await more input.

   Code Overview
Download(link, download_folder, resolution, file_format)
This function downloads a single video from the provided YouTube link. It allows you to specify the desired resolution and format, and saves the video to the given download folder.

BatchDownload(links, download_folder, resolution, file_format)
This function processes multiple YouTube links, downloading each one sequentially. The links are provided as a comma-separated list.

main()
The main function handles user input, allowing you to enter multiple video URLs, select a download folder, and choose resolution/format options. It then calls BatchDownload to process the download.

Error Handling
The program gracefully handles common issues, including:

Video Unavailability: If a video is not available, the downloader will report the error.
Regex Errors: If there is a problem with the YouTube URL format, it will notify the user.
Unexpected Errors: Any other unexpected issues will be caught and displayed.
