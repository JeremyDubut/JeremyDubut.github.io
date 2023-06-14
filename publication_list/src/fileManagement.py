from datetime import datetime

def partition(filename: str) -> (object,list[str]):

    # get the lines
    f = open(filename,"r")
    lines = f.readlines()
    f.close()

    g = open(filename,"w")

    prefix, postfix = [], []
    pref_done = False
    for i, l in enumerate(lines):
        if pref_done and l == "\t<!-- tag for end of action -->\n":
            postfix = lines[i:]
            break
        elif not pref_done: 
            if l == "\t<!-- tag for action -->\n":
                pref_done = True
                g.write(l)
                g.write("\t<!-- Last update on "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" -->\n")
                g.write("\n")
            else:
                g.write(l)

    return (g,postfix)

