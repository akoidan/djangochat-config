#sessionId=$(curl --form "config=@fontello-conf.json" http://fontello.com/)
#echo $sessionId
#wget http://fontello.com/$sessionId/get -O fonts.zip
if [  -f "$1" ]; then
    unzip $1 -d ./fontello
    dir=$(ls ./fontello)
    cp -r ./fontello/$dir/font ./static
    cp -r ./fontello/$dir/css ./static
    cp ./fontello/$dir/demo.html ./static
    cp ./fontello/$dir/config.json ./
    rm -r ./fontello/
else
 echo "Pass path to archive downloaded from http://fontello.com/ as first argument"
fi
