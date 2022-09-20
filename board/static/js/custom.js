var row;
order = {};

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
  value = 1;
  children.forEach(element => {
    order[element["id"]]=value;
    value += 1;
  });
  console.log('-----------------------')
  $.ajax(
    {
        type:"POST",
        url: "sort/1",
        data: order,
        success: function( data ) 
        {
            console.log($('#category').val())
        }
     })
}
