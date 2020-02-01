const passport = require("passport");
const GoogleStrategy = require("passport-google-oauth20");
const FacebookStrategy = require("passport-facebook");
const User = require("../models/User");

passport.serializeUser((user, done) => {
  done(null, user._id);
});

passport.deserializeUser(async (id, done) => {
  const user = await User.findById(id);
  done(null, user);
});

passport.use(
  new GoogleStrategy(
    {
      callbackURL: "/auth/google/redirect",
      clientID:
        "573557351496-v4al56hb5q58jcl9slphobcs01j8dlf5.apps.googleusercontent.com",
      clientSecret: "XNa0oQSrcRoG_2OVZI-EuF6p"
    },
    async (accessToken, refreshToken, profile, done) => {
      console.log(profile._json.given_name);
      const existUser = await User.findOne({ googleID: profile.id });
      if (existUser) {
        done(null, existUser);
      } else {
        const newUser = await new User({
          username: profile.displayName,
          googleID: profile.id,
          first_name: profile._json.given_name,
          last_name: profile._json.family_name
        }).save();

        done(null, newUser);
      }
    }
  )
);

passport.use(
  new FacebookStrategy(
    {
      callbackURL: "/auth/facebook/redirect",
      clientID: "2547900241974534",
      clientSecret: "f9c5793fd295a75aab4743f16c91bf06"
    },
    async (accessToken, refreshToken, profile, done) => {
      const existUser = await User.findOne({ facebookID: profile.id });
      if (existUser) {
        done(null, existUser);
      } else {
        const newUser = await new User({
          username: profile.displayName,
          facebookID: profile.id,
          first_name: profile.name.given_name,
          last_name: profile.name.family_name
        }).save();
        done(null, newUser);
      }
      console.log(profile);
    }
  )
);
