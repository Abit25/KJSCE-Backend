const express = require("express");
const passport = require("passport");
const router = express.Router();

router.get("/google", passport.authenticate("google", { scope: ["profile"] }));

router.get("/google/redirect", passport.authenticate("google"), (req, res) => {
  console.log("Hi");
  res.redirect("http://localhost:3000");
});

router.get("/facebook", passport.authenticate("facebook"));

router.get(
  "/facebook/redirect",
  passport.authenticate("facebook"),
  (req, res) => {
    res.redirect("http://localhost:3000");
  }
);

const checkAuth = (req, res, next) => {
  if (!req.user) {
    res.status(401).send({ err: "Please Authenticate" });
  }
  res.send("Yaaaaay");
};

router.get("/add", checkAuth, (req, res) => {
  try {
    console.log("Done");
    res.send("Heya");
  } catch (error) {
    res.send(error);
  }
});

router.get("/isloggedin", (req, res) => {
  if (!req.user) {
    res.send({ status: 401 });
  } else {
    res.send({ status: 200, user: req.user });
  }
});

router.get("/logout", (req, res) => {
  req.logout();
  res.redirect("http://localhost:3000");
});

module.exports = router;
