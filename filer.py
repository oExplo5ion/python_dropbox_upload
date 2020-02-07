import config
import shutil
import os
from zipfile import ZipFile

class Filer(object):

    _WORK_DIR = config.WORK_DIRECTORY + '\\py_drop'

    # public
    def __init__(self):
        self._create_work_dir()
        pass
    
    # returns url of archived file
    def archive_file(self, url = ''):
        # checks
        if url.lower().endswith('.zip'):
            return url
        if url.lower().endswith('.rar'):
            return url
        if self._create_work_dir() != True :
            return None
        if len(url) <= 0 :
            return None
        # prepeare urls
        furl = os.path.normpath(url)
        fname = os.path.basename(furl)
        # change working directory
        try:
            os.chdir(self._WORK_DIR)
        except OSError:
            print('Could not change working directory')
            return None
        # create zip
        return shutil.make_archive(fname, 'zip', furl)

    def delete_file(self, url):
        try:
            os.remove(url)
        except OSError:
            print('Could not delete file')
    
    # private
    def _create_work_dir(self):
        if os.path.exists(self._WORK_DIR):
            return True
        try:
            os.mkdir(self._WORK_DIR)
        except OSError:
            print('Failed to create work directory')
            return False
        return True
        