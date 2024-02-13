import os
import shutil

def organize_desktop():
    # Define desktop directory
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Create folders if they don't exist
    folders = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'Documents': ['doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'ppt', 'pptx'],
        'Videos': ['mp4', 'avi', 'mkv', 'mov'],
        'Audios': ['mp3', 'wav', 'flac'],
        'Others': []
    }
    
    for folder in folders:
        folder_path = os.path.join(C:\Users\chelf\Downloads, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Move files to corresponding folders
    for file in os.listdir(desktop_path):
        if file != 'desktop_organizer.py':  # Exclude the script file itself
            file_path = os.path.join(desktop_path, file)
            if os.path.isfile(file_path):
                for folder, extensions in folders.items():
                    if file.split('.')[-1].lower() in extensions:
                        shutil.move(file_path, os.path.join(desktop_path, folder, file))
                        print(f'Moved "{file}" to {folder} folder.')
                        break
                else:
                    shutil.move(file_path, os.path.join(desktop_path, 'Others', file))
                    print(f'Moved "{file}" to Others folder.')

if __name__ == "__main__":
    organize_desktop()
