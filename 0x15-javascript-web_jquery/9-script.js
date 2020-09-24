$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (response) {
    const hello = response.hello;
    $('#hello').text('<p>' + hello + '</p>');
  });
});
