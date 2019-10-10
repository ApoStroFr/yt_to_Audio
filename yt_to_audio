#bin/bash
if [ "$1" = "-u" ]
then
	echo $1
	itag=`pytube $2 --list | grep -F "audio/mp4" | cut -d'"' -f2`
	pytube $2 --itag $itag

elif [ "$1" = "-f" ]
then
	while read line
	do
		itag=`pytube $2 --list | grep -F "audio/mp4" | cut -d'"' -f2`
		pytube $line --itag $itag
	done	< $3
elif [ "$1" = "-m" ]
then
	ffmpeg -i "$2" "$3"

elif [ "$1" = "-h" ]
then
	echo "Below the command line possible :"
	echo "	-u [YOUTUBE URL] : Télécharge la vidéo youtube si celle-ci dure moins de 20 minutes "
	echo "	-f [File contain YOUTUBE URL] : Télécharge la totalité des vidéos youtube ayant leur lien dans le fichier"
	echo "	-m [MP4 source file] [MP3 destination file] : Créer un fichier audio MP3 à partir d'un fichier MP4"
	echo "	-h : Command guideline"
else
	echo "Syntax Error : write \"-h\" to discover the command guideline"
fi
