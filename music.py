import random

chordTransitions = [[0, .1, 0, .4, .3, .1, 0], \
                    [.3, 0, .3, .1, .3, 0, 0], \
                    [0, .25, 0, .4, .25, .1, 0], \
                    [.2, .1, .3, 0, .4, 0, 0], \
                    [.3, .15, .2, .2, 0, .15, 0], \
                    [0, .35, 0, .1, .25, 0, .2], \
                    [.5, 0, .1, .1, .3, 0, 0]]

chords = ["C", "Dm", "Em", "F", "G", "Am", "Bm"]

rhythmTransitions = [[.7, .3], \
                     [.3, .7]]

lengths = [.25, .125]

#noteTransitions = [[.1, .2, .1, .1, .35, .1, .05], \
#                   [.2, .1, .3, .15, .2, .025, .025], \
#                   [.1, .2, .1, .3, .2, .05, .05], \
#                   [.15, .05, .2, .1, .4, .05, .05], \
#                   [.3, 0, 0, .3, 0, .2, .2], \
#                   [.1, .05, .05, .1, .3, .1, .3], \
#                   [.3, .05, 0, .05, .25, .3, .05]]

noteTransitions = [[0, .25, .25, .25, .25], \
                   [.25, 0, .25, .25, .25], \
                   [.25, .25, 0, .25, .25], \
                   [.25, .25, .25, 0, .25], \
                   [.25, .25, .25, .25, 0]]

#notes = ["C", "D", "E", "F", "G", "A", "B"]
notes = ["C", "D", "D", "G", "A"]

def pickRandomIndex(li):
    # Given a list li that contains the probabilities of integers
    # 0, 1, ..., len(li) - 1, pick an integer at random
    cumProb = 0.0
    randVal = random.random()
    index = -1
    while randVal >= cumProb:
        index = index + 1
        cumProb = cumProb + li[index]

    return index

def generateChain(start, steps, transitions):
    # Generates a chain of states represented by a list of integers
    # Based on the probabilities in the transitions 2D list
    progression = []
    state = start
    for i in range(steps):
        progression.append(state)
        state = pickRandomIndex(transitions[state])

    return progression

def printChordProgression(progression):
    # Output a list of integers as chords
    for i in range(len(progression)):
        print(chords[progression[i]], end=" ")

    print("")

def printMelody(noteProgression, rhythmProgression):
    # noteProgression and rhythmProgression must be lists of same lengths
    # For example, noteProgression[n] represents the tone of the nth note,
    # and rhythmProgression[n] represents that note's length (e.g. quarter note)
    for i in range(len(noteProgression)):
        print(notes[noteProgression[i]], end="")
        print(lengths[rhythmProgression[i]], end=" ")
    print("")

def generateRhythmProgression(start, measures, rhythmTransitions):
    # Generate a rhythmProgression that uses of the space of a Given
    # number of measures, assuming 4/4 time
    length = 0.0
    progression = []
    state = start
    while length < measures:
        if (measures - length) == .125:
            progression.append(1)
            length += .125
        progression.append(state)
        length += lengths[state]

        state = pickRandomIndex(rhythmTransitions[state])

    return progression

def createAndPrintMelody(startNote, startRhythm, measures):
    # A melody is stored as two separate lists: one representing tones
    # and another representing lengths of notes
    rhythmProgression = generateRhythmProgression(startRhythm, measures, \
                                                  rhythmTransitions)
    noteProgression = generateChain(startNote, len(rhythmProgression), \
                                    noteTransitions)
    printMelody(noteProgression, rhythmProgression)

createAndPrintMelody(0, 0, 2.0)
