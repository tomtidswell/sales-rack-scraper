// next is used so the request doesnt get stuck inside this app.use statement - it moves it on to the next app.use
function requestLogger(req, res, next){
  console.log(`${req.method} to ${req.url}`)
  if(req.body) console.log('includes body:', req.body)
  next()
}

module.exports = { requestLogger }
