document.addEventListener('DOMContentLoaded', function() {
    const thx = document.querySelector('#thx')
    const likes_data = document.querySelector('#likes-data')
    
    thx.onclick = function() {
        fetch('/thx_data', {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'slug': 'main'}),
        })
        .then(res => res.json())
        .then (
            data => {
                likes_data.textContent = data.likes_count
            })
    }
});