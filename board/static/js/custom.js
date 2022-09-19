var row;

function start(){  
  row = event.target; 
}

function dragover(){
  var e = event;
  e.preventDefault(); 
  
  let children= Array.from(e.target.parentNode.parentNode.children);

  if(children.indexOf(e.target.parentNode)>children.indexOf(row))
    e.target.parentNode.after(row);
  else
    e.target.parentNode.before(row);
}

function dragend(){
  var e = event;
  e.preventDefault(); 
  let children= Array.from(e.target.parentNode.children);
  children.forEach(element => {
    console.log(element["id"]);
    console.log('-----------------------')
  });
}