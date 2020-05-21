f = open("log.txt", 'w')


def create_log_file():
    global f
    f = open("log.txt", 'w')
    f.write("Игра началась")
    f.close()


def read_log():
    global f
    f = open("log.txt", 'r')
    print(f.read())
    f.close()

def add_line(line):
    global f
    f = open("log.txt", "a")
    f.write("\n" + line)
    f.close()