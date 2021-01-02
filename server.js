// all the consts
const express = require('express')
const mongoose = require('mongoose')
const app = express()
const { port, dbURI } = require('./config/environment')
const router = require('./config/routes')
const bodyParser = require('body-parser')
const { requestLogger } = require('./lib/logger')
const errorHandler = require('./lib/errorHandler')

//connect to the database
mongoose.connect(dbURI, {useNewUrlParser: true }, ()=> console.log('Database connected'))

// register bodyparser before the router so that it can make use of its functionality
app.use(bodyParser.json())

// add some more adviced logging into the console, via a logging function
app.use(requestLogger)

// this adds api between the domain and the index, so that separates the front and backend routes to the api
app.use('/api', router)

// enhanced error handling capability. We can implement it here if we make use of the .next() method in the router for error messages
app.use(errorHandler)

// ensure we're lisening to the port
app.listen(port, () => console.log(`Listening on port ${port}`))
