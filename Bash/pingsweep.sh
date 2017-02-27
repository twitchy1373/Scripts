#!/bin/bash
case $1 in
	"-a" )
	for x in `seq 1 254`; do
	ping -c 1 $2.$x.$x.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//'
done
		;;
		"-b" )
		for x in `seq 1 254`; do
		ping -c 1 $2.$x.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//'
	done
	;;
	"-c" )
	for x in `seq 1 254`; do
	ping -c 1 $2.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//'
done
;;
"-h" )
echo "Enter network class with args "-a" for type A, "-b" for type B, and
 "-c" for type C.  Then enter beginning of network range to scan.
 Ex: pingsweep.sh -c 192.168.1 pings 192.168.1.1-254 "
 ;;
 "")
 echo "Run pingsweep.sh -h for help"
esac
