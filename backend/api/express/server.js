import express from "express";
import mongoose from "mongoose";

mongoose.connect("mongodb://localhost/animalshelter");
const db = mongoose.connection;

const AnimalSchema = new mongoose.Schema({
  name: String,
  age: Number,
  description: String,
});

const Animal = mongoose.model("Animal", AnimalSchema);

const app = express();
app.use(express.json());

app.listen(3000);

app.get("/animals", async (req, res) => {
  const animals = await Animal.find();
  res.json(animals);
});

app.get("/animals/:id", async (req, res) => {});

app.post("/animals", async (req, res) => {
  const animal = new Animal(req.body);
  await animal.save();
  res.send("ok");
});

app.put("/animals/:id", (req, res) => {});

app.delete("/animals/:id", (req, res) => {});
