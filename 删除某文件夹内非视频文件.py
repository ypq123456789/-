import os
import mimetypes

# Specify your directory here
directory = 'E:\\OneDrive - todo group\\国产精品\\阿朱\\秀人网'

def find_non_videos(directory):
    non_video_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # Check if the file is a video file
            if not mimetypes.guess_type(filepath)[0].startswith('video'):
                non_video_files.append(filepath)
    return non_video_files

non_video_files = find_non_videos(directory)

# Print all non-video files
print("Found the following non-video files:")
for file in non_video_files:
    print(file)

# Ask the user if they want to delete the files
delete = input('Do you want to delete these files? (yes/no): ')
if delete.lower() == 'yes':
    for file in non_video_files:
        os.remove(file)
        print(f'Deleted: {file}')

# Delete empty directories
for root, dirs, files in os.walk(directory, topdown=False):
    for name in dirs:
        try:
            os.rmdir(os.path.join(root, name))
            print(f'Deleted directory: {os.path.join(root, name)}')
        except OSError:
            pass  # Directory not empty
