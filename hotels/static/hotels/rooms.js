document.addEventListener('DOMContentLoaded', () => {
    const url = 'http://127.0.0.1:8000/attractions';
    // Call our API for attraction data.
    fetch(url).then((response) => {
        console.log(response);
        return response.json();
    }).then((data) => {
        console.log('Here is my json: ', data);
        // Reference the attractions div, we will add our list here.
        const display = document.querySelector('#attractions');
        // Create a <ul> wrapper. Remember we might of chosen to write the <ul> in rooms.html template and
        // append to it instead of the attractions <div>.
        const unordered_list = document.createElement('ul');
        // Loop, create <li>'s with attraction data and append them to the <ul>.
        data.forEach((attraction) => {
            let list_item = document.createElement('li');
            // Notice the dot notation for our JSON data and the template literals (back ticks).
            list_item.innerHTML = `${attraction.label} is $${attraction.admission} and has ${attraction.stars} stars.`;
            unordered_list.appendChild(list_item);
        });
        // Write our newly created list to the attractions div.
        display.appendChild(unordered_list);
    }).catch((error) => {
        // Good use of console.log()
        console.log(error);
    });

    // For every button, add an on-click event to book the Room, kinda :)
    document.querySelectorAll('button').forEach(function (button) {
        button.onclick = () => {
            alert('Thank you. Room is booked.');
            button.innerHTML = 'Room Booked.';
            button.style.color = button.dataset.color;
        }
    })
});

