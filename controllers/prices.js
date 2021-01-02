// const Product = require('../models/product')
// const { Price } = require('../models/price')

// // INDEX handler
// function indexRoute(req, res, next) {
//     Price
//         //access the query parameters in the url using req.query
//         .find(req.query)
//         .then(prices => res.status(200).json(prices))
//         .catch(next)
// }

// // SHOW handler
// function showRoute(req, res, next) {
//     Price
//         .findById(req.params.id)
//         .then(price => {
//             //.then will trigger if the id was valid, but does the price exist in the database?
//             if (!price) throw new Error('Not Found')
//             return res.status(200).json(price)
//         })
//         //an error will be thrown if the id was not valid
//         .catch(next)
// }


// // CREATE product price
// function createRoute(req, res, next) {
//     Product
//         .findById(req.params.id)
//         .then(product => {
//             if (!product) throw new Error('Not Found')
//             product.prices.push(req.body)
//             return product.save()
//         })
//         .then(product => {
//             if (!product) throw new Error('Error saving product price')
//             res.status(201).json(product)
//         })
//         .catch(next)
// }


// //build up the export object so it can simply be imported in the router file
// module.exports = {
//     index: indexRoute,
//     show: showRoute,
//     create: createRoute,
// }
