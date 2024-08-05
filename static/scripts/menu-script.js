const d = document;

const checkbox = d.getElementById('menu-button'),
  menu = d.querySelector('.menu');

checkbox.addEventListener('change', (e) =>{
  e.target.checked 
    ? menu.classList.add('isOpen') 
    : menu.classList.remove('isOpen');
});


e7011ef04b52442f930ec081a62faf05f54cec8c
