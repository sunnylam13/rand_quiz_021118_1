# Randomized Multiple Choice Answer Quizzes with Answer Keys

## OVERVIEW

create quizzes and answers in random order, along with the answer key

## Goals

create 35 different quizzes

create 50 multi choice questions for each quiz in random order

provide correct answer and 3 random wrong answers for each question in random order

write quizzes to 35 text files

write the answer keys to 35 text files


## needs to do

store states and capitals in a dictionary

call open(), write(), close() for quiz and answer key text files

use random.shuffle() to randomize order of questions and multiple choice options

## GENERATE QUIZ FILES

Since this program will be randomly ordering the questions and answers, you’ll need to import the random module ➊ to make use of its functions. The capitals variable ➋ contains a dictionary with US states as keys and their capitals as values. And since you want to create 35 quizzes, the code that actually generates the quiz and answer key files (marked with TODO comments for now) will go inside a for loop that loops 35 times ➌. (This number can be changed to generate any number of quiz files.)

%s is use of formatters to sub in the variable after %

## Reference

ABSP: 303
