#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
import os
import shutil
import uuid
import zipfile
from datetime import datetime
import hashlib

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


def encode_file_name(filename):
    now = datetime.now()
    encoded = hashlib.sha224(filename.encode('utf8')).hexdigest()
    return '{}{}'.format(now.isoformat(), encoded)

def directory_listing(folder_name, file_type=None):
    if not folder_name or str(folder_name).__eq__(''):
        raise Exception("Folder must not be empty.")
    files = []
    allfiles = os.listdir(folder_name)
    for x in allfiles:
        if not file_type:
            files.append(x)
        else:
            if str(x).endswith(file_type):
                files.append(x)
    return files


def file_info_gathering(filename):
    if not filename:
        raise Exception("The file name can not be empty")
    if not os.path.isfile(filename):
        raise Exception("The file" + filename + "does not exist or corrupt. Please check again.")
    info = os.stat(filename)
    return info


def get_file_name_extension(filename):
    splits = os.path.splitext(filename)
    name, ext = splits[0], splits[1]
    return name, ext


def copy_file(source_file, target_file):
    if not source_file:
        raise Exception("Check the input filename please. It can not be empty")
    if not os.path.isfile(source_file):
        raise Exception("File does not exist.")
    shutil.copy2(source_file, target_file)


def copy_directory(source_dir, target_dir):
    if not source_dir:
        raise Exception("Check the source directory name. It can not be empty.")
    if not target_dir:
        raise Exception("Check the destination directory name. It can not be empty.")
    shutil.move(source_dir, target_dir)


def copy_file_to_directory(source_file, target_dir):
    if not source_file:
        raise Exception("Check the source file name. It can not be empty.")
    if not target_dir:
        raise Exception("Check the destination directory name. It can not be empty.")
    shutil.move(source_file, target_dir)


def get_file_content(filename):
    if not filename:
        return None
    with open(filename, mode='r') as file:
        content = file.read()
    return content


def generate_id():
    return uuid.uuid4().hex


def unzip_file(filename, path_to_extract):
    if not filename:
        raise Exception("The " + filename.__str__ + " doest not exist. Please check again.")
    if not os.path.isfile(filename):
        raise Exception("File doest not exist. Please check again.")
    zip = zipfile.ZipFile(file=filename, mode='r')
    zip.extractall(path=path_to_extract)
    zip.close()
