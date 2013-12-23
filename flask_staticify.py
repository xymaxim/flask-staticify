# coding: utf-8

import os

from flask import current_app, send_from_directory
from werkzeug.exceptions import NotFound


def _fallback_to(folder):
    def send_static(filename):
        """Serves files from the static folder if they exist or
        use a mounting folder as a fallback.
        """
        try:
            return current_app.send_static_file(filename)
        except NotFound:
            directory = os.path.join(current_app.root_path, folder)
            return send_from_directory(directory, filename)

    return send_static

def mount_folder(app, folder):
    app.view_functions['static'] = _fallback_to(folder)