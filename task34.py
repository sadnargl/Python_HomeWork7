poem = input ("Введите кричалку Винни-Пуха: ",)
poem = poem.split ()
print (poem)

res = list (map (lambda x: x.count('а'), poem))
print (res)
if res.count (res[0]) == len (res):
    print ("Парам-пам-пам")
else:
    print ("Пам парарам")
