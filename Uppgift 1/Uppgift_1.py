a = int(input("Hur manga sekunder mellan vare eaten carrot does Tor wait?"))
b = int(input("Hur manga sekunder mellan vare eaten carrot does Mor wait?"))

if a>b:
    c = a/b
    print("Tor eats ", ((40/c)/2), "carrots\nMor eats ", 40-(40/c)/2,"carrots")
elif a<b:
    c = b/a
    print("Mor eats ", ((40/c)/2), "carrots\nTor eats ", 40-(40/c)/2,"carrots")
else:
    print("They eat 20 carrots each")