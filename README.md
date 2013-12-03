ut-itunes-import
=========================

Import to iTunes from uTorrent

On Windows:

1. Close µTorrent
2. Locate your iTunes library's [Automatically Add to iTunes folder](http://support.apple.com/kb/HT3832 "Understanding the "Automatically Add to iTunes" folder") and
uTorrent's resume.dat file.
3. Open a command prompt and navigate to the ut-itunes-import directory
4. Run the following command ([Label] is optional):

        C:\> python import.py [Path_to_resume.dat] [Path_to_Add_to_iTunes_folder] [Label]

    or

        C:\> python import.py -h
        Usage: python import.py [Path_to_resume.dat] [Path_to_Add_to_iTunes_folder]
        Optional arguments: [Label] filters by the specified label(s)

Fork [the repository](https://github.com/smithbr/ut-itunes-import "ut-itunes-import") to start making your changes to the **master** branch.
