function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Serviço de localização não disponível neste dispositivo.");
    }
}

function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const mapDiv = document.getElementById('map');
    mapDiv.innerHTML = `
        <iframe width="100%" height="100%" frameborder="0" style="border:0" 
        src="https://www.google.com/maps/embed/v1/view?key=AIzaSyD_MfWSPC_ZlxV3K0yy7XZB6dwc8EW_yzs
        &center=${lat},${lon}&zoom=15" allowfullscreen></iframe>
    `;
}

$(document).ready(function() {
    $('#checkinBtn').click(function() {
        const name = $('#name').val();
        const cpf = $('#cpf').val();
        if (name && cpf) {
            $.post('/checkin', { name: name, cpf: cpf }, function(data) {
                alert(data.message);
            });
        } else {
            alert("Por favor, preencha todos os campos.");
        }
    });

    $('#checkoutBtn').click(function() {
        const name = $('#name').val();
        const cpf = $('#cpf').val();
        if (name && cpf) {
            $.post('/checkout', { name: name, cpf: cpf }, function(data) {
                alert(data.message);
            });
        } else {
            alert("Por favor, preencha todos os campos.");
        }
    });

    getLocation();
});
