from pathlib import Path
import os

import shutil
import zipfile
import send2trash

class FileNav:
    # Files and File Paths
    def set_path(self, specified_path):
        return Path(specified_path)

    def current_working_directory(self):
        return Path.cwd()

    def change_working_directory(self, specified_path):
        os.chdir(specified_path)

    def home_directory(self):
        return Path.home()

    # Handling Absolute and Relative Paths
    def is_path_absolute(self, specified_path):
        return Path(specified_path).is_absolute()

    def convert_to_absolute_path(self, specified_path):
        return os.path.abspath(specified_path)

    def get_relative_path(self, specified_path, start=None):
        return os.path.relpath(specified_path, start)

    # Getting the Parts of a File Path
    def get_anchor(self, specified_path):
        return Path(specified_path).anchor # C:/

    def get_parent(self, specified_path): # C:/Windows/Users/
        return Path(specified_path).parent

    def get_parents(self, specified_path):
        return Path(specified_path).parents

    def get_filename_with_extension(self, specified_path):
        return Path(specified_path).name

    def get_filename(self, specified_path):
        return Path(specified_path).stem

    def get_file_extension(self, specified_path):
        return Path(specified_path).suffix

    def get_driver(self, specified_path):
        return Path(specified_path).drive

    # Finding File Sizes and Folder Contents
    def get_file_size(self, specified_path):
        return os.path.getsize(specified_path)

    def get_list_of_filenames(self, specified_path):
        return os.listdir(specified_path)

    def get_list_of_filenames_by_glob(self, specified_path, pattern='*'):
        return list(Path(specified_path).glob(pattern))

    # Checking Path Validity
    def is_path_exists(self, specified_path):
        return Path(specified_path).exists()

    def is_file_and_path_exists(self, specified_path):
        return Path(specified_path).is_file()

    def is_directory_and_path_exists(self, specified_path):
        return Path(specified_path).is_dir()

class FileManipulate:
    # Creating New Folders
    def create_folders(self, specified_path): # C:\\delicious\\walnut\\waffles
        os.makedirs(specified_path)

    def create_folder(self, specified_path):
        Path(specified_path).mkdir()

    # Copying Files and Folders
    def copy_file(self, source_path, destination_path):
        shutil.copy(source_path, destination_path)

    def copy_folder_all_contents(self, source_path, destination_path):
        shutil.copytree(source_path, destination_path)

    # Moving and Renaming Files and Folders
    def move_file_or_folder(self, source_path, destination_path):
        shutil.move(source_path, destination_path)

    def rename_file(self, source_path, destination_path):
        shutil.move(source_path, destination_path)

    # Permanently Deleting Files and Folders
    def delete_file(self, specified_path):
        os.unlink(specified_path)

    def delete_empty_folder(self, specified_path):
        os.rmdir(specified_path)

    def delete_folder_all_contents(self, specified_path):
        shutil.rmtree(specified_path)

    # Safe Deletes
    def safe_delete(self, specified_path):
        send2trash.send2trash(specified_path)

    # Walking a Directory Tree
    def get_foldernames_subfolders_filenames(self, specified_path):
        return os.walk(specified_path)


class ZipFiles:
    # Compressing Files
    def read_zip_files(self, specified_path):
        zip_ = zipfile.ZipFile(specified_path)
        zip_.close()
        return zip_.namelist

    def get_zip_filename_size(self, specified_path, filename):
        zip_ = zipfile.ZipFile(specified_path)
        file = zip_.getinfo(filename)
        zip_.close()
        return file.file_size

    def get_zip_filename_compress_size(self, specified_path, filename):
        zip_ = zipfile.ZipFile(specified_path)
        file = zip_.getinfo(filename)
        zip_.close()
        return file.compress_size

    # Extracting from ZIP Files
    def extract_zip_all_contents(self, source_path, destination_path=None):
        zip_ = zipfile.ZipFile(source_path, destination_path)
        zip_.extractall()
        zip_.close()

    def extract_zip_content(self, source_path, filename, destination_path=None):
        zip_ = zipfile.ZipFile(source_path)
        zip_.extract(filename, destination_path)
        zip_.close()

    # Creating and Adding to ZIP Files
    def create_zip(self, destination_path, file_to_zip):
        zip_ = zipfile.ZipFile(destination_path, 'w')
        zip_.write(file_to_zip, compress_type=zipfile.ZIP_DEFLATED)
        zip_.close()

    def append_zip(self, destination_path, file_to_zip):
        zip_ = zipfile.ZipFile(destination_path, 'a')
        zip_.write(file_to_zip, compress_type=zipfile.ZIP_DEFLATED)
        zip_.close()

def main():
    # f = FileNav()
    # print(f.set_path('C:/Windows/System32/'))

    # print(f.current_working_directory())
    # print(f.home_directory())
    # print(f.is_path_absolute(f.current_working_directory()))
    # print(f.convert_to_absolute_path('.'))
    # print(f.get_relative_path('C:/Windows', f.current_working_directory()))
    # print(f.get_list_of_filenames_by_glob(f.current_working_directory(), '*.txt'))

    # e = FileManipulate()
    pass

if __name__ == '__main__':
    main()