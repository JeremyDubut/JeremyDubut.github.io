import os
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
)
logging.addLevelName(25,"sql query")
logging.addLevelName(26,"sql answer")
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
import timeit
from sqlite3 import connect

from publication_list.src.sql import select, innerJoin
from publication_list.src.html import (publicationItemOpen, publicationItemClose, publicationAuthors,\
    publicationTitle, publicationInfo, publicationCollapsibleButton, publicationCollapsibleContent, \
    publicationCollapsibleOpen, publicationCollapsibleClose, publicationListOpen, publicationListClose, \
    publicationComment)
from publication_list.src.fileManagement import partition
    
def main() -> ():

    try:

        # Preparing the html file
        (f,postfix) = partition("index2.html")

        # Connecting to the database
        conn = connect("publication_list/papers.db")
        cur = conn.cursor()

        # list of types of publications
        pub_typ = [
            ("\"journaly\"", "Journals"), 
            ("\"conference\"","Conferences"), 
            ("\"preprint\"","Preprints"), 
            ("\"thesis\"","Theses")
        ]

        for typ, head in pub_typ:

            # write header
            f.write("<h3>"+head+"</h3>\n\n")
            publicationListOpen(f,typ)
            # f.write("<ol class=\"publicationList\" reversed>\n")

            # Select all the papers
            sel = select([],"Papers", condition="Papers.Type="+typ, ordering="Papers.Id DESC")
            log.log(25,"\n"+sel)
            res = cur.execute(sel).fetchall()
            log.log(26,f"Query answered with:\n{res}")

            # joining authors with authorship in a temp table
            join = innerJoin("Authors", "Id", "Authorship", "AuthorId")

            for paperId, title, _, venue, journal, vol, num, papnum, fpage, lpage, pub, year, abstract, keywords, comment in res:

                # select the authors of the paper, by order
                cols = ["Authors.Id","Authors.FName", "Authors.LName", "Authors.url"]
                sel = select(cols, join, condition="Authorship.PaperId="+str(paperId), ordering="Authorship.AuthorOrder ASC")
                log.log(25,"\n"+sel)
                resp = cur.execute(sel).fetchall()
                log.log(26,f"Query answered with:\n{resp}")

                # select the links
                sel = select(["Links.Caption","Links.Url"], "Links", condition="Links.PaperId="+str(paperId))
                log.log(25,"\n"+sel)
                links = cur.execute(sel).fetchall()
                log.log(26,f"Query answered with:\n{links}")

                # writing
                publicationItemOpen(f,paperId,typ)
                publicationAuthors(f,resp)
                publicationTitle(f,title)
                publicationInfo(f,venue,journal,vol,num,papnum,fpage,lpage,pub,year)
                publicationComment(f,comment)
                publicationCollapsibleOpen(f)
                publicationCollapsibleButton(f)
                publicationCollapsibleContent(f, abstract, keywords, links)
                publicationCollapsibleClose(f)
                publicationItemClose(f)

            publicationListClose(f,typ)
            # f.write("</ol>\n\n")

    # Making sure the postfix is written up and everyting closed

    except Exception as e:
        for l in postfix:
            f.write(l)
        f.close()
        conn.close()
        raise Exception(e)

    else:
        for l in postfix:
            f.write(l)
        f.close()
        conn.close()
        log.info("Finishing process without error.")


if __name__ == "__main__":
    main()

