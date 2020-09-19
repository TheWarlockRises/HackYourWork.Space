const mongoose = require("mongoose");
const uri = "mongodb://anna:momentsgang123@cluster0.hsobq.mongodb.net/users?retryWrites=true&w=majority";

mongoose.connect(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('MongoDB Connected...')
}).catch(err => console.log(err))
