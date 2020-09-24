$(document).ready(function () {
  $('#btn_translate').click(function () {
	  const leng = $('#language_code').val();
	  const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
	  $.get(url, function (response) {
      const hello = response.hello;
      $('#hello').append('<p>' + hello + '</p>');
	  });
  });
});
