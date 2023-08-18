// Function to get the CSRF token from cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Get references to the form and its input fields
    const loginForm = document.querySelector('#login-form');
    const usernameInput = document.querySelector('#username');
    const passwordInput = document.querySelector('#password');

    // Add an event listener to the form for form submission
    loginForm.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        console.log('Form submission event triggered.');

        // Get the input values
        const username = usernameInput.value;
        const password = passwordInput.value;

        console.log('Username:', username);
        console.log('Password:', password);

        // Create a new FormData object to send the data
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        console.log('FormData:', formData);

        // Perform an AJAX POST request
        fetch('.', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Identify the request as AJAX
                'X-CSRFToken': getCookie('csrftoken') // Get the CSRF token from cookies
            }
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response data:', data);

                // Handle the response data (e.g., redirect on success or display an error message)
                if (data.success) {
                    console.log('Login successful. Redirecting to:', data.redirect_url);
                    window.location.href = data.redirect_url; // Redirect on success
                } else {
                    console.log('Login failed. Error message:', data.error_message);

                    // Display an error message
                    const errorDiv = document.querySelector('.error');
                    errorDiv.textContent = data.error_message;
                }
            });
    });
});
