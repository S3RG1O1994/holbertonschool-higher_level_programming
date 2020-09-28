#!/usr/bin/node
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
};
