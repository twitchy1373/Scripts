#!/bin/bash

case $1 in
	"" )
	echo "Please enter the network you would like to ping.  Please note
	 that pingsweep utilizes fping and will not work if fping is not
	 installed. Use fpingsweep -h for help.  Use fpingsweep -w to write to a file
	  where the file is specified after the network"
	 ;;
"-w")
fping -agq $2 > $3
;;
*)
fping -agq $1
;;
esac
