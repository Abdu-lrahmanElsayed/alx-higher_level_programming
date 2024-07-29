#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 | w == null | h <= 0 | h == null) {
      this.width;
      this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      } console.log();
    }
  }

  rotate () {
    this.height = this.width;
    this.width = this.height;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
