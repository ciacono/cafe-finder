/*
function init() {
    var input = document.getElementById('locationTextField');
    var autocomplete = new google.maps.places.Autocomplete(input);
    var place = autocomplete.getPlace();
    $("#latlng").val(place.geometry.location);
}

google.maps.event.addDomListener(window, 'load', init);
*/

function showPosition(position) {
    document.getElementById("locationTextField").value = position.coords.latitude + "," + position.coords.longitude
}

function getLocation() {
    navigator.geolocation.getCurrentPosition(showPosition);
}