# you can use glob(* ?) to form lists
for fruit in peach orange apple; do # in bash the sequences are constructed just by listing the elements with space in between
    echo "I like this $fruit!"
done

echo

for file in *.HTM; do # vai percorrer a lista de arquivos gerados com glob
name=$(basename "$file" .HTM) # vai armazenar o resultado do basename sem o .HTM
echo mv "$file" "$name.html" # vai substituir a extensão com o mesmo nome de arquivo
done