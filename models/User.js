const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  username: {
    type: String
  },
  googleID: {
    type: String,
    unique: true
  },
  first_name: {
    type: String
  },
  last_name: {
    type: String
  },
  facebookID: {
    type: String
  }
});

const User = mongoose.model("User", userSchema);

module.exports = User;
