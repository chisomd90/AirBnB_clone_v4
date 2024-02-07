import os
import shutil

def copy_files(src_dir, dest_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # List files in the source directory
    files = os.listdir(src_dir)

    # Look for 100-hbnb.html or fallback to 8-hbnb.html
    html_file = '100-hbnb.html' if '100-hbnb.html' in files else '8-hbnb.html'

    # Copy files to the destination directory
    for filename in files:
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        shutil.copy2(src_file, dest_file)

    # Rename 100-hbnb.html to 0-hbnb.html
    os.rename(os.path.join(dest_dir, html_file), os.path.join(dest_dir, '0-hbnb.html'))

def main():
    src_dir = 'web_flask/templates'
    dest_dir = 'web_dynamic/templates'
    copy_files(src_dir, dest_dir)

if __name__ == '__main__':
    main()

