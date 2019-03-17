
function init() {
    var input = document.getElementById('locationTextField');
    var autocomplete = new google.maps.places.Autocomplete(input);
    var place = autocomplete.getPlace();
    $("#latlng").val(place.geometry.location);
}

google.maps.event.addDomListener(window, 'load', init);


function showPosition(position) {
    document.getElementById("locationTextField").value = position.coords.latitude + "," + position.coords.longitude
}

function getLocation() {
    navigator.geolocation.getCurrentPosition(showPosition);
}

function filterTable(rating) {
  var table, tr, td, i, txtValue;
  table = document.getElementById("cafes");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (parseFloat(txtValue) > rating) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
