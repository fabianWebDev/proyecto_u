const d = document;

const checkbox = d.getElementById('menu-button'),
  menu = d.querySelector('.menu');

checkbox.addEventListener('change', (e) =>{
  e.target.checked 
    ? menu.classList.add('isOpen') 
    : menu.classList.remove('isOpen');
});
