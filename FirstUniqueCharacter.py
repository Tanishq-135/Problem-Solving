string = "aabcc"
ch = ""

if len(string) == 0 :
    print("No Input String has been given")
else:
    for i in string:
        if string.count(i) == 1:
            ch = i
            break
    if ch:
        print("First non-repeating character is", ch)
    else:
        print("All characters are repeating")
