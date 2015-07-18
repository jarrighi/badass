console.log("Let's race!!");

var dropZones = document.querySelectorAll('.pile');
var dragElements = document.querySelectorAll('.draggable');
var elementDragged = null;

// bind dragging event listeners to draggable items
for(var i = 0; i < dragElements.length; i++) {
  
  dragElements[i].addEventListener('dragstart', function(e) {
    console.log('Drag Interaction Started!');
    this.style.borderColor = 'black';
    e.dataTransfer.effectAllowed = 'move';
    elementDragged = this;
  });

  dragElements[i].addEventListener('dragend', function(e) {
    console.log('Drag Interaction Ended!');
    this.style.borderColor = 'white';
    elementDragged = null;
  });
};

// bind dragging event listeners to drag zones
for(var i = 0; i < dropZones.length; i++){

  dropZones[i].addEventListener('dragover', function(e){
    if (e.preventDefault) {
      e.preventDefault();
    }
    e.dataTransfer.dropEffect = 'move';
    return false;
  });

  dropZones[i].addEventListener('dragenter', function(e){
    elementDragged.style.backgroundColor = '#4466dd';
  });

  dropZones[i].addEventListener('dragleave', function(e){
    elementDragged.style.backgroundColor = 'rgba(255,255,255,.3)';
  });

  dropZones[i].addEventListener('drop', function(e){
    console.log("Dropped!");
    elementDragged.style.backgroundColor = 'rgba(255,255,255,.3)';
    this.appendChild(elementDragged);
  });
}