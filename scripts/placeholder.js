var ph = document.getElementsByClassName("placeholder");
var conf = document.getElementsByClassName("conference");
var i;
var id;
var j;

for (i = 0; i < coll.length; i++) {
    j = 0;
    id = ph[i].getAttribute("href").substring(1);
    while ((! (id == conf[j].getAttribute("id"))) && (j < conf.length)) {
        j++;
    }
    ph[i].innerHTML = "hi"
    if (! (j == conf.length)) {
        ph[i].innerHTML = String(conf.length-j);
    }
    else {
        ph[i].innerHTML = "error"
    }
}