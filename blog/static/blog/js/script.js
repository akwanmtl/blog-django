document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});


const editBlog = document.querySelectorAll(".edit-btn");
const icons = document.querySelectorAll(".btn-floating");

editBlog.forEach(edit => {
  edit.addEventListener('click', function(){
    if(edit.innerHTML === "Edit Blog"){
      edit.innerHTML = "Done"
      icons.forEach(icon => {
        icon.classList.remove('icon')
      })
    }
    else{
      
      edit.innerHTML = "Edit Blog"
      icons.forEach(icon => {
        icon.classList.add('icon')
      })
    }
  })
})