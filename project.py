#score is zero(0) because quiz has not started and goes up when score increases 
score = 0
#create a dictionary with the questions inside a list
quiz_pocket = [
    {
       'question': 'what is the square of 5?',
        'choices': 'A) 10 B) 25 C) 30',
        'answer': 'B'   
    },
    {
        'question': 'result for 5 + 3 * 2',
        'choices': 'A) 16 B) 11 C) 13 D) 20',
        'answer': 'B'  
    },
    {
        'question': 'calculate the perimeter of a rectangle; lenth is 24cm and width is 13cm.',
        'choices': 'A) 74cm B) 37cm C) 48cm D) 66cm',
        'answer': 'A' 
    },
    {
        'question': 'what is the chemical element for Au?',
        'choices': 'A) Gold B) Silver C) Sodium D) potassium',
        'answer': 'A' 
    },
    {
        'question': 'in which year did Kenya gain independence?',
        'choices': 'A) 1950 , B) 1972 C) 1964 D) 1963',
        'answer': 'D'
    },
]
#welcoming the user  
print('Welcome to Hotpoint Quiz')
#asking for user's name
user_name = input('enter your name: ')
#motivating user
print(f'All the best!, {user_name}')
#using for loop to iterate through questions
for item in quiz_pocket:
    #retriving the question and choices
    prompt_txt = print(f'{item['question']} [{item['choices']}]  your answer: ')
    #user inputs answer/choice
    user_choice = input('prompt_txt')
    #comparing answers while using .strip().upper() to clean and modify text data
    if user_choice.strip().upper() == item['answer']:
        print('correct: ')
        score = score + 1
    else:
        print(f'wrong. the correct answer was {item['answer']}')
#final results
#calculating score
#len looks at the number of questions in the dictonary
print(f'Quiz done! final score is: {score}/{len(quiz_pocket)}')
#using chained conditions 'else-if'
if score == len(quiz_pocket):
    print('Feedback: excellent!')
elif score >= len(quiz_pocket) / 2:
    #divide the total questions by 2 to check if score is greater than or equal to half the total score 
    print('Feedback: good')
else: 
    print('Feedback: try again')