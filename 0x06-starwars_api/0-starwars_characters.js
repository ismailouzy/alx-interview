#!/usr/bin/node


const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else if (response.statusCode !== 200) reject(new Error(`Invalid status code: ${response.statusCode}`));
        else resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(characterUrls.map(fetchCharacter))
    .then(characters => characters.forEach(name => console.log(name)))
    .catch(error => console.error('Error:', error));
});
