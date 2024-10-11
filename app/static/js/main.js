const navLinks = document.getElementById('link');


navLinks.forEach(link => {

  link.addEventListener('click', () => {

    navLinks.forEach(l => l.classList.remove('active'));

    link.classList.add('active');

  });

});