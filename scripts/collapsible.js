var coll = document.getElementsByClassName("collapsibleButton");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            this.innerHTML = "&#10507;";
            content.style.maxHeight = null;
            setTimeout(() => {  
                content.style.marginTop = "0px";
                this.style.top = "-25px";
                content.style.padding = "0px 18px";
            }, 200);
        } else {
            this.innerHTML = "&#10506;"
            content.style.maxHeight = content.scrollHeight + "px";
            content.style.marginTop = "10px";
            this.style.top = "-35px";
            content.style.padding = "5px 18px";
        }
    }
    );
}