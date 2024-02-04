const faq1 = document.getElementsByClassName('faq1')[0];
const faq2 = document.getElementsByClassName('faq2')[0];
const faq3 = document.getElementsByClassName('faq3')[0];
const faq4 = document.getElementsByClassName('faq4')[0];
const faq5 = document.getElementsByClassName('faq5')[0];
const faq6 = document.getElementsByClassName('faq6')[0];

function deactivateAllFAQs() {
  faq1.classList.remove("active");
  faq2.classList.remove("active");
  faq3.classList.remove("active");
  faq4.classList.remove("active");
  faq5.classList.remove("active");
  faq6.classList.remove("ctive");
}
  
faq1.addEventListener("click", () => {
    if (faq1.classList.contains("active")) {
        faq1.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq1.classList.add("active");
    }
});

faq2.addEventListener("click", () => {
    if (faq2.classList.contains("active")) {
        faq2.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq2.classList.add("active");
    }
});

faq3.addEventListener("click", () => {
    if (faq3.classList.contains("active")) {
        faq3.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq3.classList.add("active");
    }
});

faq4.addEventListener("click", () => {
    if (faq4.classList.contains("active")) {
        faq4.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq4.classList.add("active");
    }
});

faq5.addEventListener("click", () => {
    if (faq5.classList.contains("active")) {
        faq5.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq5.classList.add("active");
    }
});

faq6.addEventListener("click", () => {
    if (faq6.classList.contains("active")) {
        faq6.classList.remove("active");
    } else {
        deactivateAllFAQs();
        faq6.classList.add("active");
    }
});