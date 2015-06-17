ut-itunes-import
=========================

Import to iTunes from µTorrent

## Prerequisites:
* [Locate your iTunes library's Automatically Add to iTunes folder](http://support.apple.com/kb/HT3832 "Understanding the "Automatically Add to iTunes" folder")
* Locate the resume.dat file (Usually found in `%appdata%\µTorrent`)

## On Windows

Download a [copy](https://github.com/smithbr/mint-backup/archive/master.zip) of this repo

Close µTorrent.

Open a command prompt and navigate to extracted directory: `cd C:\ut-itunes-import`

### Usage
        C:\> python import.py [Path_to_resume.dat] [Path_to_Add_to_iTunes_folder] [Label(s) (optional)]

### Help

        C:\> python import.py --help
        Usage: python import.py [Path_to_resume.dat] [Path_to_Add_to_iTunes_folder] [Label(s) (optional)]
        Optional arguments: [Label] only import files with specified label(s)
