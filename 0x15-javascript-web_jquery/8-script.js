$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    const my_list = data.results;
    for (const i of my_list) {
      $('#list_movies').append('<li>' + i.title + '</li>');
    }
  });
});
