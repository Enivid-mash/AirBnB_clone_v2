#!/usr/bin/python3

import os
import datetime
from fabric.api import local


def do_pack():
    """
    A script that generates an archive of the contents of web_static folder
    It creates a timestamped filename and uses tar to create a .tgz archive.
    """

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    web_static_folder = 'web_static'
    versions_folder = 'versions'
    archive_filename = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join(versions_folder, archive_filename)

    try:
        os.makedirs(versions_folder, exist_ok=True)
        local(f'tar -czvf {archive_path} {web_static_folder}')
        return archive_path

    except Exception as e:
        return None
