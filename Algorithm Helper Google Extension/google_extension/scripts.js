
document.addEventListener('DOMContentLoaded', function () {
    const mic = document.getElementById('micButton');
    mic.addEventListener('click', function(){
        console.log('mic button pressed');
        
        fetch("http://localhost:5000/mic", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify('mic pressed!!')
        })
        .then(response => {
            return response.json();
        })
        .then(data =>{
            console.log('Recieved from Flask: ', data)
        })

    })
});