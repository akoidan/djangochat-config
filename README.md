#sessionId=$(curl --form "config=@fontello-conf.json" http://fontello.com/)
echo $sessionId
#wget http://fontello.com/$sessionId/get -O fonts.zip
unzip fonts.zip -d ./fontello
dir=$(ls ./fontello)
cp -r ./fontello/$dir/font ./static
cp -r ./fontello/$dir/css ./static
cp ./fontello/$dir/demo.html ./static
rm -r ./fontello/
