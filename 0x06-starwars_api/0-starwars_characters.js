#!/usr/bin/node
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

const args = process.argv.slice(2);

const url = baseUrl + args;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);

    // Use Promise.all to fetch character data concurrently
    const characterPromises = result.characters.map(peopleUrl => {
      return new Promise((resolve, reject) => {
        request(peopleUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const people = JSON.parse(body);
            resolve(people.name);
          }
        });
      });
    });
    Promise.all(characterPromises)
      .then(peopleNames => {
        peopleNames.forEach(name => {
          console.log(name);
        });
      });
  }
}
);
