<template>
  <div id="app">
    <nav>
      <Navigation @shop="shop=$event" @category="category=$event"/>
    </nav>
    <main>
      <ProductsByRetailer v-if="shop && !category" :retailer="shop" />
      <ProductsByCategory v-else-if="!shop && category" :category="category" />
      <ProductsBest v-else :retailer="shop" />
    </main>
    <footer>Shop footer</footer>
  </div>
</template>

<script>
import ProductsByRetailer from "./ProductsByRetailer.vue"
import ProductsByCategory from "./ProductsByCategory.vue"
import ProductsBest from "./ProductsBest.vue"
import Navigation from "./Navigation.vue"

export default {
  name: "App",
  components: {
    ProductsByRetailer,
    ProductsByCategory,
    ProductsBest,
    Navigation,
  },
  data() {
    return {
      shop: null,
      category: null,
      filterOptions: [],
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-image: url("../assets/shopping-centre.jpg");
  background-color: #fbf4f5;
  background-attachment: fixed;
  background-size: cover;
  background-blend-mode: overlay;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  min-height: 80vh;
}
header {
  font-size: 2em;
}
main {
  flex-grow: 1;
}
</style>
