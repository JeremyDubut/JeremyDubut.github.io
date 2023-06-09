function openMenu() {
    sm = document.getElementById("sideMenu")
    sm.style.width = "250px";
    sm.style.boxShadow = "0 0 .2rem #0000001a,0 .2rem .4rem #0003";
    document.getElementById("main").style.opacity = "0.6";
    document.getElementById("mainTitle").style.opacity = "0.6";
}
  
function closeMenu() {
    sm = document.getElementById("sideMenu")
    sm.style.width = "0";
    sm.style.boxShadow = "";
    document.getElementById("main").style.opacity = "1";
    document.getElementById("mainTitle").style.opacity = "1";
}