# -le = less or equal
n=0
comand=$1 # Equivalente ao sys.argv[1] no python
while ! $comand && [ $n -le 5 ]; do # vai parar se o comando for sucesso ou depois de 5 tentativas
    sleep $n
    ((n=n+1))
    echo "retry #$n"
done;