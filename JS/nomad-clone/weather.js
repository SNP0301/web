function onGeoOk() {

}

function onGeoError() {
    alert("where are you");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);