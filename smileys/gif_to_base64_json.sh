filename='gif_base64.json'

function printJson() {
  echo "\"$1\" : {" >> $filename
  pattern="./$1/*.gif"
  files=($(ls $pattern))
  for i in "${files[@]}"
  do
     gif_file_name=$(echo "${i:0:-4}" | tail -c 5)
   base=$(cat "$i" |base64 -w 0)
   echo "  \"$gif_file_name\" : \"$base\"," >>  $filename
  done
  echo '},' >> $filename
}

dirs=("base" "girls" "extra")
echo '' > $filename
echo "{" >> $filename
for i in "${dirs[@]}";  do
  printJson "$i"
done
echo "}" >> $filename
