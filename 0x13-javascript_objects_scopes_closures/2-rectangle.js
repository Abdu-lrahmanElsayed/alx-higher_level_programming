#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && w != null && h > 0 && h != null) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
