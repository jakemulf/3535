import reverse
import one


"""
Reverses the input, and then calls one on the reversal
"""

usage = """
Usage:
    python reverseAndOne.py <beats|segments> <inputFilename> <outputFilename>
"""

def main(toReverse, inputFilename, outputFilename):
    reverse.main(toReverse, inputFilename, "temp.mp3")
    one.main("temp.mp3",outputFilename)

if __name__ == '__main__':
    import sys
    import os.path
    try :
        toReverse = sys.argv[1]
        inputFilename = sys.argv[2]
        outputFilename = sys.argv[3]
    except :
        print usage
        sys.exit(-1)
    if not toReverse in ["beats", "segments"]:
        print usage
        sys.exit(-1)
    if os.path.isfile("temp.mp3"):
        print "File temp.mp3 exists. Remove before usage"
        sys.exit(-1)
    main(toReverse, inputFilename, outputFilename)
