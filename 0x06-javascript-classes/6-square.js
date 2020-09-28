#!/usr/bin/node

module.exports = class Square {
  constructor (size = 0, pst = []) {
    try {
      if (!Number.isInteger(size)) throw 'size must be an integer';
      else if (size < 0) throw 'size must be >= 0';
      else if (typeof (pst) !== 'object') throw 'This datatype not valid';
      else {
        this._size = size;
        this._position = pst;
      }
    } catch (err) {
      console.log(err);
    }
  }

  area () {
    return this._size * this._size;
  }

  get position () {
    return this._position;
  }

  set position (value) {
    try {
      if (typeof (value) !== 'object' || value.length > 2) {
        throw 'position must be a array of 2 positive integers';
      }
    } catch (err) { return console.log(err); }
    this.position = value;
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
    if (this._size === 0) { console.log(' '); } else {
      for (let i = 0; i < this._size; i++) {
        console.log('_'.repeat(this.position[0]) + '#'.repeat(this._size));
      }
    }
  }
};
