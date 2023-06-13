def splitText(
    f: object,
    abstract: str,
) -> ():

    if not (abstract == "" or abstract == " "):
        if len(abstract) > 80:
            pref = abstract[:80].rpartition(" ")[0]
        else:
            pref = abstract
        f.write("\t\t\t\t\t\t"+pref+"\n")
        splitText(f,abstract[len(pref)+1:])

# assume that there is at most one reference
# of the form [%id]
def placeholder(
    com: str
) -> str:

    if "%" in com:
        pref, _, suff = com.partition("%")
        iden, _, suff = suff.partition("]")
        return pref+"<a href=#"+iden+" class=\"placeholder\">0</a>]"+suff
    else:
        return com

def publicationItemOpen(
    f: object,
    paperId: str,
    typ: str
) -> ():
        
    f.write("\t\t\t<li class=\"publicationItem "+typ[1:-1]+"\" id="+str(paperId)+">\n")

def publicationAuthors(
    f: object,
    authors: list[tuple[str]],
    full: bool = False,
    me: bool = False
) -> ():

    if len(authors) > 0:
        f.write("\t\t\t\t<span class=\"publicationAuthors\">\n")
        nb_auth = len(authors)
        for i, author in enumerate(authors):
            if i == 1 and nb_auth == 2:
                f.write(" and\n")
            elif i == nb_auth - 1 and not i == 0:
                f.write(", and\n")
            elif not i == 0:
                f.write(",\n")
            publicationAuthor(f,author,full,me)
            if i == nb_auth - 1:
                f.write(".<br>\n")
        f.write("\t\t\t\t</span>\n")

def publicationAuthor(
    f: object, 
    author: tuple[str], 
    full: bool = False,
    me : bool = False
) -> ():

    if full:
        fname = author[1]
    else:
        fname = author[1][0]+"."

    if author[3] is None or ((not me) and author[0] == "me"):
        f.write("\t\t\t\t\t"+fname+" "+author[2]+"")
    else:
        f.write("\t\t\t\t\t<a href=\""+author[3]+"\">"+fname+" "+author[2]+"</a>")


def publicationTitle(
    f: object,
    title: str
) -> ():

    f.write("\t\t\t\t<div class=\"publicationTitle\">"+title+".</div>\n")

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

    f.write("\t\t\t\t<div class=\"publicationInfo\">\n")
    f.write("\t\t\t\t\t")
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
        else:
            f.write(str(fpage)+"-"+str(lpage)+", ")
    if year is not None:
        f.write(pub+", "+str(year)+".\n")
    else:
        f.write(pub+".\n")
    f.write("\t\t\t\t</div>\n")

def publicationItemClose(
    f: object
) -> ():
        
    f.write("\t\t\t</li>\n")

def publicationCollapsibleButton(
    f: object
) -> ():

    f.write("\t\t\t\t\t<button class=\"collapsibleButton\">\n")
    f.write("\t\t\t\t\t\t&#10507;\n")
    f.write("\t\t\t\t\t</button>\n")

def publicationCollapsibleContent(
    f: object,
    abstract: str,
    keywords: str,
    links: list[tuple[str]]
) -> ():

    f.write("\t\t\t\t\t<div class=\"collapsibleContent\">\n")
    f.write("\t\t\t\t\t\t<div class=\"collapsibleContentTitle\">Abstract:</div>\n")
    # f.write("\t\t\t\t"+abstract+"<br><br>\n")
    splitText(f,abstract)
    f.write("\t\t\t\t\t\t<br><br>\n")
    f.write("\t\t\t\t\t\t<div class=\"collapsibleContentTitle\">Key words:</div>\n")
    f.write("\t\t\t\t\t\t"+keywords+"\n")
    if not len(links) == 0:
        f.write("\t\t\t\t\t\t<br><br>\n")
        f.write("\t\t\t\t\t\t<div class=\"collapsibleContentTitle\">Links:</div>\n")
        f.write("\t\t\t\t\t\t<ul class=\"linksList\">\n")
        # f.write("\t\t\t\tTo be done\n")
        for caption, url in links:
            f.write("\t\t\t\t\t\t\t<li class=\"linksItem\"><a href="+url+">"+caption+"</a></li>\n")
        f.write("\t\t\t\t\t\t</ul>\n")
    f.write("\t\t\t\t\t</div>\n")

def publicationCollapsibleOpen(
    f: object
) -> ():

    f.write("\t\t\t\t<div class=\"collapsible\">\n")

def publicationCollapsibleClose(
    f: object
) -> ():

    f.write("\t\t\t\t</div>\n")

def publicationListClose(
    f: object,
    typ: str
) -> ():

    if typ == "\"conference\"" or typ == "\"journaly\"":
        f.write("\t\t</ol>\n\n")
    else:
        f.write("\t\t</ul>\n\n")

def publicationListOpen(
    f: object,
    typ: str
) -> ():

    if typ == "\"conference\"":
        f.write("\t\t<ol class=\"publicationList\" reversed>\n")
    elif typ == "\"journaly\"":
        f.write("\t\t<ol type=I class=\"publicationList\" reversed>\n")
    else:
        f.write("\t\t<ul style=\"list-style: none;\" class=\"publicationList\">\n")

def publicationComment(
    f: object,
    comment: str
) -> ():

    if comment is not None:
        f.write("\t\t\t\t<div class=\"publicationComment\">"+placeholder(comment)+".</div>\n")
