/*eslint-env es6*/
const navSlide = () => {
     const linebar = document.querySelector('.linebar');
     const nav = document.querySelector('.rightmenu');
     const navLinks = document.querySelectorAll('.rightmenu li');



     linebar.addEventListener('click', () => {
           nav.classList.toggle('nav-active');

           navLinks.forEach((link, index) => {
                 if(link.style.animation){
                    link.style.animation = '';
                 } else {
                    link.style.animation = 'navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s';
                 }
           });
           linebar.classList.toggle('toggle');
    });
}

 navSlide();
