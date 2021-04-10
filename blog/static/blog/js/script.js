document.addEventListener('DOMContentLoaded', function() {
  var elemsNav = document.querySelectorAll('.sidenav');
  var elemsModal = document.querySelectorAll('.modal');
  var instancesNav = M.Sidenav.init(elemsNav);
  var instancesModal = M.Modal.init(elemsModal);
  
  function closeNav () {
    elemsNav.forEach(nav =>{
      const instance = M.Sidenav.getInstance(nav);
      instance.close();
    })
  }

  const editBlog = document.querySelectorAll(".edit-btn");
  const icons = document.querySelectorAll(".btn-floating");

  editBlog.forEach(edit => {
    edit.addEventListener('click', function(){
      console.log(edit.innerHTML)
      if(edit.innerHTML === "Edit Posts"){
        icons.forEach(icon => {
          icon.classList.remove('scale-out')
        })
        edit.innerHTML = "Save Blog"
      }
      else{
        
        icons.forEach(icon => {
          icon.classList.add('scale-out')
        })
        edit.innerHTML = "Edit Posts"
      }
      closeNav();
    })
  })

  const editPost = document.querySelectorAll(".edit-post");
  const deletePost = document.querySelectorAll(".delete-post");

  editPost.forEach(element => {
    element.addEventListener('click', function(){
      const id = element.getAttribute('data-id');
      console.log("/edit/"+id)
      location.href = "/edit/"+id;
    })
  })

  const confirmModal = document.getElementById("confirm-delete-modal");


  deletePost.forEach(element => {
    element.addEventListener('click', function(){
      console.log(element.getAttribute('data-id'));
      
      const instance = M.Modal.getInstance(confirmModal);
      confirmModal.setAttribute('data-id',element.getAttribute('data-id'))
      instance.open();
    })
  })

  function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

  const deleteYes = document.getElementById("delete-yes");
  if(deleteYes){
    deleteYes.addEventListener('click', function(){
      const id = deleteYes.parentElement.parentElement.getAttribute('data-id')
      console.log('deleting '+ id);
      fetch('/delete/'+id, {
        method:"delete",
        headers: { 
          "X-CSRFToken": getCookie("csrftoken"),
          "Accept": "application/json",
          "Content-Type": "application/json" 
        }
      }).then(response => {
        location.reload()
      })
      .catch(err => console.log(err))    
    })
  }
  

});


