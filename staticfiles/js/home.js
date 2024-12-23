let currentIndex = 0;

function moveSlide(direction) {
    const carouselList = document.querySelector(".carousel-list");
    const slides = document.querySelectorAll(".carousel-slide");
    const totalSlides = slides.length;

    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    } else if (currentIndex >= totalSlides) {
        currentIndex = 0;
    }

    const offset = -currentIndex * 100; // Translate by 100% per slide
    carouselList.style.transform = `translateX(${offset}%)`;
}
