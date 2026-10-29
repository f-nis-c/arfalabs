#!/usr/bin/env bash
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT
cd "$d"
printf 'Linea 1 de prueba\nLinea 2 con palabra clave\nLinea 3 final\n' >editor.txt
t=(
"pwd~where location path here~Print the current folder~pwd"
"ls~list show files folder~List files~ls -lah"
"mkdir~create new folder~Make a folder~mkdir -p dir1/sub_dir && ls"
"touch~create new empty file~Make an empty file~touch a.txt b.md && ls"
"cp~copy duplicate backup~Copy a file~cp editor.txt copia.txt && ls"
"mv~move rename~Move or rename a file~mv editor.txt nuevo.txt && ls"
"rm~delete remove erase~Delete a file~rm editor.txt && ls"
"echo~print say text~Print a line~echo 'Unicorns are the national animal of Scotland'"
">~write overwrite save file~Write text into a file~echo 'Welcome to the zoo' > zoo.txt && cat zoo.txt"
">>~add append file end~Add a line to a file~echo 'Welcome to the zoo' > zoo.txt; echo 'Unicorns are the national animal of Scotland' >> zoo.txt; cat zoo.txt"
"sed~replace swap word~Swap a word in a file~echo 'Scotland' > zoo.txt; sed -i 's/Scotland/Narnia/' zoo.txt; cat zoo.txt"
"tee~save show both~Show and save at once~echo Hello | tee zoo.txt"
"cat~read show print file~Print a file~cat editor.txt"
"head~first top lines~First lines~head -n 2 editor.txt"
"tail~last bottom lines~Last lines~tail -n 1 editor.txt"
"grep~search find word~Find lines with a word~grep palabra editor.txt"
"find~locate files name~Find files by name~find . -type f -name '*.txt'"
"wc~count lines words~Count lines~cat editor.txt | grep Linea | wc -l"
"math~arithmetic add multiply~Whole number arithmetic~echo \$((15 + 27))"
"bc~decimal fraction divide~Decimal arithmetic~echo 'scale=2; 10 / 3' | bc"
"printf~format type convert~Choose the output type~printf '%d %s %.1f\n' 42 unicorn 42"
"chmod~permission access~Change permissions~chmod 644 editor.txt && ls -l editor.txt"
"ps~process running~List processes~ps aux | head -n 3"
"kill~stop terminate~Stop a process~sleep 9 & kill -9 \$!; echo stopped"
"for~loop repeat each~Repeat for each item~for i in {1..3}; do echo Iteracion \$i; done"
"if~condition compare test~Decide with a test~N=15; if [ \$N -gt 10 ]; then echo mayor; else echo menor; fi"
)
l(){
for i in "${!t[@]}";do
[[ ${t[i],,} == *"${1,,}"* ]]&&{ IFS='~' read -r a b c e <<<"${t[i]}";echo "$((i+1)) $a: $c";}
done
}
l "$1"
while read -rp "word or number, q quits: " w;do
[[ $w == q ]]&&break
if [[ $w =~ ^[0-9]+$ && $w -ge 1 && $w -le ${#t[@]} ]];then
IFS='~' read -r a b c e <<<"${t[w-1]}"
echo "\$ $e"
eval "$e"
else
l "$w"
fi
done
