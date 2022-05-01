import sys, os
import subprocess, shlex
import json
import shutil
from StickerUtils import *

def getLocationsFile():
	return os.path.join(os.path.expanduser('~'), "Documents/locations.json")

def getDefaultStorageLocation():
	return os.path.join(os.path.expanduser('~'), "Downloads/")

def zipDir( dirLocation : str, outputLocation : str ):
    shutil.make_archive(outputLocation, 'zip', dirLocation)
    print(f" files saved to {outputLocation}")


def createStickerFiles( stickerName : str,\
    stickerImageDir : str,\
    outputLocation : str  ) -> str:
    # create new folder to zip
    # add index, sticker, png files
    os.system(f"mkdir {stickerName}")
    os.system(f'cp "{stickerImageDir}"  {stickerName}/{stickerName}.png')
    os.system(f'echo "{getStickerEntityData(stickerName)}" > {stickerName}/{stickerName}.sticker')
    os.system(f'echo "{getIndexFileData(stickerName)}" > {stickerName}/index.yaml')
    return os.path.join(os.getcwd(), stickerName)

def deleteFiles( location : str ):
    os.system(f"rm -rf {location}")


def transformAndSave( 
    stickerName : str,\
    stickerImageDir : str,\
    outputLocation : str ):
    
    s = createStickerFiles( stickerName, stickerImageDir, outputLocation )
    zipDir( s, f"{outputLocation}/{stickerName}" )
    deleteFiles( s )


    