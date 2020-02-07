import config
from dropbox import Dropbox
from dropbox import files
from filer import Filer
from os import path

class PyDrop(object):

    db = Dropbox(config.ACCESS_TOKEN)
    user = db.users_get_current_account()

    def upload_files(self):
        filer = Filer()        
        for p in config.PATHS:
            # get url to zip file
            zipfile = filer.archive_file(p)
            dropfile = '/' + config.DROP_BOX_FOLDER + '/' + path.normpath(path.basename(zipfile))
            # upload file to dropbox
            with open(zipfile, 'rb') as f:
                self.db.files_upload(f.read(), dropfile, mode= files.WriteMode('overwrite'))
                # delete file after upload
                filer.delete_file(zipfile)