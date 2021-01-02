//use this file to define the schema and model of the objects required for the api
//mongoose is an ODM (object data modeller)- an interface between the database and the programming language
const mongoose = require('mongoose')

const priceSchema = new mongoose.Schema({
    price: { type: String, required: true },
    priceDescription: { type: String, required: false },
    prevPrice: { type: String, required: false },
    prevPriceDescription: { type: String, required: false },
    discount: { type: String, required: false },
    badge: { type: String, required: false },
}, { timestamps: true })

// example setter
// function obfuscate (dBText) {
//     return "*****"
// }

// create the schema as a blueprint of a product
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    url: { type: String, required: true, unique: true },
    priceHistory: [ priceSchema ],
    // prices: { type: mongoose.Schema.ObjectId, ref: 'Prices' },
    main_image: { type: String },
    hover_image: { type: String },
    images: { type: Array },
    source: { type: String },
    retailer: { type: String },
    category: { type: String },
    // secret: { type: String, get: obfuscate },
}, {
    timestamps: true, 
    // toObject: { getters: true, setters: true },
    toJSON: { getters: true, setters: true }
})

// add a virtual field of latest price, which is just the most recent item from the price history
productSchema.virtual('latestPrice').get((value, virtual, doc)=>{
    return doc.priceHistory[doc.priceHistory.length - 1]
})

// small helper function to handle adding a new price
productSchema.methods.addPrice = function (priceData) {
    const prevPriceData = this.priceHistory.length ? this.priceHistory[this.priceHistory.length - 1] : {}
    // console.log('Prev price to string:', JSON.stringify(prevPriceData))
    if (prevPriceData.price !== priceData.price) this.priceHistory.push(priceData)
}


//this package enhances the validation made against the schema for unique entries, and it makes it more like the other types of schema validation
productSchema.plugin(require('mongoose-unique-validator'))

//register the schema as a model for a product object, and export it
module.exports = mongoose.model('Product', productSchema)
