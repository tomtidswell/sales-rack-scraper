// //use this file to define the schema and model of the objects required for the api

// //mongoose is an ODM (object data modeller)- an interface between the database and the programming language
// const mongoose = require('mongoose')


// // const pricesSchema = new mongoose.Schema({
// //     //this schema object reference is used to refer to another schema and refer to a mongoose model
// //     prices: [ priceSchema ],
// //     // likes: { type: String }
// // }, { timestamps: false })

// // create the schema as a blueprint of a price
// const priceSchema = new mongoose.Schema({
//     price: { type: String, required: true },
//     displayedPrevPrice: { type: String, required: false },
//     discount: { type: String, required: false },
//     badge: { type: Boolean, required: false },
// }, { timestamps: true })

// //this package enhances the validation made against the schema for unique entries, and it makes it more like the other types of schema validation
// // priceSchema.plugin(require('mongoose-unique-validator'))

// //register the schema as a model for a price object, and export it
// module.exports = {
//     // Price: mongoose.model('Price', priceSchema),
//     priceSchema
// }
