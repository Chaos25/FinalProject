import sys
sys.path.insert(0, 'D:/CHA/CHAFile')

from ChaFile import *
cha = ChaFile('D:/Voices-AWS/reading/24mb.cha')
lines = cha.getLines()

# Define the output file path
output_path = 'D:/Voices-AWS/reading/24mb.align'

# Open the output file in write mode
with open(output_path, 'w', encoding='utf-8') as output_file:
    for line in lines:
        utterance = line[LINE_UTTERANCE]
        # Ensure that timestamp is a list/tuple of [start, end]
        timestamp = line[LINE_BULLET]
        start, end = timestamp
        # Write the formatted line to the output file
        output_file.write(f"{start} {end} {utterance}\n")
