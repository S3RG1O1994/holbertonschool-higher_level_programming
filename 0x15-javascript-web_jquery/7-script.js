$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (response) {
    const name = response.name;
    $('#character').append('<p>' + name + '</p>');
  });
});
