require('dotenv').config();
const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.post("/form-submit", async (req, res) => {
  try {
    await axios.post(process.env.MY_ENV_VARIABLE, {
      username: req.body.username,
      password: req.body.password,
    });
    res.send("Data submitted successfully!");
  } catch (err) {
    res.status(500).send("Error submitting data");
  }
});

app.listen(3000, () => {
  console.log("Frontend server running on http://127.0.0.1:3000");
});
