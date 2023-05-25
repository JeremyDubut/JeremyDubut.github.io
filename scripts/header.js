var hd = document.getElementById("header")

if (hd.position = "sticky")
    {window.onscroll = function() {scrollFunction()};}

function scrollFunction() {
  if (document.body.scrollTop > 5 || document.documentElement.scrollTop > 5) {
    hd.style.boxShadow = "0 0 .2rem #0000001a,0 .2rem .4rem #0003";
  } else {
    hd.style.boxShadow = "";
  }
}