document.addEventListener("DOMContentLoaded", function () {
    // Change background color of the "Passenger" button on hover
    const passengerButton = document.querySelector(".passenger-button");
    passengerButton.addEventListener("mouseover", function () {
        passengerButton.style.backgroundColor = "#0056b3";
    });
    passengerButton.addEventListener("mouseout", function () {
        passengerButton.style.backgroundColor = "#007bff";
    });

    // Change background color of the "Driver" button on hover
    const driverButton = document.querySelector(".driver-button");
    driverButton.addEventListener("mouseover", function () {
        driverButton.style.backgroundColor = "#0056b3";
    });
    driverButton.addEventListener("mouseout", function () {
        driverButton.style.backgroundColor = "#007bff";
    });

    // Apply a subtle animation to the company logo
    const companyLogo = document.querySelector(".company-logo");
    companyLogo.addEventListener("mouseover", function () {
        companyLogo.style.transform = "scale(1.05)";
    });
    companyLogo.addEventListener("mouseout", function () {
        companyLogo.style.transform = "scale(1)";
    });

    // Create a fade-in effect for the content
    const content = document.querySelector(".content");
    content.style.opacity = 0;
    let opacity = 0;
    const fadeInInterval = setInterval(function () {
        opacity += 0.02;
        content.style.opacity = opacity;
        if (opacity >= 1) {
            clearInterval(fadeInInterval);
        }
    }, 50);

    // Display a welcome message with current date and time
    const welcomeMessage = document.createElement("p");
    welcomeMessage.textContent = `Welcome! Current date and time: ${new Date().toLocaleString()}`;
    content.appendChild(welcomeMessage);
});
