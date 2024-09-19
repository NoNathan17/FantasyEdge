let slideIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-slide');
    const totalSlides = slides.length;

    if (index >= totalSlides) {
        slideIndex = 0;
    } else if (index < 0) {
        slideIndex = totalSlides - 1;
    } else {
        slideIndex = index;
    }

    const newTransformValue = -slideIndex * 100;
    document.querySelector('.carousel-wrapper').style.transform = `translateX(${newTransformValue}%)`;
}

function moveSlide(step) {
    showSlide(slideIndex + step);
}

// Initialize the carousel
document.addEventListener('DOMContentLoaded', () => {
    showSlide(slideIndex);
});
