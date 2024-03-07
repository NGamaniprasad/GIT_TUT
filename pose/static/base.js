document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', function (event) {
        const usernameInput = document.getElementById('username');
        const passwordInput = document.getElementById('password');
        let isValid = true;

        // Simple validation: Ensure that username and password are not empty
        if (usernameInput.value.trim() === '') {
            isValid = false;
            alert('Please enter a username.');
        }

        if (passwordInput.value.trim() === '') {
            isValid = false;
            alert('Please enter a password.');
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});
