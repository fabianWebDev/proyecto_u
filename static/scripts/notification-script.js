document.addEventListener('DOMContentLoaded', () => {
  const notifcations = document.querySelectorAll('.notification'),
    closeButtons = document.querySelectorAll('.close-btn');
    
  notifcations.forEach((el) => {
      el.classList.add('show');

      setTimeout(() => {
          el.classList.remove('show');
      }, 5000);
  });

  closeButtons.forEach((el) => {
      el.addEventListener('click', () => {
          const notification = el.closest('.notification');
          notification.classList.remove('show');
      });
  });
});