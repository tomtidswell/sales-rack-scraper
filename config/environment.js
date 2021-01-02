// the or statements here allow a default if they havent been set with a .env file (ie in a production env)

const port = process.env.PORT || 4000
const dbURI = process.env.MONGODB_URI || 'mongodb://localhost/sales'
const secret = process.env.SECRET || 'tommykins rules ok'

module.exports = { port, dbURI, secret }
