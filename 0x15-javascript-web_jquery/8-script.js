$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (response) {
    const name = response.results;
    for (let cnt = 0; cnt < name.length; cnt++) {
      $('#list_movies').css('list-style-type', 'decimal');
      $('#list_movies').append('<li>' + name[cnt].title + '</li>');
    }
  });
});
