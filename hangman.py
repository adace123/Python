def hangman():
    words = ["python", "java", "ruby", "javascript", "assembly"]
    choice = ""
    missed = 0
    randomWord = random.randint(0,len(words)-1)
    asterisks = len(words[randomWord]) * ["*"]

    while "*" in asterisks and choice!="n":
            letter = input("(Guess) Enter a letter in word " + "".join(asterisks) + " > ")

            if letter in words[randomWord] and letter not in asterisks:
                letterindex  = words[randomWord].index(letter)
                asterisks[letterindex] = letter

            elif letter in asterisks and asterisks.count(letter)>=words[randomWord].count(letter):
                print(letter,"is already in the word")
                missed+=1

            elif letter in asterisks and asterisks.count(letter)<words[randomWord].count(letter):
                #letterindex = "".join(words[randomWord]).rindex(letter)
                for i in range(asterisks.index(letter)+1,len(asterisks)-1):

                    letterindex = words[randomWord][i:].find(letter)

                    if letterindex>=0:
                        asterisks[letterindex+i] = letter

            else:
                print(letter,"is not in the word")
                missed+=1

            if "*" not in asterisks:
                print("The word is",words[randomWord]+". You missed",missed,"time(s)")
                choice = input("Continue? (y/n): ")
                if choice == "y":
                    hangman()
                else:
                    print("Thanks for playing!")

hangman()
