# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

#####################################
# IMPORTS
#####################################

import random

#####################################
# END IMPORTS
#####################################

#####################################
# QUIZ DATA
#####################################

# keys are provinces and values capitals

capitals = {
	'Alabama':'Montgomery',
	'Alaska':'Juneau',
	'Arizona':'Phoenix',
	'Arkansas': 'Little Rock', 
	'California': 'Sacramento', 
	'Colorado': 'Denver',
	'Connecticut': 'Hartford', 
	'Delaware': 'Dover', 
	'Florida': 'Tallahassee',
	'Georgia': 'Atlanta', 
	'Hawaii': 'Honolulu', 
	'Idaho': 'Boise', 
	'Illinois':'Springfield', 
	'Indiana': 'Indianapolis', 
	'Iowa': 'Des Moines', 
	'Kansas':'Topeka', 
	'Kentucky': 'Frankfort', 
	'Louisiana': 'Baton Rouge', 
	'Maine':'Augusta', 
	'Maryland': 'Annapolis', 
	'Massachusetts': 'Boston', 
	'Michigan':'Lansing', 
	'Minnesota': 'Saint Paul', 
	'Mississippi': 'Jackson', 
	'Missouri':'Jefferson City', 
	'Montana': 'Helena', 
	'Nebraska': 'Lincoln', 
	'Nevada':'Carson City', 
	'New Hampshire': 'Concord', 
	'New Jersey': 'Trenton', 
	'New Mexico': 'Santa Fe', 
	'New York': 'Albany', 
	'North Carolina': 'Raleigh',
	'North Dakota': 'Bismarck', 
	'Ohio': 'Columbus', 
	'Oklahoma': 'Oklahoma City',
	'Oregon': 'Salem', 
	'Pennsylvania': 'Harrisburg', 
	'Rhode Island': 'Providence',
	'South Carolina': 'Columbia', 
	'South Dakota': 'Pierre', 
	'Tennessee':'Nashville', 
	'Texas': 'Austin', 
	'Utah': 'Salt Lake City', 
	'Vermont':'Montpelier', 
	'Virginia': 'Richmond', 
	'Washington': 'Olympia', 
	'West Virginia': 'Charleston', 
	'Wisconsin': 'Madison', 
	'Wyoming': 'Cheyenne'
}

#####################################
# END QUIZ DATA
#####################################

#####################################
# GENERATE QUIZ FILES
#####################################

for quizNum in range(35):
	# create the quiz and answer key files
	quizFile = open('capitalquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	# write out the header for the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# shuffle the order of the states
	states = list(capitals.keys())
	random.shuffle(states)

	# loop through all 50 states, making a question for each
	# create answer options
	for questionNum in range(50):
		# get right and wrong answers
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values()) # duplicate *all* the values in the `capitals` dict
		del wrongAnswers[wrongAnswers.index(correctAnswer)] # delete the correct answer
		wrongAnswers = random.sample(wrongAnswers, 3) # select 3 random values from this list
		answerOptions = wrongAnswers + [correctAnswer] # this is a concat list, the full list of answer is a combo of 3 wrong and 1 right
		random.shuffle(answerOptions) # answers randomized so correct response ain't always choice D
	
		# write the question and answer options to the quiz file
		quizFile.write('%s. What is the capital of the %s?\n' % (questionNum + 1, states[questionNum]))
		# generate the multiple choice answers to populate
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i])) # 'ABCD'[i] treats 'ABCD' as an array and will evaluate to A, B, C, D on each loop run through
			quizFile.write('\n')

		# write the answer key to a file
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) # finds the integer index of the correct answer in the randomly ordered answer options
		# 'ABCD'[answerOptions.index(correctAnswer)] evaluates to the correct answer's letter to be written to the answer file
	quizFile.close()
	answerKeyFile.close()

#####################################
# END GENERATE QUIZ FILES
#####################################
