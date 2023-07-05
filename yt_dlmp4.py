import os
import yt_dlp

# Lấy URL hoặc ID của playlist từ người dùng.
url_or_playlist_id = input("Nhập URL hoặc ID của playlist YouTube: ")

# Tạo một từ điển với các tùy chọn cho quá trình tải xuống.
options = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
    'merge_output_format': 'mp4', # Định dạng file đã edit xong rồi
    'ignoreerrors': True,  # Bỏ qua lỗi và tiếp tục tải xuống các video khác
}

# Tạo một đối tượng YTDL với các tùy chọn.
ydl = yt_dlp.YoutubeDL(options)

# Kiểm tra xem đầu vào là một playlist hay một liên kết video.
if 'playlist?list=' in url_or_playlist_id:
    # Phát hiện URL của playlist.
    playlist_url = url_or_playlist_id

    # Trích xuất thông tin playlist.
    playlist = ydl.extract_info(playlist_url, download=False)

    # Tạo thư mục cho playlist.
    playlist_directory = playlist['title']
    if not os.path.exists(playlist_directory):
        os.makedirs(playlist_directory)

    # Lặp qua từng video trong playlist.
    for video in playlist['entries']:
        video_url = video['webpage_url']
        try:
            # Tải xuống video.
            ydl.download([video_url])
        except yt_dlp.DownloadError as e:
            if 'Video unavailable' in str(e):
                print(f"Video không khả dụng: {video_url}. Bỏ qua việc tải xuống.")
            else:
                print(f"Đã xảy ra lỗi với video: {video_url}. Lỗi: {e}")
else:
    # Phát hiện URL của video.
    video_url = url_or_playlist_id

    # Tải xuống video.
    try:
        ydl.download([video_url])
    except yt_dlp.DownloadError as e:
        if 'Video unavailable' in str(e):
            print("Video không khả dụng. Bỏ qua việc tải xuống.")
        else:
            print("Đã xảy ra lỗi:", e)
