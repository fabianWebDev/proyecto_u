const d = document;

const checkbox = d.getElementById('menu-button'),
  nav = document.getElementById('navbarNav'),
  menu = d.querySelector('.menu');
  
checkbox.addEventListener('change', (e) =>{
  e.target.checked 
    ? menu.classList.add('isOpen') 
    : menu.classList.remove('isOpen');
});

const currentPath = window.location.pathname;
const links = nav.querySelectorAll('.nav-link');

document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('navbarNav');
  const currentPath = window.location.pathname;

  const links = nav.querySelectorAll('.nav-link');
  links.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  nav.addEventListener('click', (e) => {
    let target = e.target;
    if (target.tagName !== 'A') {
      target = target.closest('a');
    }

    if (target && target.classList.contains('nav-link')) {
      links.forEach(link => link.classList.remove('active'));
      target.classList.add('active');
    }
  });
});