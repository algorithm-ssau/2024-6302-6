// Начало работы с back 
import express from "express";
import mongoose from "mongoose";
import cors from "cors";
// Подключение к базе данных MongoDB - const db - управление соединением
mongoose.connect("mongodb://localhost/animalshelter");
const db = mongoose.connection;
// Определение структуры документов 
const AnimalSchema = new mongoose.Schema({
  name: String,
  age: Number,
  description: String,
  type: String,
  image_url: String,
});

const Animal = mongoose.model("Animal", AnimalSchema);
// Импорт express
const app = express();
// Обработка JSON и URL-кодированных данных
app.use(express.json());
app.use(express.text());
// Cross-Origin Resource Sharing
app.use(cors());

// Запуск сервера на порту 3000
app.listen(3000);
// получени всех
app.get("/animals", async (req, res) => {
  const animals = await Animal.find();
  res.json(animals);
});
// получение по ID
app.get("/animals/:id", async (req, res) => {
  const animal = await Animal.findById(req.params.id);
  res.json(animal);
});
// создание
app.post("/animals", async (req, res) => {
  const animal = new Animal(JSON.parse(req.body));
  await animal.save();
  res.send("ok");
});
// обновление
app.put("/animals/:id", (req, res) => {});
// удаление 
app.delete("/animals/:id", (req, res) => {});
