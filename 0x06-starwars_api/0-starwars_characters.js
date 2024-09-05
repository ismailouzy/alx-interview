#!/usr/bin/node

const request = require('request');
const MovieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;

request(url, async (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          reject(err);
          return;
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});

