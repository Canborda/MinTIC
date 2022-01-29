import express from "express";
import userController from "../controllers/user.controller.js";

const router = express.Router();

router.get('/', userController.getAllUsers);
router.get('/:user_id', userController.getUserById);

router.post('/', userController.createUser);

export default router;
