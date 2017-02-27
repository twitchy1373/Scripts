#!/bin/bash
case $1 in
  "")
  echo "Please enter a youtube link or text file containing links to download from.
   Please note this program takes yuotube-dl as a dependency.  For installation,
    do (sudo) pip install youtube-dl."
;;
*.txt)
youtube-dl -x --audio-format mp3 -a $1 -o "~/Music/%(title)s.%(ext)s"
;;
*)
youtube-dl -x --audio-format mp3 $1 -o "~/Music/%(title)s.%(ext)s"
;;
esac
