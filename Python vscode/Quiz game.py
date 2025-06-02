questions = ("Which of these organisms have only single hearts?",
             "Which planets is the hottest in solar system?",
             "Which element is found most in Earth atmosphere?",
             "Which organism has highest level of regeneration?",
             "What is largest organ in human body?",
             "How many chambers in human heart?",
             "What is hardest part in human body?" )
options =(("A.Squid","B.Platypus","C.Earthworm","D.None"),
          ("A.Mercury","B.Venus","C.Mars","D.Earth"),
          ("A.Oxygen","B.Nitrogen","C.Carbon-Dioxide","D.Hydrogen"),
          ("A.Axolotl","B.Starfish","C.Jellyfish","D.Octopus"),
          ("A.Intestine","B.Lungs","C.Oesophagus","D.None"),
          ("A.1","B.2","C.3","D.4"),
          ("A.Bone","B.Tooth","C.Cardiac muscle","D.Gray matter"))
answers =("D", "B", "B", "A", "D", "D", "B")
score = 0
guesses =[]
question_num = 0

for question in questions:
    print("------------------------------------------------------" )
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter A, B, C or D: ").capitalize()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f'Correct Answer is {answers[question_num]}')
    question_num +=1

print("------------------------------------------------------")
print('RESULTS')
print("------------------------------------------------------")

score = int(score/len(questions) * 100)
print(f"your score is {score}%")