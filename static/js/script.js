document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const menu = document.querySelector('.menu');
    const menuItems = document.querySelectorAll('.menu a');

    hamburgerMenu.addEventListener('click', function() {
        menu.classList.toggle('active');
        if (menu.classList.contains('active')) {
            hamburgerMenu.innerHTML = '&times;'; // Change to closing symbol
        } else {
            hamburgerMenu.innerHTML = '&#9776;'; // Change back to hamburger menu
        }
    });

    menuItems.forEach(function(item) {
        item.addEventListener('click', function() {
            menu.classList.remove('active');
            hamburgerMenu.innerHTML = '&#9776;'; // Change back to hamburger menu
        });
    });
});