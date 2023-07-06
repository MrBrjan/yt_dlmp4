# YouTube Video Downloader

This is a Python script that allows you to download YouTube videos and save them in the MP4 format. The script uses the `yt_dlp` library for downloading videos.

## Setup

To use this script, you need to follow these steps:

1. Install the required libraries by running the following command:

2. Clone the repository or download the script file.

3. Make sure you have Python 3.x installed on your system.

4. Run the script using the following command: pip install yt_dlp

## Usage

1. When prompted, enter the URL or ID of the YouTube playlist you want to download. If you want to download a single video, enter the video's URL or ID.

2. The script will download the videos and save them in the format `playlist_title/video_title.mp4` for playlists or `video_title.mp4` for single videos. The downloaded videos will be saved in the same directory as the script.

## Advanced Options

If you want to change the output format or video quality, you can modify the options in the script:

- Output Format: By default, the script saves videos in the MP4 format. If you want to change the output format, modify the `merge_output_format` option in the `options` dictionary.

- Video Quality: The script downloads the best available video and audio quality by default. If you want to change the video quality, modify the `format` option in the `options` dictionary. You can refer to the `yt_dlp` documentation for more information on available format options.

Please note that downloading videos from YouTube may infringe on the platform's terms of service or violate copyright laws. Make sure to use this script responsibly and for personal use only.


## Usage

1. When prompted, enter the URL or ID of the YouTube playlist you want to download. If you want to download a single video, enter the video's URL or ID.

2. The script will download the videos and save them in the format `playlist_title/video_title.mp4` for playlists or `video_title.mp4` for single videos. The downloaded videos will be saved in the same directory as the script.

## Advanced Options

If you want to change the output format or video quality, you can modify the options in the script:

- Output Format: By default, the script saves videos in the MP4 format. If you want to change the output format, modify the `merge_output_format` option in the `options` dictionary.

- Video Quality: The script downloads the best available video and audio quality by default. If you want to change the video quality, modify the `format` option in the `options` dictionary. You can refer to the `yt_dlp` documentation for more information on available format options.

Please note that downloading videos from YouTube may infringe on the platform's terms of service or violate copyright laws. Make sure to use this script responsibly and for personal use only.


### Usage and Copyright

The yt_dlp library is released under an open-source license and can be used free of charge. However, using and downloading videos from YouTube may violate YouTube's policies and regulations. Make sure to comply with YouTube's terms of service and only use this library for personal purposes.

### Documentation

You can learn more about the yt_dlp library on the project's official GitHub page: [yt-dlp](https://github.com/yt-dlp/yt-dlp).

### Contributions

If you encounter any issues or have suggestions for improvements to the yt_dlp library, you can contribute to the project by creating issues or pull requests on the GitHub page.

