# ddsclobber

[![Python application](https://github.com/Ganonmaster/ddsclobber/actions/workflows/python-app.yml/badge.svg)](https://github.com/Ganonmaster/ddsclobber/actions/workflows/python-app.yml)

Converts a DDS file, or folder with DDS files, to TGA, overwriting any file with the the tga extension that might already exists.

Written in python. Uses ImageMagick/Wand to do the conversion. Works on Windows, not tested on Mac or Linux, but should work.
  
## Instructions
 
 
- Download and install ImageMagick from https://imagemagick.org/script/download.php#windows
  You probably want this file: `ImageMagick-7.1.0-24-Q16-HDRI-x64-dll.exe`
- Download the latest ddsclobber.exe from here: https://github.com/Ganonmaster/ddsclobber/releases
- Drag a DDS file or folder of DDS files on top of the ddsclobber.exe file.
  .tga files should now be generated automatically.

If you receive errors, try running the program from the command line.
