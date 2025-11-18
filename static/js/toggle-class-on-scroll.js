function toggleClassOnScroll() {
    const goBackToTopElement = document.getElementById("go-back-to-top-btn");

    if (document.documentElement.scrollTop >= 515) goBackToTopElement.classList.add("show");
    else goBackToTopElement.classList.remove("show");
}

document.addEventListener("scroll", toggleClassOnScroll);