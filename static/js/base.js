function toggleMenu() {
    const menu = document.getElementById('nav-menu')
    menu.classList.toggle('show')
}

function closeMenu() {
    const menu = document.getElementById('nav-menu');

    if (window.innerWidth > 1250)
        menu.classList.remove('show')
}

window.addEventListener('resize', closeMenu)