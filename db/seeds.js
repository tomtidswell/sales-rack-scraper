const mongoose = require('mongoose')
const { dbURI } = require('../config/environment')
const Product = require('../models/product')

// the idea of this file is that it lives standalone and acts as a re-seeder of the database during development

const productData = [
  {
    name: "Pure Cotton Luxury Spa Towel",
    prices: ['Sale price', '£6.00 - £18.00', 'Previous price'],
    url: "https://www.marksandspencer.com/pure-cotton-luxury-spa-towel/p/hbp60467039?color=WHITE#intid=prodColourId-60467042",
    badge: "40% off"
  },
  {
    name: "Temperature Comfort 10.5 Tog Duvet",
    prices: ['Sale price', '£29.70 - £41.40', 'Previous price'],
    url: "https://www.marksandspencer.com/temperature-comfort-10-5-tog-duvet/p/hbp60454341?color=WHITE",
    badge: "New"
  },
  {
    name: "Large Oval Platter",
    prices: ['Sale price', '£12.00', 'Previous price', '£20.0'],
    url: "https://www.marksandspencer.com/large-oval-platter/p/hbp60476526?color=WHITE",
    badge: "40% off"
  }
]



mongoose.connect(dbURI, {useNewUrlParser: true}, (err,db)=> {
  //some connection error handling, or confirmation of connection
  if(err) return console.log(`There is an error in connecting: ${err}`)
  else console.log(`Seeds file is connected to database`)
  
  mongoose.connection.db.dropCollection("products")
    .then((result, err) => {
      if(result) console.log("Collection droped")
      else console.log("Error dropping colleciton", err)
      return Product.create(productData)
    })
    .then(products => console.log(`${products.length} dinosaurs seeded into the database`))
    .catch(err => console.log(err))
    .finally(() => mongoose.connection.close())
  
})

