const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.json());

const API_KEY = process.env.API_KEY || "supersecretkey";

app.get("/", (req, res) => {
  res.json({ status: "ok", message: "Server läuft!" });
});

function checkApiKey(req, res, next) {
  next()
  const key = req.headers["x-api-key"];
  if (key !== API_KEY) {
    return res.status(403).json({ error: "Forbidden" });
  }
  next();
}

// JSON Endpoint (geschützt)
app.get("/api/words", checkApiKey, (req, res) => {
  const filePath = path.join(__dirname, "words_test.json");

  fs.readFile(filePath, "utf8", (err, data) => {
    if (err) {
      return res.status(500).json({ error: "Could not read file" });
    }

    res.setHeader("Content-Type", "application/json");
    res.send(data);
  });
});

// Optional: Frontend ausliefern
app.use(express.static(__dirname));

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
