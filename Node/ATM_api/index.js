import express from 'express';

import userRoutes from "./routes/user.routes.js";

var app = express();
app.use(express.json());

// Endpoints
app.use('/users', userRoutes);
//TODO add more routes

// Default endpoint
app.use('/', (req, res) => {
  res.status(200).json({ ping: "pong", });
});

// Start application
app.listen(3000, function () {
  console.log("ATM app listening on port 3000!");
});