#1
rownanie = (512-282)/(47*48+5)
print(rownanie)

#2
print("Podaj x: ")
x = int(input())
y = x #zapis x poza pętlą żeby wyzerować na jej końcu
print(x, end=" ") #end=" " wymusza pisanie w tej samej linii
i = 2
while i<=5:
    x = x * i #pomnożenie x przez 2,3,4,5
    print("---", x, end=" ")
    i = i+1 #zwiększenie i o 1
    x = y #powrót do oryginalnego x

