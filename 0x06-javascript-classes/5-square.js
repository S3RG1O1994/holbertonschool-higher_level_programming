#!/usr/bin/node

const { thistle } = require("color-name");

module.exports = class Square {
  constructor (size = 0) {
    try {
      if (!Number.isInteger(size)) throw 'size must be an integer';
      else if (size < 0) throw 'size must be >= 0';
      this._size = size;
    } catch (err) {
      console.log(err);
    }
  }

  area () {
    return this._size * this._size;
  }

  get size () {
    return this._size;
  }

  set size (value) {
    try {
      if (!Number.isInteger(value)) throw 'size must be an integer';
      else if (value < 0) throw 'size must be >= 0';
      this._size = value;
    } catch (err) {
      console.log(err);
    }
  }

  print () {
    if (this._size === 0) { console.log(" "); }
    else {
      for (let i = 0; i < this._size; i++) {
        console.log('#'.repeat(this._size));
      }
    }
  }
};
