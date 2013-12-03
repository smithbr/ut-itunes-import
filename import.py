#!/usr/bin/env python

from bencode import *
import shutil
import os
import sys
import time
import tempfile


base_dir = tempfile.gettempdir() + "\\ut-itunes-import"
item_list = []
file_count = 0
file_types = ['.mp3',]


if "--help" in str(sys.argv[1]).lower():
    print """ Usage: python import.py [Path_to_resume.dat] [Path_to_Add_to_iTunes_folder] [Label(s) (optional)]
              Optional arguments: [Label] only import files with specified label(s)"""
    sys.exit()

if not os.path.isfile(str(sys.argv[1]).replace("\\","\\\\")) \
    or not os.path.isdir(sys.argv[2]):
        raise AssertionError("""Path does not exist. Please check your 
                                resume.dat and Add to iTunes folder paths 
                                are correct.""")
        sys.exit()
else:
    RESUME_DAT = sys.argv[1]
    ADD_TO_ITUNES_FOLDER = sys.argv[2]
    try:
        # Labels don't do anything right now, sorry
        CUSTOM_LABELS = sys.argv[3]
    except:
        pass

try:
    META_INFO_FILE = open(RESUME_DAT, 'rb')
    META_INFO_CONTENT = bdecode(META_INFO_FILE.read())
except Exception, e:
    raise Exception("Could not find resume.dat file! Message: %s" % str(e))

try:
    for torrent in META_INFO_CONTENT.keys():
        item_list.append(torrent)
        THIS_TORRENTS_FILE_LIST = []

        if torrent == 'rec' or torrent == '.fileguard':
            item_list.remove(torrent)
        else:
            if META_INFO_CONTENT[torrent]['labels'] == [] and META_INFO_CONTENT[torrent]['completed_on'] > 0:

                print "[uTorrent metadata] Name: %s " % str(torrent)
                print "[uTorrent metadata] Label(s): %s" % str(META_INFO_CONTENT[torrent]['labels'])
                print "[uTorrent metadata] Path: %s" % str(META_INFO_CONTENT[torrent]['path'])
                print "[uTorrent metadata] Completed: %s" % str(META_INFO_CONTENT[torrent]['completed_on'])

                FINISHED_FOLDER_PATH = str(base_dir + str(torrent.strip(".torrent")))

                print "Source: %s" % META_INFO_CONTENT[torrent]['path']
                print "Destination %s" % FINISHED_FOLDER_PATH
                print "Starting copy folder..."

                if not os.path.isdir(FINISHED_FOLDER_PATH):
                    try:
                        print "Copying the folder to %s..." % str(base_dir)
                        shutil.copytree(META_INFO_CONTENT[torrent]['path'], FINISHED_FOLDER_PATH)
                        print "Copy finished."
                    except Exception, e:
                        raise Exception("""Error: Something went wrong when copying the %s
                            directory to %s! Message: %s"""
                            % (META_INFO_CONTENT[torrent]['path'], FINISHED_FOLDER_PATH, str(e)))
                else:
                    print "Destination directory already exists. Skipping copy..."

                print "Scanning for file types %s..." + str(file_types)

                any_mp3s_in_here = False

                for media_file in os.listdir(FINISHED_FOLDER_PATH):
                    for filetype in file_types:
                        if media_file[-4:] == filetype:
                            ADD_TO_ITUNES_SOURCE_FILE = str(FINISHED_FOLDER_PATH + "\\" + media_file)
                            THIS_TORRENTS_FILE_LIST.append(ADD_TO_ITUNES_SOURCE_FILE)
                            any_mp3s_in_here = True
                            file_count += 1

                print "Found %s %s files..." % (str(file_count), str(file_types))

                if not THIS_TORRENTS_FILE_LIST == []:
                    print str(THIS_TORRENTS_FILE_LIST)

                if not file_count > 0:
                    print "Skipping copy..."
                else:
                    print "Copying files to %s" + str(ADD_TO_ITUNES_FOLDER)
                    for file in THIS_TORRENTS_FILE_LIST:
                        try:
                            print "Copying: %s..." % file
                            shutil.copy(file, ADD_TO_ITUNES_FOLDER)
                        except Exception, e:
                            raise Exception("""Error: There was an issue copying the %s
                                file to the Add To iTunes directory! Message: %s"""
                                % (file, str(e)))
                        print "Success."

                if THIS_TORRENTS_FILE_LIST == []:
                    print "KEEPING MOVED DIRECTORY INTACT SINCE THERE WERE NO MUSIC FILES MOVED..."
                else:
                    try:
                        print "Cleaning up..."
                        shutil.rmtree(FINISHED_FOLDER_PATH)
                    except Exception, e:
                        raise Exception(""""Error: Could not delete the folder %s!"""
                            % (FINISHED_FOLDER_PATH, str(e)))
                    print "Success."

                print "---"

except Exception, e:
    print "Error: Something went wrong. Message: %s" % str(e)

finally:
    print "Closing resume.dat..."
    META_INFO_FILE.close()
    print "Closed."
    print "Cleaning up leftover files..."
    try:
        shutil.rmtree(base_dir)
    except:
        pass
    print "All done."
