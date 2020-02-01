const express = require("express");
const app = express();
const passport = require("passport");
const mongoose = require("mongoose");
const cookie = require("cookie-session");
const authRouter = require("./routes/authRoutes");
const cors = require("cors");
require("./config/passport-setup");

mongoose.connect(
  "mongodb+srv://admin:admin@cluster0-x2onl.mongodb.net/mydb?retryWrites=true&w=majority",
  { useNewUrlParser: true, useUnifiedTopology: true },
  () => {
    console.log("Connected succesfully to MongoDB");
  }
);

// var corsOptions = {
//   origin: "http://localhost:3000"
//   // some legacy browsers (IE11, various SmartTVs) choke on 204
// };
// app.use(cors(corsOptions));
app.use(function(req, res, next) {
  // Website you wish to allow to connect
  res.setHeader("Access-Control-Allow-Origin", "http://localhost:3000");

  // Request methods you wish to allow
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );

  // Request headers you wish to allow
  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-Requested-With,content-type"
  );

  // Set to true if you need the website to include cookies in the requests sent
  // to the API (e.g. in case you use sessions)
  res.setHeader("Access-Control-Allow-Credentials", true);

  // Pass to next layer of middleware
  next();
});

app.use(
  cookie({
    maxAge: 24 * 60 * 60 * 1000,
    keys: ["hwhrhriqbdiuv89545"]
  })
);

app.use(passport.initialize());
app.use(passport.session());

app.use("/auth", authRouter);

app.listen(8080, () => {
  console.log("Listening on port 8080");
});
