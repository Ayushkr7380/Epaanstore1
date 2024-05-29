


function populateSelect() {
    for (var i = 0; i <= 100; i++) {
        $(".quantity").append('<option value="' + i + '">' + i + '</option>');
    }
}


// Call the populateSelect function when the page loads
window.onload = function() {
    populateSelect();
};



let logoutbutton = document.getElementById('logoutbutton');

function getCSRFToken() {
    const csrfTokenCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfTokenCookie) {
        return csrfTokenCookie.split('=')[1];
    }
    return null;
}
logoutbutton.addEventListener('click', function(event) {
    event.preventDefault();
    // let paancart = JSON.parse(localStorage.getItem('paancart'));
    let csrfToken = getCSRFToken();
    fetch(this.href, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        if(localStorage.getItem('paancart')){

            localStorage.removeItem('paancart');
            console.log('Cart cleared from localStorage');
        }
        // return response.json();
    })
    .then(data => {
        console.log('Logout successful:', data);
        window.location.href = '/auth/login';

    })
    .catch(error => {
        console.error('Error logging out:', error);
    });
});




