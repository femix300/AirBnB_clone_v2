#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compress the web_static folder into a .tgz archive
    """
    try:
        # Create the "versions" folder if it doesn't exist
        local("mkdir -p versions")

        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Set the archive filename
        archive_filename = "versions/web_static_{}.tgz".format(timestamp)

        # Compress the contents of the web_static folder into the archive
        local("tar -cvzf {} web_static".format(archive_filename))

        # Check if the archive was created successfully
        if local("test -e {}".format(archive_filename)).succeeded:
            return archive_filename
        else:
            return None
    except Exception as e:
        return None
