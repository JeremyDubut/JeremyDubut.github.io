def publicationItem(
    f: object,
    paperId: str
) -> ():
        
    f.write("\t<li class=\"publicationItem\" id="+str(paperId)+">\n")

def publicationAuthors(
    f: object,
    authors: list[tuple[str]]
) -> ():

    f.write("\t\t<span class=\"publicationAuthors\">\n")
    nb_auth = len(authors)
    for i, author in enumerate(authors):
        if i == 1 and nb_auth == 2:
            f.write(" and\n")
        elif i == nb_auth - 1:
            f.write(", and\n")
        elif not i == 0:
            f.write(",\n")
        publicationAuthor(f,author)
        if i == nb_auth - 1:
            f.write(".<br>\n")
    f.write("\t\t</span>\n")

def publicationAuthor(
    f: object, 
    author: tuple[str]
) -> ():

    # f.write("\t\t<div class=\"publicationAuthor\" id=\""+author[0]+"\">\n")
    if author[3] is None:
        f.write("\t\t\t"+author[1][0]+". "+author[2]+"")
    else:
        f.write("\t\t\t<a href=\""+author[3]+"\">"+author[1][0]+". "+author[2]+"</a>")


def publicationTitle(
    f: object,
    title: str
) -> ():

    f.write("\t\t<div class=\"publicationTitle\">"+title+".</div>\n")

def publicationInfo(
    f: object,
    venue: str,
    journal: str,
    vol: int,
    num: int,
    papnum: int,
    fpage: int,
    lpage: int,
    pub: str,
    year: int
) -> ():

    f.write("\t\t<div class=\"publicationInfo\">\n")
    f.write("\t\t\t")
    if venue is not None:
        f.write("In "+venue+", ")
    if journal is not None:
        f.write(journal+", ")
    if vol is not None:
        if num is not None:
            f.write(str(vol)+"("+str(num)+"), ")
        else:
            f.write(str(vol)+", ")
    if fpage is not None:
        if papnum is not None:
            f.write(str(papnum)+":"+str(fpage)+"-"+str(papnum)+":"+str(lpage)+", ")
    f.write(pub+", "+str(year)+".\n")
    f.write("\t\t</div>")