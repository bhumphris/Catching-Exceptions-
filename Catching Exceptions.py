fileIn = 'myfile.txt'
convertInput = 0
try:
    with open(fileIn, 'r') as f:
        file_content = f.read()
        print "Reading file: " + fileIn
    if not file_content:
        print "There is no data in file:" + fileIn
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror) + ': ' + fileIn

while True:
    try:
        userInput = raw_input("please enter an integer: ")
        userInput = int(userInput)
        break
    except ValueError:
        print("\nThat is not an integer. Please enter an integer: ")
