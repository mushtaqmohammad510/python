document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            const dataDiv = document.getElementById('data');
            dataDiv.innerText = `${data.message}\nData: ${data.data.join(', ')}`;
        })
        .catch(error => console.error('Error fetching data:', error));
});
