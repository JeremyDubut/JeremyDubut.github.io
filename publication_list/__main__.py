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
from publication_list.src.html import publicationItem, publicationAuthors, publicationTitle
    
def main() -> ():

    # Preparing the html file
    f = open("publication.html","w")
    f.write("<ol class=\"publicationList\">\n")

    # Connecting to the database
    conn = connect("publication_list/papers2.db")
    cur = conn.cursor()

    # Select all the papers
    sel = select([],"Papers")
    log.log(25,"\n"+sel)
    res = cur.execute(sel).fetchall()
    log.log(26,f"Query answered with:\n{res}")

    # joining authors with authorship in a temp table
    join = innerJoin("Authors", "Id", "Authorship", "AuthorId")

    for paperId, title in res:

        # select the authors of the paper, by order
        cols = ["Authors.Id","Authors.FName", "Authors.LName", "Authors.url"]
        sel = select(cols, join, "Authorship.PaperId="+str(paperId),"Authorship.AuthorOrder ASC")
        log.log(25,"\n"+sel)
        resp = cur.execute(sel).fetchall()
        log.log(26,f"Query answered with:\n{resp}")

        # writing
        publicationItem(f,paperId)
        publicationAuthors(f,resp)
        publicationTitle(f,title)

        # Select the authors information in order for a particular paper

    # # log.debug(f"{res.fetchall()}")
    # # for p_id, title, venue, year, comments, _, journal, volume,\
    # #     number, page_start, page_end, paper_number, publisher in res.fetchall():
    # for p_id, title in res.fetchall():
    #     f.write("\t<li id="+str(p_id)+">\n")
    #     join = cur.execute("SELECT Authors.Name FROM Authors INNER JOIN Authorship ON Authors.Id = Authorship.AuthorId WHERE Authorship.PaperId="+str(p_id)+" ORDER BY Authorship.AuthorOrder DESC;").fetchall()
    #     # authors = join.execute("SELECT Authors.Name FROM Authors WHERE (PaperId="+str(p_id)+") ORDER BY Authorship.AuthorOrder ASC;")
    #     # log.debug(f"{join.fetchall()}")
    #     l = len(join)
    #     f.write("\t\t")
    #     for i, name in enumerate(join):
    #         if i == l-2:
    #             if l == 2:
    #                 f.write(name[0]+" and ")
    #             else:
    #                 f.write(name[0]+", and ")
    #         elif i == l-1:
    #             f.write(name[0]+".<br>\n")
    #         else:  
    #             f.write(name[0]+", ")
    #     f.write("\t\t"+title+"\n")
    #     f.write("\t</li>\n")
    f.write("</ol>")
    f.close()
    conn.close()


if __name__ == "__main__":
    main()

