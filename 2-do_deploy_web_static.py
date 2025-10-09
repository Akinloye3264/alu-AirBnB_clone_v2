#!/usr/bin/python3
from fabric.api import env, put, run
import os

# Set environment variables for Fabric
env.hosts = ['54.242.117.7', '54.226.19.77']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive details
        archive_name = os.path.basename(archive_path)
        no_ext = archive_name.split('.')[0]
        release_path = f"/data/web_static/releases/{no_ext}"

        # Upload the archive to /tmp/ on the server
        put(archive_path, '/tmp/')

        # Create target directory
        run(f"mkdir -p {release_path}")

        # Uncompress the archive
        run(f"tar -xzf /tmp/{archive_name} -C {release_path}")

        # Delete the archive from /tmp/
        run(f"rm /tmp/{archive_name}")

        # Move contents out of web_static folder
        run(f"mv {release_path}/web_static/* {release_path}/")

        # Remove now-empty folder
        run(f"rm -rf {release_path}/web_static")

        # Remove old symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_path}/ /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
