
class UserController {

  async getAllUsers(req, res) {
    res.json({ method: "getAllUsers" });
  }

  async getUserById(req, res) {
    res.json({ method: "getUserById", params: req.params });
  }

  async getUserByParam(req, res) {

    console.log(req.params);
    res.json({method: "getUserByParam", params: "ds"});
  }

  async createUser(req, res) {
    res.json({ method: "createUser", body: req.body });
  }

}

export default new UserController();