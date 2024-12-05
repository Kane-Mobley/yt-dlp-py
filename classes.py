from enum import Enum

class FileFormat(Enum):
    MP4 = 'mp4',
    MP3 = 'mp3',
    WEBM = 'webm'
    
class ImportType(Enum):
    BATCH = 'batch',
    LINK = 'link'