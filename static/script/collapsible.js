var expanded;

function setup() {
  var elements = document.getElementsByClassName('collapsible');
  var i;

  // setup
  for(i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", function(e) {
      // if( e.target !== this) return;
      if(expanded && expanded !== this) {
        expanded.classList.remove("expanded");
      }

      this.classList.toggle("expanded");
      if(this.classList.contains("expanded")) {
        expanded = this;
      }
    });
  }
}
