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
    result.characters.forEach(peopleUrl => {
      request(peopleUrl, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const people = JSON.parse(body);
          console.log(people.name);
        }
      });
    });
  }
}
);
