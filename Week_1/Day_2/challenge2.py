"""
#### Rules:

* Rock beats scissors
* Scissors beats paper
* Paper beats rock

#### Concepts Used

* Loops( for,while etc.)
* if else

#### Function Template

* def compare(user1_answer='rock',user2_answer='paper')

#### Error Handling
* If the user_answer input is anything other than 'rock','paper' or 'scissors' return a string stating 'invalid input'

#### Libraries needed
* sys - to accept user input."""

def compare(u1, u2):
    inputVerify = {'rock', 'paper', 'scissors'}
    if u1 not in inputVerify or u2 not in inputVerify:
        return "Invalid input! You have not entered rock, paper or scissors, try again."
    
    if u1 == u2:
        return "It's a tie"

    if u1 == "rock":
        if u2 == "scissors":
            return "Rock wins!"
        elif u2 == "paper":
            return "Paper wins!"
    elif u1 == "scissors":
        if u2 == "rock":
            return "Rock wins!"
        elif u2 == "paper":
            return "Scissors wins!"
    elif u1 == "paper":
        if u2 == "scissors":
            return "scissors wins!"
        elif u2 == "rock":
            return "Paper wins!"

user1_answer = input("do yo want to choose rock, paper or scissors?")
user2_answer = input("do you want to choose rock, paper or scissors?")

print(compare(user1_answer, user2_answer))
