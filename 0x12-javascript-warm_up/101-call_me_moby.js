#!/usr/bin/node
module.exports.callMeMoby = function (x, callMeMoby){
  for (let cnt = 0; cnt < x; cnt += 1) {
    callMeMoby();
  }
};
