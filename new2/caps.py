import random
def get_pair(line):
    key, sep, value = line.strip().partition(" ")
    return str(key), value

with open("C:\sample\python\state_capitals.txt") as fd:
    d = dict(get_pair(line) for line in fd)
    print(d)

for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(d.keys())
    random.shuffle(states)

for questionNum in range(29):
    correctAnswer = d[states[questionNum]]
    wrongAnswers = list(d.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,              states[questionNum]))

for i in range(4):
    quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    quizFile.write('\n')
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[               answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
