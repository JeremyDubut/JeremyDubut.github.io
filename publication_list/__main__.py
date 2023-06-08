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
    publicationTitle, publicationInfo)
from publication_list.fileManagement import partition
    
def main() -> ():

    try:

        # Preparing the html file
        (f,postfix) = partition("index2.html")
        f.write("<ol class=\"publicationList\" reversed>\n")

        # Connecting to the database
        conn = connect("publication_list/papers.db")
        cur = conn.cursor()

        # Select all the papers
        sel = select([],"Papers",ordering="Papers.Id DESC")
        log.log(25,"\n"+sel)
        res = cur.execute(sel).fetchall()
        log.log(26,f"Query answered with:\n{res}")

        # joining authors with authorship in a temp table
        join = innerJoin("Authors", "Id", "Authorship", "AuthorId")

        for paperId, title, typ, venue, journal, vol, num, papnum, fpage, lpage, pub, year in res:

            # select the authors of the paper, by order
            cols = ["Authors.Id","Authors.FName", "Authors.LName", "Authors.url"]
            sel = select(cols, join, "Authorship.PaperId="+str(paperId),"Authorship.AuthorOrder ASC")
            log.log(25,"\n"+sel)
            resp = cur.execute(sel).fetchall()
            log.log(26,f"Query answered with:\n{resp}")

            # writing
            publicationItemOpen(f,paperId)
            publicationAuthors(f,resp)
            publicationTitle(f,title)
            publicationInfo(f,venue,journal,vol,num,papnum,fpage,lpage,pub,year)
            publicationItemClose(f)

        f.write("</ol>\n")

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


if __name__ == "__main__":
    main()

