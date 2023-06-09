// var coll = document.getElementsByClassName("collapsible");
// var i;

// for (i = 0; i < coll.length; i++) {
// 	coll[i].addEventListener("click", function() {
// 	this.classList.toggle("activeCollapsible");
// 	var content = this.nextElementSibling;
// 	if (content.style.maxHeight){
// 		content.style.maxHeight = null;
// 	} else {
// 		content.style.maxHeight = content.scrollHeight + "px";
// 	} 
// 	});
// }

var coll = document.getElementsByClassName("collapsibleButton");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            this.innerHTML = "&#10507;"
            content.style.maxHeight = null;
            content.style.marginTop = "0px"
            this.style.top = "-25px"
            content.style.padding = "0px 18px"
        } else {
            this.innerHTML = "&#10506;"
            content.style.maxHeight = content.scrollHeight + "px";
            content.style.marginTop = "10px"
            this.style.top = "-35px"
            content.style.padding = "5px 18px"
        }
    }
    );
}