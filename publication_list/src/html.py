def publicationItem(
    f,
    paperId: str
) -> ():
        
    f.write("\t<li class=\"publicationItem\" id="+str(paperId)+">\n")

def publicationAuthors(
    f,
    authors: list[tuple[str]]
) -> ():

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

def publicationAuthor(
    f, 
    author: tuple[str]
) -> ():

    # f.write("\t\t<div class=\"publicationAuthor\" id=\""+author[0]+"\">\n")
    if author[3] is None:
        f.write("\t\t"+author[1][0]+". "+author[2]+"")
    else:
        f.write("\t\t<a href=\""+author[3]+"\">"+author[1][0]+". "+author[2]+"</a>")


def publicationTitle(
    f,
    title: str
) -> ():

    f.write("\t\t<div class=\"publicationTitle\">"+title+".</div>\n")